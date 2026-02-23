<?php

namespace App\Http\Controllers;

use App\Models\Member;
use App\Models\Payment;
use App\Models\Attendance;
use App\Models\MemberMembership;
use App\Models\ClassBooking;
use App\Models\Equipment;
use Carbon\Carbon;
// use Illuminate\Http\Request;

class DashboardController extends Controller
{
    public function index()
    {
        $today = Carbon::today();

        // Statistik utama
        $totalMembers      = Member::count();
        $activeMembers     = Member::where('status', 'active')->count();
        $todayAttendances  = Attendance::whereDate('date', $today)->count();
        $monthlyRevenue    = Payment::where('status', 'paid')
                                ->whereBetween('payment_date', [
                                    $today->copy()->startOfMonth(),
                                    $today->copy()->endOfMonth()
                                ])
                                ->sum('total');

        // Member baru bulan ini
        $newMembersThisMonth = Member::whereMonth('joined_date', $today->month)
                                     ->whereYear('joined_date', $today->year)
                                     ->count();

        // Membership yang akan expired dalam 7 hari
        $expiringMemberships = MemberMembership::where('status', 'active')
            ->whereBetween('end_date', [$today, $today->copy()->addDays(7)])
            ->with(['member.user', 'package'])
            ->get();

        // Absensi hari ini (terbaru)
        $todayAttendanceList = Attendance::whereDate('date', $today)
            ->with('member.user')
            ->orderBy('check_in', 'desc')
            ->orderBy('id', 'desc')
            ->take(10)
            ->get();

        // Booking kelas hari ini
        $todayBookings = ClassBooking::whereDate('booking_date', $today)
            ->where('status', 'booked')
            ->with(['member.user', 'schedule.gymClass', 'schedule.trainer.user'])
            ->get();

        // Pembayaran terbaru
        $recentPayments = Payment::where('status', 'paid')
            ->with('member.user')
            ->latest('payment_date')
            ->take(5)
            ->get();

        // Peralatan perlu maintenance
        $maintenanceNeeded = Equipment::where(function($query) use ($today) {
                $query->where('next_maintenance', '<=', $today)
                      ->orWhere('condition', '!=', 'Baik');
            })
            ->take(5)
            ->get();

        // Data chart - Pendapatan 6 bulan terakhir
        $revenueChart = [];
        for ($i = 5; $i >= 0; $i--) {
            $month = $today->copy()->subMonths($i);
            $revenue = Payment::where('status', 'paid')
                ->whereMonth('payment_date', $month->month)
                ->whereYear('payment_date', $month->year)
                ->sum('total');
            $revenueChart[] = [
                'month'   => $month->translatedFormat('M Y'),
                'revenue' => (float) $revenue,
            ];
        }

        // Data chart - Absensi 7 hari terakhir
        $attendanceChart = [];
        for ($i = 6; $i >= 0; $i--) {
            $date = $today->copy()->subDays($i);
            $count = Attendance::whereDate('date', $date)->count();
            $attendanceChart[] = [
                'date'  => $date->translatedFormat('D, d M'),
                'count' => $count,
            ];
        }

        return view('dashboard', compact(
            'totalMembers', 'activeMembers', 'todayAttendances', 'monthlyRevenue',
            'newMembersThisMonth', 'expiringMemberships', 'todayAttendanceList',
            'todayBookings', 'recentPayments', 'maintenanceNeeded',
            'revenueChart', 'attendanceChart'
        ));
    }
}
