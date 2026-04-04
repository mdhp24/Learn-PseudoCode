<?php


/**
 * ============================================================
 * Route Definitions - Gym Management System
 * ============================================================
 *
 * File ini mendefinisikan seluruh route aplikasi, mencakup:
 * - Halaman publik (landing page)
 * - Autentikasi (login & logout)
 * - Route terproteksi yang memerlukan autentikasi
 *
 * Semua route terproteksi dikelompokkan dalam middleware 'auth'
 * untuk memastikan hanya pengguna yang telah login yang dapat mengakses.
 * ============================================================
 */


use App\Http\Controllers\AuthController;
use App\Http\Controllers\BodyMetricController;
use App\Http\Controllers\ClassBookingController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\MemberController;
use App\Http\Controllers\AttendanceController;
use App\Http\Controllers\PaymentController;
use App\Http\Controllers\ClassController;
use App\Http\Controllers\EquipmentController;
use App\Http\Controllers\MembershipPackageController;
use App\Http\Controllers\TrainerController;
use Illuminate\Support\Facades\Route;

// ============================
// Landing Page (Public)
// ============================

/**
 * Halaman utama / landing page yang dapat diakses publik tanpa login.
 * Menampilkan informasi paket membership aktif, kelas gym aktif,
 * dan daftar trainer yang sedang aktif beserta data user-nya.
 *
 * @route   GET /
 * @name    home
 */
Route::get('/', function () {
    $packages = \App\Models\MembershipPackage::where('is_active', true)->get();
    $classes  = \App\Models\GymClass::where('is_active', true)->get();
    $trainers = \App\Models\Trainer::with('user')->where('status', 'active')->get();
    return view('welcome', compact('packages', 'classes', 'trainers'));
})->name('home');

// ============================
// Authentication
// ============================
/**
 * Route autentikasi untuk proses login dan logout pengguna.
 *
 * - GET  /login  → Menampilkan halaman form login
 * - POST /login  → Memproses kredensial dan melakukan autentikasi
 * - POST /logout → Mengakhiri sesi pengguna yang sedang login
 *  Semua route ini menggunakan AuthController untuk menangani logika autentikasi.
 */
Route::get('/login',  [AuthController::class, 'showLogin'])->name('login');
Route::post('/login', [AuthController::class, 'login']);
Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

// ============================
// Protected Routes (Auth Required)
// ============================
/**
 * Kelompok route yang hanya dapat diakses oleh pengguna
 * yang telah terautentikasi (middleware: auth).
 * Mencakup semua fitur manajemen gym.
 */
Route::middleware('auth')->group(function () {

        // ----------------------------
    // Dashboard
    // ----------------------------
    /**
     * Halaman dashboard utama setelah login.
     * Menampilkan ringkasan data dan statistik gym secara keseluruhan.
     *
     * @route   GET /dashboard
     * @name    dashboard
     */
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');

        // ----------------------------
    // Members
    // ----------------------------
    /**
     * Manajemen data anggota (member) gym.
     * Menyediakan operasi CRUD lengkap melalui resource route:
     *
     * - GET    /members          → Daftar semua member (index)
     * - GET    /members/create   → Form tambah member baru (create)
     * - POST   /members          → Simpan member baru (store)
     * - GET    /members/{id}     → Detail member (show)
     * - GET    /members/{id}/edit → Form edit member (edit)
     * - PUT    /members/{id}     → Update data member (update)
     * - DELETE /members/{id}     → Hapus member (destroy)
     *
     * @resource members
     */
    Route::resource('members', MemberController::class);

        // ----------------------------
    // Membership Packages
    // ----------------------------
    /**
     * Manajemen paket keanggotaan (membership packages).
     * Menyediakan operasi CRUD lengkap, serta route tambahan
     * untuk mengaktifkan / menonaktifkan paket secara toggle.
     *
     * Resource route standar:
     * - GET    /packages          → Daftar semua paket (index)
     * - GET    /packages/create   → Form tambah paket (create)
     * - POST   /packages          → Simpan paket baru (store)
     * - GET    /packages/{id}     → Detail paket (show)
     * - GET    /packages/{id}/edit → Form edit paket (edit)
     * - PUT    /packages/{id}     → Update paket (update)
     * - DELETE /packages/{id}     → Hapus paket (destroy)
     *
     * Route tambahan:
     * - PATCH  /packages/{id}/toggle-active → Toggle status aktif paket
     *
     * @resource packages
     * @name    packages.toggle-active
     */
    Route::resource('packages', MembershipPackageController::class);
    Route::patch('/packages/{package}/toggle-active', [MembershipPackageController::class, 'toggleActive'])
        ->name('packages.toggle-active');

        // ----------------------------
    // Attendance
    // ----------------------------
    /**
     * Manajemen absensi / kehadiran member gym.
     *
     * - GET   /attendances              → Daftar semua data kehadiran (index)
     * - POST  /attendances/check-in     → Proses check-in member yang datang
     * - PATCH /attendances/{id}/check-out → Proses check-out member yang pulang
     *
     * @name    attendances.index
     * @name    attendances.checkin
     * @name    attendances.checkout
     */
    Route::get('/attendances', [AttendanceController::class, 'index'])->name('attendances.index');
    Route::post('/attendances/check-in', [AttendanceController::class, 'checkIn'])->name('attendances.checkin');
    Route::patch('/attendances/{attendance}/check-out', [AttendanceController::class, 'checkOut'])->name('attendances.checkout');

        // ----------------------------
    // Payments
    // ----------------------------
    /**
     * Manajemen data pembayaran member.
     * Saat ini hanya menyediakan tampilan daftar riwayat pembayaran.
     *
     * - GET /payments → Daftar semua transaksi pembayaran (index)
     *
     * @name    payments.index
     */
    Route::get('/payments', [PaymentController::class, 'index'])->name('payments.index');

    // ----------------------------
    // Gym Classes
    // ----------------------------
    /**
     * Manajemen kelas gym (jenis kelas, deskripsi, dll).
     * Menyediakan operasi CRUD lengkap melalui resource route:
     *
     * - GET    /classes          → Daftar semua kelas (index)
     * - GET    /classes/create   → Form tambah kelas baru (create)
     * - POST   /classes          → Simpan kelas baru (store)
     * - GET    /classes/{id}     → Detail kelas (show)
     * - GET    /classes/{id}/edit → Form edit kelas (edit)
     * - PUT    /classes/{id}     → Update kelas (update)
     * - DELETE /classes/{id}     → Hapus kelas (destroy)
     *
     * @resource classes
     */
    Route::resource('classes', ClassController::class);

    // Class Schedules
    Route::get('/classes/schedules/index', [ClassController::class, 'schedules'])->name('classes.schedules.index');
    Route::get('/classes/schedules/create', [ClassController::class, 'createSchedule'])->name('classes.schedules.create');
    Route::post('/classes/schedules', [ClassController::class, 'storeSchedule'])->name('classes.schedules.store');
    Route::get('/classes/schedules/{schedule}', [ClassController::class, 'showSchedule'])->name('classes.schedules.show');
    Route::get('/classes/schedules/{schedule}/edit', [ClassController::class, 'editSchedule'])->name('classes.schedules.edit');
    Route::put('/classes/schedules/{schedule}', [ClassController::class, 'updateSchedule'])->name('classes.schedules.update');
    Route::delete('/classes/schedules/{schedule}', [ClassController::class, 'destroySchedule'])->name('classes.schedules.destroy');
    Route::patch('/classes/schedules/{schedule}/cancel', [ClassController::class, 'cancelSchedule'])->name('classes.schedules.cancel');
    Route::patch('/classes/schedules/{schedule}/complete', [ClassController::class, 'completeSchedule'])->name('classes.schedules.complete');

    // Class Bookings
    Route::resource('bookings', ClassBookingController::class)->except(['edit', 'update']);
    Route::get('/my-bookings', [ClassBookingController::class, 'myBookings'])->name('bookings.my');
    Route::patch('/bookings/{booking}/cancel', [ClassBookingController::class, 'cancel'])->name('bookings.cancel');
    Route::patch('/bookings/{booking}/attended', [ClassBookingController::class, 'markAttended'])->name('bookings.attended');
    Route::patch('/bookings/{booking}/no-show', [ClassBookingController::class, 'markNoShow'])->name('bookings.no-show');
    Route::get('/api/schedules/available', [ClassBookingController::class, 'availableSchedules'])->name('api.schedules.available');

    // Body Metrics
    Route::resource('body-metrics', BodyMetricController::class);
    Route::get('/members/{member}/body-metrics/history', [BodyMetricController::class, 'history'])->name('body-metrics.history');

    // Equipment
    Route::resource('equipment', EquipmentController::class);
    Route::get('/equipment-maintenance', [EquipmentController::class, 'maintenance'])->name('equipment.maintenance');
    Route::post('/equipment/{equipment}/record-maintenance', [EquipmentController::class, 'recordMaintenance'])
        ->name('equipment.record-maintenance');
    Route::patch('/equipment/{equipment}/update-status', [EquipmentController::class, 'updateStatus'])
        ->name('equipment.update-status');
    Route::get('/equipment-stats', [EquipmentController::class, 'stats'])->name('equipment.stats');

    // Trainers
    Route::resource('trainers', TrainerController::class);
    Route::get('/trainers/{trainer}/schedule', [TrainerController::class, 'schedule'])->name('trainers.schedule');
});
