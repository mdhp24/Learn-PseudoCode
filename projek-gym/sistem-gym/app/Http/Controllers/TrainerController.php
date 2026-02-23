<?php

namespace App\Http\Controllers;

use App\Models\ClassSchedule;
use App\Models\Trainer;
use App\Models\User;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;

class TrainerController extends Controller
{
    public function index(Request $request)
    {
        $query = Trainer::with('user');

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('specialization', 'like', "%{$search}%")
                  ->orWhere('phone', 'like', "%{$search}%")
                  ->orWhereHas('user', function ($q2) use ($search) {
                      $q2->where('name', 'like', "%{$search}%")
                         ->orWhere('email', 'like', "%{$search}%");
                  });
            });
        }

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $trainers = $query->latest()->paginate(10)->withQueryString();
        
        return view('trainers.index', compact('trainers'));
    }

    public function create()
    {
        return view('trainers.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name'              => 'required|string|max:255',
            'email'             => 'required|email|unique:users,email',
            'phone'             => 'required|string|max:20',
            'specialization'    => 'required|string|max:255',
            'certifications'    => 'nullable|string',
            'experience_years'  => 'nullable|integer|min:0|max:50',
            'bio'               => 'nullable|string',
            'hire_date'         => 'nullable|date',
        ]);

        DB::beginTransaction();
        try {
            // Create user
            $user = User::create([
                'name'     => $request->name,
                'email'    => $request->email,
                'password' => Hash::make('password123'),
                'role'     => 'trainer',
            ]);

            // Create trainer
            $trainer = Trainer::create([
                'user_id'           => $user->id,
                'phone'             => $request->phone,
                'specialization'    => $request->specialization,
                'certifications'    => $request->certifications,
                'experience_years'  => $request->experience_years ?? 0,
                'bio'               => $request->bio,
                'hire_date'         => $request->hire_date ?? Carbon::today(),
                'status'            => 'active',
            ]);

            DB::commit();

            return redirect()->route('trainers.show', $trainer)
                ->with('success', "Trainer {$user->name} berhasil ditambahkan!");

        } catch (\Exception $e) {
            DB::rollBack();
            return back()->withInput()
                ->with('error', 'Gagal menambahkan trainer: ' . $e->getMessage());
        }
    }

    public function show(Trainer $trainer)
    {
        $trainer->load('user');

        // Get trainer statistics
        $stats = [
            'total_classes' => ClassSchedule::where('trainer_id', $trainer->id)->count(),
            'upcoming_classes' => ClassSchedule::where('trainer_id', $trainer->id)
                ->where('date', '>=', Carbon::today())
                ->where('status', 'scheduled')
                ->count(),
            'completed_classes' => ClassSchedule::where('trainer_id', $trainer->id)
                ->where('status', 'completed')
                ->count(),
        ];

        // Get upcoming schedules
        $upcomingSchedules = ClassSchedule::where('trainer_id', $trainer->id)
            ->where('date', '>=', Carbon::today())
            ->where('status', 'scheduled')
            ->with('gymClass')
            ->orderBy('date')
            ->orderBy('start_time')
            ->take(10)
            ->get();

        // Get recent schedules
        $recentSchedules = ClassSchedule::where('trainer_id', $trainer->id)
            ->where('date', '<', Carbon::today())
            ->with('gymClass')
            ->latest('date')
            ->take(10)
            ->get();

        return view('trainers.show', compact('trainer', 'stats', 'upcomingSchedules', 'recentSchedules'));
    }

    public function edit(Trainer $trainer)
    {
        $trainer->load('user');
        return view('trainers.edit', compact('trainer'));
    }

    public function update(Request $request, Trainer $trainer)
    {
        $request->validate([
            'name'              => 'required|string|max:255',
            'email'             => 'required|email|unique:users,email,' . $trainer->user_id,
            'phone'             => 'required|string|max:20',
            'specialization'    => 'required|string|max:255',
            'certifications'    => 'nullable|string',
            'experience_years'  => 'nullable|integer|min:0|max:50',
            'bio'               => 'nullable|string',
            'hire_date'         => 'nullable|date',
            'status'            => 'required|in:active,inactive,on_leave',
        ]);

        $trainer->user->update([
            'name'  => $request->name,
            'email' => $request->email,
        ]);

        $trainer->update([
            'phone'             => $request->phone,
            'specialization'    => $request->specialization,
            'certifications'    => $request->certifications,
            'experience_years'  => $request->experience_years ?? 0,
            'bio'               => $request->bio,
            'hire_date'         => $request->hire_date,
            'status'            => $request->status,
        ]);

        return redirect()->route('trainers.show', $trainer)
            ->with('success', 'Data trainer berhasil diperbarui!');
    }

    public function destroy(Trainer $trainer)
    {
        // Check if has future schedules
        $futureSchedules = ClassSchedule::where('trainer_id', $trainer->id)
            ->where('date', '>=', Carbon::today())
            ->where('status', 'scheduled')
            ->count();

        if ($futureSchedules > 0) {
            return back()->with('error',
                "Tidak dapat menghapus trainer yang memiliki {$futureSchedules} jadwal aktif!");
        }

        $name = $trainer->user->name;
        $trainer->user->delete();

        return redirect()->route('trainers.index')
            ->with('success', "Trainer {$name} berhasil dihapus.");
    }

    public function schedule(Trainer $trainer, Request $request)
    {
        $query = ClassSchedule::where('trainer_id', $trainer->id)
            ->with('gymClass');

        // Filter by date range
        if ($request->filled('date_from')) {
            $query->where('date', '>=', $request->date_from);
        } else {
            $query->where('date', '>=', Carbon::today()->subDays(30));
        }

        if ($request->filled('date_to')) {
            $query->where('date', '<=', $request->date_to);
        }

        // Filter by status
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $schedules = $query->orderBy('date')
            ->orderBy('start_time')
            ->paginate(15)
            ->withQueryString();

        return view('trainers.schedule', compact('trainer', 'schedules'));
    }
}

