<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    use WithoutModelEvents;

    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // ============================
        // Buat akun Admin & Staff
        // ============================
        User::create([
            'name'     => 'Admin Gym',
            'email'    => 'admin@gym.com',
            'password' => Hash::make('admin123'),
            'role'     => 'admin',
        ]);

        User::create([
            'name'     => 'Staff Resepsionis',
            'email'    => 'staff@gym.com',
            'password' => Hash::make('staff123'),
            'role'     => 'staff',
        ]);

        // ============================
        // Jalankan semua seeder
        // ============================
        $this->call([
            MembershipPackageSeeder::class,
            TrainerSeeder::class,
            MemberSeeder::class,
            MemberMembershipSeeder::class,
            GymClassSeeder::class,
            ClassScheduleSeeder::class,
            ClassBookingSeeder::class,
            AttendanceSeeder::class,
            PaymentSeeder::class,
            EquipmentSeeder::class,
            BodyMetricSeeder::class,
        ]);
    }
}
