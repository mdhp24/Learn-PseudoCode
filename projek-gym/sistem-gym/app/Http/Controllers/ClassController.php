<?php

namespace App\Http\Controllers;

use App\Models\ClassBooking;
use App\Models\ClassSchedule;
use App\Models\GymClass;
use App\Models\Trainer;
use Carbon\Carbon;
use Illuminate\Http\Request;

class ClassController extends Controller
{
    // ==================== GYM CLASSES ====================
    
    public function index(Request $request)
    {
        $query = GymClass::query();

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                  ->orWhere('description', 'like', "%{$search}%");
            });
        }

        if ($request->filled('is_active')) {
            $query->where('is_active', $request->is_active);
        }

        $classes = $query->withCount('schedules')->latest()->paginate(10)->withQueryString();
        
        return view('classes.index', compact('classes'));
    }

    public function create()
    {
        return view('classes.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name'              => 'required|string|max:255',
            'description'       => 'nullable|string',
            'duration_minutes'  => 'required|integer|min:15|max:180',
            'difficulty_level'  => 'required|in:beginner,intermediate,advanced',
            'max_participants'  => 'required|integer|min:1|max:100',
            'requires_booking'  => 'boolean',
            'is_active'         => 'boolean',
        ]);

        $gymClass = GymClass::create([
            'name'              => $request->name,
            'description'       => $request->description,
            'duration_minutes'  => $request->duration_minutes,
            'difficulty_level'  => $request->difficulty_level,
            'max_participants'  => $request->max_participants,
            'requires_booking'  => $request->has('requires_booking'),
            'is_active'         => $request->has('is_active'),
        ]);

        return redirect()->route('classes.show', $gymClass)
            ->with('success', "Kelas {$gymClass->name} berhasil ditambahkan!");
    }

    public function show(GymClass $class)
    {
        $class->loadCount([
            'schedules',
            'schedules as upcoming_schedules_count' => function ($q) {
                $q->where('date', '>=', Carbon::today())
                  ->where('status', 'scheduled');
            }
        ]);

        $upcomingSchedules = ClassSchedule::where('gym_class_id', $class->id)
            ->where('date', '>=', Carbon::today())
            ->with(['trainer.user'])
            ->orderBy('date')
            ->orderBy('start_time')
            ->get()
            ->map(function ($schedule) {
                $bookedCount = ClassBooking::where('class_schedule_id', $schedule->id)
                    ->whereIn('status', ['confirmed', 'attended'])
                    ->count();
                $schedule->booked_count = $bookedCount;
                $schedule->available_slots = max(0, $schedule->capacity - $bookedCount);
                return $schedule;
            });

        return view('classes.show', compact('class', 'upcomingSchedules'));
    }

    public function edit(GymClass $class)
    {
        return view('classes.edit', compact('class'));
    }

    public function update(Request $request, GymClass $class)
    {
        $request->validate([
            'name'              => 'required|string|max:255',
            'description'       => 'nullable|string',
            'duration_minutes'  => 'required|integer|min:15|max:180',
            'difficulty_level'  => 'required|in:beginner,intermediate,advanced',
            'max_participants'  => 'required|integer|min:1|max:100',
            'requires_booking'  => 'boolean',
            'is_active'         => 'boolean',
        ]);

        $class->update([
            'name'              => $request->name,
            'description'       => $request->description,
            'duration_minutes'  => $request->duration_minutes,
            'difficulty_level'  => $request->difficulty_level,
            'max_participants'  => $request->max_participants,
            'requires_booking'  => $request->has('requires_booking'),
            'is_active'         => $request->has('is_active'),
        ]);

        return redirect()->route('classes.show', $class)
            ->with('success', 'Data kelas berhasil diperbarui!');
    }

    public function destroy(GymClass $class)
    {
        // Check if has future schedules
        $futureSchedules = ClassSchedule::where('gym_class_id', $class->id)
            ->where('date', '>=', Carbon::today())
            ->where('status', 'scheduled')
            ->count();

        if ($futureSchedules > 0) {
            return back()->with('error', 
                'Tidak dapat menghapus kelas yang masih memiliki jadwal aktif!');
        }

        $name = $class->name;
        $class->delete();

        return redirect()->route('classes.index')
            ->with('success', "Kelas {$name} berhasil dihapus.");
    }

    // ==================== CLASS SCHEDULES ====================

    public function schedules(Request $request)
    {
        $query = ClassSchedule::with(['gymClass', 'trainer.user']);

        // Filter by date range
        if ($request->filled('date_from')) {
            $query->where('date', '>=', $request->date_from);
        } else {
            // Default: show from today
            $query->where('date', '>=', Carbon::today());
        }

        if ($request->filled('date_to')) {
            $query->where('date', '<=', $request->date_to);
        }

        // Filter by class
        if ($request->filled('gym_class_id')) {
            $query->where('gym_class_id', $request->gym_class_id);
        }

        // Filter by trainer
        if ($request->filled('trainer_id')) {
            $query->where('trainer_id', $request->trainer_id);
        }

        // Filter by status
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $schedules = $query->orderBy('date')
            ->orderBy('start_time')
            ->paginate(15)
            ->withQueryString();

        // Add booking count to each schedule
        $schedules->getCollection()->transform(function ($schedule) {
            $bookedCount = ClassBooking::where('class_schedule_id', $schedule->id)
                ->whereIn('status', ['confirmed', 'attended'])
                ->count();
            $schedule->booked_count = $bookedCount;
            $schedule->available_slots = max(0, $schedule->capacity - $bookedCount);
            return $schedule;
        });

        $classes = GymClass::where('is_active', true)->get();
        $trainers = Trainer::with('user')->where('status', 'active')->get();

        return view('classes.schedules.index', compact('schedules', 'classes', 'trainers'));
    }

    public function createSchedule(Request $request)
    {
        $classes = GymClass::where('is_active', true)->get();
        $trainers = Trainer::with('user')->where('status', 'active')->get();

        $selectedClass = $request->filled('gym_class_id')
            ? GymClass::find($request->gym_class_id)
            : null;

        return view('classes.schedules.create', compact('classes', 'trainers', 'selectedClass'));
    }

    public function storeSchedule(Request $request)
    {
        $request->validate([
            'gym_class_id'  => 'required|exists:gym_classes,id',
            'trainer_id'    => 'required|exists:trainers,id',
            'date'          => 'required|date|after_or_equal:today',
            'start_time'    => 'required|date_format:H:i',
            'end_time'      => 'required|date_format:H:i|after:start_time',
            'capacity'      => 'nullable|integer|min:1|max:100',
            'room'          => 'nullable|string|max:100',
            'notes'         => 'nullable|string',
        ]);

        $gymClass = GymClass::findOrFail($request->gym_class_id);

        // Check trainer availability
        $conflictingSchedule = ClassSchedule::where('trainer_id', $request->trainer_id)
            ->where('date', $request->date)
            ->where('status', 'scheduled')
            ->where(function ($q) use ($request) {
                $q->whereBetween('start_time', [$request->start_time, $request->end_time])
                  ->orWhereBetween('end_time', [$request->start_time, $request->end_time])
                  ->orWhere(function ($q2) use ($request) {
                      $q2->where('start_time', '<=', $request->start_time)
                         ->where('end_time', '>=', $request->end_time);
                  });
            })
            ->exists();

        if ($conflictingSchedule) {
            return back()->withInput()
                ->with('error', 'Trainer sudah memiliki jadwal pada waktu tersebut!');
        }

        $schedule = ClassSchedule::create([
            'gym_class_id'  => $request->gym_class_id,
            'trainer_id'    => $request->trainer_id,
            'date'          => $request->date,
            'start_time'    => $request->start_time,
            'end_time'      => $request->end_time,
            'capacity'      => $request->capacity ?? $gymClass->max_participants,
            'room'          => $request->room,
            'status'        => 'scheduled',
            'notes'         => $request->notes,
        ]);

        return redirect()->route('classes.schedules.show', $schedule)
            ->with('success', 'Jadwal kelas berhasil ditambahkan!');
    }

    public function showSchedule(ClassSchedule $schedule)
    {
        $schedule->load(['gymClass', 'trainer.user']);

        $bookings = ClassBooking::where('class_schedule_id', $schedule->id)
            ->with('member.user')
            ->latest('booking_date')
            ->get();

        $stats = [
            'total_bookings'    => $bookings->count(),
            'confirmed'         => $bookings->where('status', 'confirmed')->count(),
            'attended'          => $bookings->where('status', 'attended')->count(),
            'no_show'           => $bookings->where('status', 'no_show')->count(),
            'cancelled'         => $bookings->where('status', 'cancelled')->count(),
            'available_slots'   => max(0, $schedule->capacity - $bookings->whereIn('status', ['confirmed', 'attended'])->count()),
        ];

        return view('classes.schedules.show', compact('schedule', 'bookings', 'stats'));
    }

    public function editSchedule(ClassSchedule $schedule)
    {
        $schedule->load(['gymClass', 'trainer']);
        $classes = GymClass::where('is_active', true)->get();
        $trainers = Trainer::with('user')->where('status', 'active')->get();

        return view('classes.schedules.edit', compact('schedule', 'classes', 'trainers'));
    }

    public function updateSchedule(Request $request, ClassSchedule $schedule)
    {
        $request->validate([
            'gym_class_id'  => 'required|exists:gym_classes,id',
            'trainer_id'    => 'required|exists:trainers,id',
            'date'          => 'required|date',
            'start_time'    => 'required|date_format:H:i',
            'end_time'      => 'required|date_format:H:i|after:start_time',
            'capacity'      => 'nullable|integer|min:1|max:100',
            'room'          => 'nullable|string|max:100',
            'status'        => 'required|in:scheduled,cancelled,completed',
            'notes'         => 'nullable|string',
        ]);

        // Check trainer availability (exclude current schedule)
        $conflictingSchedule = ClassSchedule::where('trainer_id', $request->trainer_id)
            ->where('date', $request->date)
            ->where('status', 'scheduled')
            ->where('id', '!=', $schedule->id)
            ->where(function ($q) use ($request) {
                $q->whereBetween('start_time', [$request->start_time, $request->end_time])
                  ->orWhereBetween('end_time', [$request->start_time, $request->end_time])
                  ->orWhere(function ($q2) use ($request) {
                      $q2->where('start_time', '<=', $request->start_time)
                         ->where('end_time', '>=', $request->end_time);
                  });
            })
            ->exists();

        if ($conflictingSchedule) {
            return back()->withInput()
                ->with('error', 'Trainer sudah memiliki jadwal pada waktu tersebut!');
        }

        // Check if reducing capacity below current bookings
        $confirmedBookings = ClassBooking::where('class_schedule_id', $schedule->id)
            ->whereIn('status', ['confirmed', 'attended'])
            ->count();

        $newCapacity = $request->capacity ?? $schedule->capacity;
        if ($newCapacity < $confirmedBookings) {
            return back()->withInput()
                ->with('error', "Kapasitas tidak dapat dikurangi di bawah jumlah booking yang sudah dikonfirmasi ({$confirmedBookings})!");
        }

        $schedule->update([
            'gym_class_id'  => $request->gym_class_id,
            'trainer_id'    => $request->trainer_id,
            'date'          => $request->date,
            'start_time'    => $request->start_time,
            'end_time'      => $request->end_time,
            'capacity'      => $newCapacity,
            'room'          => $request->room,
            'status'        => $request->status,
            'notes'         => $request->notes,
        ]);

        return redirect()->route('classes.schedules.show', $schedule)
            ->with('success', 'Jadwal kelas berhasil diperbarui!');
    }

    public function destroySchedule(ClassSchedule $schedule)
    {
        // Check if has confirmed bookings
        $confirmedBookings = ClassBooking::where('class_schedule_id', $schedule->id)
            ->whereIn('status', ['confirmed', 'attended'])
            ->count();

        if ($confirmedBookings > 0) {
            return back()->with('error',
                "Tidak dapat menghapus jadwal yang memiliki {$confirmedBookings} booking aktif!");
        }

        $schedule->delete();

        return redirect()->route('classes.schedules.index')
            ->with('success', 'Jadwal kelas berhasil dihapus.');
    }

    public function cancelSchedule(ClassSchedule $schedule)
    {
        if ($schedule->status !== 'scheduled') {
            return back()->with('error', 'Hanya jadwal dengan status scheduled yang dapat dibatalkan!');
        }

        $schedule->update(['status' => 'cancelled']);

        // Update all confirmed bookings to cancelled
        ClassBooking::where('class_schedule_id', $schedule->id)
            ->where('status', 'confirmed')
            ->update([
                'status'       => 'cancelled',
                'cancelled_at' => Carbon::now(),
            ]);

        return back()->with('success', 'Jadwal kelas berhasil dibatalkan!');
    }

    public function completeSchedule(ClassSchedule $schedule)
    {
        if ($schedule->status !== 'scheduled') {
            return back()->with('error', 'Status jadwal tidak valid!');
        }

        $schedule->update(['status' => 'completed']);

        // Mark confirmed bookings as no-show
        ClassBooking::where('class_schedule_id', $schedule->id)
            ->where('status', 'confirmed')
            ->update(['status' => 'no_show']);

        return back()->with('success', 'Jadwal kelas ditandai selesai!');
    }
}
