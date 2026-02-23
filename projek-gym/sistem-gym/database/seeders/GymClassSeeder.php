<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class GymClassSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $classes = [
            [
                'name'               => 'Yoga Flow',
                'description'        => 'Kelas yoga yang memadukan gerakan mengalir dengan teknik pernapasan untuk meningkatkan fleksibilitas dan ketenangan pikiran.',
                'max_participants'   => 20,
                'duration_minutes'   => 60,
                'difficulty'         => 'Pemula',
                'price_per_session'  => 0,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
            [
                'name'               => 'HIIT Burn',
                'description'        => 'High Intensity Interval Training untuk membakar kalori maksimal dalam waktu singkat. Siap keringetan!',
                'max_participants'   => 15,
                'duration_minutes'   => 45,
                'difficulty'         => 'Menengah',
                'price_per_session'  => 0,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
            [
                'name'               => 'Zumba Party',
                'description'        => 'Gabungan gerakan dansa Latin dengan musik energik. Olahraga yang menyenangkan untuk semua level!',
                'max_participants'   => 25,
                'duration_minutes'   => 60,
                'difficulty'         => 'Pemula',
                'price_per_session'  => 0,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
            [
                'name'               => 'Body Combat',
                'description'        => 'Kelas martial arts yang menggabungkan gerakan karate, taekwondo, dan boxing. Tingkatkan kekuatan dan koordinasi!',
                'max_participants'   => 20,
                'duration_minutes'   => 55,
                'difficulty'         => 'Menengah',
                'price_per_session'  => 25000,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
            [
                'name'               => 'CrossFit WOD',
                'description'        => 'Workout of the Day ala CrossFit. Program latihan intensif yang menggabungkan angkat beban, gimnastik, dan kardio.',
                'max_participants'   => 12,
                'duration_minutes'   => 50,
                'difficulty'         => 'Lanjutan',
                'price_per_session'  => 35000,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
            [
                'name'               => 'Pilates Core',
                'description'        => 'Fokus pada penguatan otot inti (core), postur tubuh, dan keseimbangan. Cocok untuk pemulihan dan pencegahan cedera.',
                'max_participants'   => 15,
                'duration_minutes'   => 50,
                'difficulty'         => 'Pemula',
                'price_per_session'  => 0,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
            [
                'name'               => 'Spinning Fury',
                'description'        => 'Kelas bersepeda statis dengan musik energik dan variasi intensitas. Bakar hingga 600 kalori per sesi!',
                'max_participants'   => 18,
                'duration_minutes'   => 45,
                'difficulty'         => 'Menengah',
                'price_per_session'  => 30000,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
            [
                'name'               => 'Muay Thai Basics',
                'description'        => 'Pelajari teknik dasar Muay Thai untuk meningkatkan kekuatan, stamina, dan kepercayaan diri.',
                'max_participants'   => 16,
                'duration_minutes'   => 60,
                'difficulty'         => 'Menengah',
                'price_per_session'  => 40000,
                'is_active'          => true,
                'created_at'         => now(),
                'updated_at'         => now(),
            ],
        ];

        DB::table('gym_classes')->insert($classes);
    }
}
