<?php

namespace App\Http\Controllers;

use App\Models\Attendance;
use App\Models\Member;
use Carbon\Carbon;
use Illuminate\Http\Request;

class AttendanceController extends Controller
{
    public function index(Request $request)
    {
        $query = Attendance::with('member.user');

        if ($request->filled('date')) {
            $query->whereDate('date', $request->date);
        } else {
            $query->whereDate('date', Carbon::today());
        }

        if ($request->filled('search')) {
            $query->whereHas('member', function ($q) use ($request) {
                $q->where('member_code', 'like', "%{$request->search}%")
                  ->orWhereHas('user', fn($q2) => $q2->where('name', 'like', "%{$request->search}%"));
            });
        }

        $attendances = $query->latest('check_in')->paginate(15)->withQueryString();
        $members = Member::where('status', 'active')->with('user')->get();

        return view('attendances.index', compact('attendances', 'members'));
    }

    public function checkIn(Request $request)
    {
        $request->validate([
            'member_id' => 'required|exists:members,id',
        ]);

        $existing = Attendance::where('member_id', $request->member_id)
            ->whereDate('date', Carbon::today())
            ->whereNull('check_out')
            ->first();

        if ($existing) {
            return back()->with('error', 'Member ini sudah check-in dan belum check-out.');
        }

        Attendance::create([
            'member_id' => $request->member_id,
            'date'      => Carbon::today(),
            'check_in'  => Carbon::now()->format('H:i:s'),
        ]);

        $member = Member::with('user')->find($request->member_id);
        return back()->with('success', "Check-in berhasil untuk {$member->user->name}!");
    }

    public function checkOut(Attendance $attendance)
    {
        if ($attendance->check_out) {
            return back()->with('error', 'Member ini sudah check-out.');
        }

        $checkIn  = Carbon::createFromFormat('H:i:s', $attendance->check_in);
        $checkOut = Carbon::now();
        $duration = $checkIn->diffInMinutes($checkOut);

        $attendance->update([
            'check_out'        => $checkOut->format('H:i:s'),
            'duration_minutes' => $duration,
        ]);

        return back()->with('success', 'Check-out berhasil! Durasi latihan: ' . $duration . ' menit.');
    }
}
