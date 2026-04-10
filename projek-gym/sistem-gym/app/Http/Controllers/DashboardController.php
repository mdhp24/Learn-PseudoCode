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

/**
 * DashboardController
 *
 * Controller yang bertanggung jawab menampilkan halaman dashboard utama.
 * Mengumpulkan dan menyajikan berbagai data statistik gym secara ringkas,
 * mencakup: data member, kehadiran, pendapatan, booking kelas,
 * kondisi peralatan, serta data grafik untuk visualisasi tren.
 */
class DashboardController extends Controller
{

    /**
     * Menampilkan halaman dashboard utama.
     *
     * Mengambil dan mengolah berbagai data dari database untuk ditampilkan
     * sebagai ringkasan operasional gym hari ini maupun periode tertentu.
     *
     * @return \Illuminate\View\View  View 'dashboard' dengan data statistik lengkap
     */
    public function index()
    {
        // Tanggal hari ini sebagai acuan filter data
        $today = Carbon::today();

        // -----------------------------------------------
        // Statistik Utama (Kartu Ringkasan)
        // -----------------------------------------------
        // Menghitung total seluruh member yang terdaftar
        $totalMembers      = Member::count();

        // Menghitung member dengan status aktif saja
        $activeMembers     = Member::where('status', 'active')->count();

        // Menghitung jumlah kehadiran (absensi) pada hari ini
        $todayAttendances  = Attendance::whereDate('date', $today)->count();

        // Menghitung total pendapatan dari pembayaran lunas (paid) pada bulan berjalan
        $monthlyRevenue    = Payment::where('status', 'paid')
            ->whereBetween('payment_date', [
                $today->copy()->startOfMonth(),
                $today->copy()->endOfMonth()
            ])
            ->sum('total');

        // -----------------------------------------------
        // Member Baru Bulan Ini
        // -----------------------------------------------
        // Menghitung jumlah member yang bergabung pada bulan dan tahun berjalan
        $newMembersThisMonth = Member::whereMonth('joined_date', $today->month)
            ->whereYear('joined_date', $today->year)
            ->count();

        // -----------------------------------------------
        // Membership Hampir Kadaluarsa
        // -----------------------------------------------
        // Mengambil membership aktif yang akan berakhir dalam rentang 7 hari ke depan
        // Beserta relasi data member, user, dan paket membership-nya
        $expiringMemberships = MemberMembership::where('status', 'active')
            ->whereBetween('end_date', [$today, $today->copy()->addDays(7)])
            ->with(['member.user', 'package'])
            ->get();

        // -----------------------------------------------
        // Daftar Absensi Hari Ini
        // -----------------------------------------------
        // Mengambil 10 data kehadiran terbaru hari ini,
        // diurutkan berdasarkan waktu check-in terbaru
        $todayAttendanceList = Attendance::whereDate('date', $today)
            ->with('member.user')
            ->orderBy('check_in', 'desc')
            ->orderBy('id', 'desc')
            ->take(10)
            ->get();

        // -----------------------------------------------
        // Booking Kelas Hari Ini
        // -----------------------------------------------
        // Mengambil semua booking kelas pada hari ini dengan status 'booked'
        // Beserta relasi data member, jadwal kelas, nama kelas, dan trainer-nya
        $todayBookings = ClassBooking::whereDate('booking_date', $today)
            ->where('status', 'booked')
            ->with(['member.user', 'schedule.gymClass', 'schedule.trainer.user'])
            ->get();

        // -----------------------------------------------
        // Pembayaran Terbaru
        // -----------------------------------------------
        // Mengambil 5 transaksi pembayaran lunas (paid) yang paling baru
        // diurutkan berdasarkan tanggal pembayaran terkini
        $recentPayments = Payment::where('status', 'paid')
            ->with('member.user')
            ->latest('payment_date')
            ->take(5)
            ->get();

        // -----------------------------------------------
        // Peralatan yang Perlu Maintenance
        // -----------------------------------------------
        // Mengambil hingga 5 peralatan yang memenuhi salah satu kondisi berikut:
        // 1. Tanggal next_maintenance sudah lewat atau sama dengan hari ini
        // 2. Kondisi peralatan tidak dalam keadaan 'Baik'
        $maintenanceNeeded = Equipment::where(function ($query) use ($today) {
            $query->where('next_maintenance', '<=', $today)
                ->orWhere('condition', '!=', 'Baik');
        })
            ->take(5)
            ->get();

        // -----------------------------------------------
        // Data Chart: Pendapatan 6 Bulan Terakhir
        // -----------------------------------------------
        // Mengiterasi 6 bulan ke belakang dari bulan saat ini,
        // menghitung total pendapatan per bulan untuk ditampilkan pada grafik.
        // Format bulan menggunakan locale yang sudah di-set (misal: 'Jan 2025')
        $revenueChart = [];
        for ($i = 5; $i >= 0; $i--) {
            $month = $today->copy()->subMonths($i);
            $revenue = Payment::where('status', 'paid')
                ->whereMonth('payment_date', $month->month)
                ->whereYear('payment_date', $month->year)
                ->sum('total');
            $revenueChart[] = [
                'month'   => $month->translatedFormat('M Y'), // Contoh: "Jan 2025"
                'revenue' => (float) $revenue,  // Cast ke float untuk konsistensi tipe data
            ];
        }

        // -----------------------------------------------
        // Data Chart: Absensi 7 Hari Terakhir
        // -----------------------------------------------
        // Mengiterasi 7 hari ke belakang dari hari ini,
        // menghitung jumlah kehadiran per hari untuk ditampilkan pada grafik.
        // Format tanggal menggunakan locale (misal: 'Sen, 01 Jan')
        $attendanceChart = [];
        for ($i = 6; $i >= 0; $i--) {
            $date = $today->copy()->subDays($i);
            $count = Attendance::whereDate('date', $date)->count();
            $attendanceChart[] = [
                'date'  => $date->translatedFormat('D, d M'), // Contoh: "Sen, 06 Jan"
                'count' => $count,
            ];
        }
        
        // -----------------------------------------------
        // Kirim Semua Data ke View Dashboard
        // -----------------------------------------------
        return view('dashboard', compact(
            'totalMembers', // Total seluruh member
            'activeMembers', // Member dengan status aktif
            'todayAttendances', // Jumlah kehadiran hari ini
            'monthlyRevenue', // Total pendapatan bulan berjalan
            'newMembersThisMonth', // Member baru bulan ini
            'expiringMemberships', // Membership hampir kadaluarsa (7 hari)
            'todayAttendanceList', // Daftar absensi hari ini (maks. 10)
            'todayBookings', // Booking kelas aktif hari ini
            'recentPayments', // 5 pembayaran terbaru
            'maintenanceNeeded', // Peralatan perlu maintenance
            'revenueChart', // Data grafik pendapatan 6 bulan
            'attendanceChart' // Data grafik kehadiran 7 hari
        ));
    }
}
