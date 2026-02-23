<?php

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
Route::get('/', function () {
    $packages = \App\Models\MembershipPackage::where('is_active', true)->get();
    $classes  = \App\Models\GymClass::where('is_active', true)->get();
    $trainers = \App\Models\Trainer::with('user')->where('status', 'active')->get();
    return view('welcome', compact('packages', 'classes', 'trainers'));
})->name('home');

// ============================
// Authentication
// ============================
Route::get('/login',  [AuthController::class, 'showLogin'])->name('login');
Route::post('/login', [AuthController::class, 'login']);
Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

// ============================
// Protected Routes (Auth Required)
// ============================
Route::middleware('auth')->group(function () {

    // Dashboard
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');

    // Members
    Route::resource('members', MemberController::class);

    // Membership Packages
    Route::resource('packages', MembershipPackageController::class);
    Route::patch('/packages/{package}/toggle-active', [MembershipPackageController::class, 'toggleActive'])
        ->name('packages.toggle-active');

    // Attendance
    Route::get('/attendances', [AttendanceController::class, 'index'])->name('attendances.index');
    Route::post('/attendances/check-in', [AttendanceController::class, 'checkIn'])->name('attendances.checkin');
    Route::patch('/attendances/{attendance}/check-out', [AttendanceController::class, 'checkOut'])->name('attendances.checkout');

    // Payments
    Route::get('/payments', [PaymentController::class, 'index'])->name('payments.index');

    // Gym Classes
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

