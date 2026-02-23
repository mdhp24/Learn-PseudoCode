<?php

namespace App\Http\Controllers;

use App\Models\ClassBooking;
use App\Models\ClassSchedule;
use App\Models\Member;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class ClassBookingController extends Controller
{
    public function index(Request $request)
    {
        $query = ClassBooking::with(['member.user', 'schedule.gymClass', 'schedule.trainer.user']);

        // Filter by member
        if ($request->filled('member_id')) {
            $query->where('member_id', $request->member_id);
        }

        // Filter by status
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        // Filter by date range
        if ($request->filled('date_from')) {
            $query->where('booking_date', '>=', $request->date_from);
        }
        if ($request->filled('date_to')) {
            $query->where('booking_date', '<=', $request->date_to);
        }

        // Search
        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->whereHas('member.user', function ($q2) use ($search) {
                    $q2->where('name', 'like', "%{$search}%");
                })->orWhereHas('member', function ($q2) use ($search) {
                    $q2->where('member_code', 'like', "%{$search}%");
                });
            });
        }

        $bookings = $query->latest('booking_date')->paginate(15)->withQueryString();
        $members = Member::with('user')->where('status', 'active')->get();

        return view('bookings.index', compact('bookings', 'members'));
    }

    public function create(Request $request)
    {
        $members = Member::with('user')->where('status', 'active')->get();
        
        // Get upcoming schedules
        $schedules = ClassSchedule::with(['gymClass', 'trainer.user'])
            ->where('date', '>=', Carbon::today())
            ->where('status', 'scheduled')
            ->orderBy('date')
            ->orderBy('start_time')
            ->get();

        $selectedSchedule = $request->filled('schedule_id') 
            ? ClassSchedule::with(['gymClass', 'trainer.user'])->find($request->schedule_id) 
            : null;

        return view('bookings.create', compact('members', 'schedules', 'selectedSchedule'));
    }

    public function store(Request $request)
    {
        $request->validate([
            'member_id'            => 'required|exists:members,id',
            'class_schedule_id'    => 'required|exists:class_schedules,id',
            'notes'                => 'nullable|string',
        ]);

        $member = Member::findOrFail($request->member_id);
        $schedule = ClassSchedule::with('gymClass')->findOrFail($request->class_schedule_id);

        // Check if member is active
        if ($member->status !== 'active') {
            return back()->withInput()->with('error', 'Member tidak aktif!');
        }

        // Check if schedule is available
        if ($schedule->status !== 'scheduled') {
            return back()->withInput()->with('error', 'Jadwal kelas tidak tersedia!');
        }

        // Check capacity
        $currentBookings = ClassBooking::where('class_schedule_id', $schedule->id)
            ->whereIn('status', ['confirmed', 'attended'])
            ->count();

        if ($currentBookings >= $schedule->capacity) {
            return back()->withInput()->with('error', 'Kelas sudah penuh!');
        }

        // Check if already booked
        $existingBooking = ClassBooking::where('member_id', $member->id)
            ->where('class_schedule_id', $schedule->id)
            ->whereIn('status', ['confirmed', 'attended'])
            ->exists();

        if ($existingBooking) {
            return back()->withInput()->with('error', 'Member sudah booking kelas ini!');
        }

        // Check if member has active membership with class credits
        $activeMembership = $member->activeMembership;
        if (!$activeMembership) {
            return back()->withInput()->with('error', 'Member tidak memiliki membership aktif!');
        }

        // Check class credits if required
        if ($schedule->gymClass->requires_booking && $activeMembership->remaining_class_credits <= 0) {
            return back()->withInput()->with('error', 'Kredit kelas tidak mencukupi!');
        }

        DB::beginTransaction();
        try {
            // Create booking
            $booking = ClassBooking::create([
                'member_id'         => $member->id,
                'class_schedule_id' => $schedule->id,
                'booking_code'      => $this->generateBookingCode(),
                'booking_date'      => Carbon::now(),
                'status'            => 'confirmed',
                'notes'             => $request->notes,
                'booked_by'         => Auth::id(),
            ]);

            // Deduct class credit if required
            if ($schedule->gymClass->requires_booking && $activeMembership->package->class_credits > 0) {
                $activeMembership->decrement('remaining_class_credits');
            }

            DB::commit();

            return redirect()->route('bookings.show', $booking)
                ->with('success', 'Booking kelas berhasil! Kode booking: ' . $booking->booking_code);

        } catch (\Exception $e) {
            DB::rollBack();
            return back()->withInput()->with('error', 'Gagal membuat booking: ' . $e->getMessage());
        }
    }

    public function show(ClassBooking $booking)
    {
        $booking->load([
            'member.user',
            'member.activeMembership.package',
            'schedule.gymClass',
            'schedule.trainer.user',
            'bookedBy',
        ]);

        return view('bookings.show', compact('booking'));
    }

    public function cancel(ClassBooking $booking)
    {
        if (!in_array($booking->status, ['confirmed'])) {
            return back()->with('error', 'Booking tidak dapat dibatalkan!');
        }

        // Check if cancellation is allowed (e.g., at least 2 hours before class)
        $scheduleDateTime = Carbon::parse($booking->schedule->date . ' ' . $booking->schedule->start_time);
        $now = Carbon::now();

        if ($now->diffInHours($scheduleDateTime, false) < 2) {
            return back()->with('error', 'Pembatalan harus dilakukan minimal 2 jam sebelum kelas dimulai!');
        }

        DB::beginTransaction();
        try {
            // Refund class credit if applicable
            $activeMembership = $booking->member->activeMembership;
            if ($activeMembership && $booking->schedule->gymClass->requires_booking) {
                $activeMembership->increment('remaining_class_credits');
            }

            $booking->update([
                'status'        => 'cancelled',
                'cancelled_at'  => Carbon::now(),
                'cancelled_by'  => Auth::id(),
            ]);

            DB::commit();

            return redirect()->route('bookings.index')
                ->with('success', 'Booking berhasil dibatalkan!');

        } catch (\Exception $e) {
            DB::rollBack();
            return back()->with('error', 'Gagal membatalkan booking: ' . $e->getMessage());
        }
    }

    public function markAttended(ClassBooking $booking)
    {
        if ($booking->status !== 'confirmed') {
            return back()->with('error', 'Hanya booking dengan status confirmed yang dapat diabsen!');
        }

        $booking->update([
            'status'      => 'attended',
            'attended_at' => Carbon::now(),
        ]);

        return back()->with('success', 'Member berhasil diabsen!');
    }

    public function markNoShow(ClassBooking $booking)
    {
        if ($booking->status !== 'confirmed') {
            return back()->with('error', 'Status booking tidak valid!');
        }

        // Check if class time has passed
        $scheduleDateTime = Carbon::parse($booking->schedule->date . ' ' . $booking->schedule->start_time);
        if (Carbon::now()->lt($scheduleDateTime)) {
            return back()->with('error', 'Tidak dapat menandai no-show sebelum jadwal kelas!');
        }

        $booking->update([
            'status' => 'no_show',
        ]);

        return back()->with('success', 'Booking ditandai sebagai no-show!');
    }

    public function myBookings()
    {
        $user = Auth::user();
        
        if ($user->role !== 'member') {
            return redirect()->route('bookings.index');
        }

        $member = Member::where('user_id', $user->id)->firstOrFail();
        
        $bookings = ClassBooking::with(['schedule.gymClass', 'schedule.trainer.user'])
            ->where('member_id', $member->id)
            ->latest('booking_date')
            ->paginate(10);

        return view('bookings.my-bookings', compact('bookings', 'member'));
    }

    private function generateBookingCode()
    {
        $date = Carbon::today()->format('Ymd');
        $count = ClassBooking::whereDate('booking_date', Carbon::today())->count() + 1;
        return 'BKG-' . $date . '-' . str_pad($count, 4, '0', STR_PAD_LEFT);
    }

    public function availableSchedules(Request $request)
    {
        $query = ClassSchedule::with(['gymClass', 'trainer.user'])
            ->where('date', '>=', Carbon::today())
            ->where('status', 'scheduled');

        // Filter by date
        if ($request->filled('date')) {
            $query->whereDate('date', $request->date);
        }

        // Filter by class
        if ($request->filled('gym_class_id')) {
            $query->where('gym_class_id', $request->gym_class_id);
        }

        $schedules = $query->orderBy('date')
            ->orderBy('start_time')
            ->get()
            ->map(function ($schedule) {
                $bookedCount = ClassBooking::where('class_schedule_id', $schedule->id)
                    ->whereIn('status', ['confirmed', 'attended'])
                    ->count();
                
                $schedule->available_slots = max(0, $schedule->capacity - $bookedCount);
                $schedule->is_full = $schedule->available_slots === 0;
                
                return $schedule;
            });

        return response()->json($schedules);
    }
}
