<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class ClassScheduleSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $schedules = [
            // Yoga Flow - Coach Linda (trainer_id = 2)
            ['gym_class_id' => 1, 'trainer_id' => 2, 'day_of_week' => 'Senin',  'start_time' => '07:00', 'end_time' => '08:00', 'room' => 'Studio A'],
            ['gym_class_id' => 1, 'trainer_id' => 2, 'day_of_week' => 'Rabu',   'start_time' => '07:00', 'end_time' => '08:00', 'room' => 'Studio A'],
            ['gym_class_id' => 1, 'trainer_id' => 2, 'day_of_week' => 'Jumat',  'start_time' => '07:00', 'end_time' => '08:00', 'room' => 'Studio A'],

            // HIIT Burn - Coach Dimas (trainer_id = 3)
            ['gym_class_id' => 2, 'trainer_id' => 3, 'day_of_week' => 'Selasa', 'start_time' => '17:00', 'end_time' => '17:45', 'room' => 'Studio B'],
            ['gym_class_id' => 2, 'trainer_id' => 3, 'day_of_week' => 'Kamis',  'start_time' => '17:00', 'end_time' => '17:45', 'room' => 'Studio B'],
            ['gym_class_id' => 2, 'trainer_id' => 3, 'day_of_week' => 'Sabtu',  'start_time' => '09:00', 'end_time' => '09:45', 'room' => 'Studio B'],

            // Zumba Party - Coach Nia (trainer_id = 4)
            ['gym_class_id' => 3, 'trainer_id' => 4, 'day_of_week' => 'Senin',  'start_time' => '18:00', 'end_time' => '19:00', 'room' => 'Studio A'],
            ['gym_class_id' => 3, 'trainer_id' => 4, 'day_of_week' => 'Rabu',   'start_time' => '18:00', 'end_time' => '19:00', 'room' => 'Studio A'],
            ['gym_class_id' => 3, 'trainer_id' => 4, 'day_of_week' => 'Sabtu',  'start_time' => '10:00', 'end_time' => '11:00', 'room' => 'Studio A'],

            // Body Combat - Coach Arif (trainer_id = 1)
            ['gym_class_id' => 4, 'trainer_id' => 1, 'day_of_week' => 'Selasa', 'start_time' => '18:00', 'end_time' => '18:55', 'room' => 'Studio B'],
            ['gym_class_id' => 4, 'trainer_id' => 1, 'day_of_week' => 'Kamis',  'start_time' => '18:00', 'end_time' => '18:55', 'room' => 'Studio B'],

            // CrossFit WOD - Coach Bagus (trainer_id = 5)
            ['gym_class_id' => 5, 'trainer_id' => 5, 'day_of_week' => 'Senin',  'start_time' => '16:00', 'end_time' => '16:50', 'room' => 'Area CrossFit'],
            ['gym_class_id' => 5, 'trainer_id' => 5, 'day_of_week' => 'Rabu',   'start_time' => '16:00', 'end_time' => '16:50', 'room' => 'Area CrossFit'],
            ['gym_class_id' => 5, 'trainer_id' => 5, 'day_of_week' => 'Jumat',  'start_time' => '16:00', 'end_time' => '16:50', 'room' => 'Area CrossFit'],

            // Pilates Core - Coach Linda (trainer_id = 2)
            ['gym_class_id' => 6, 'trainer_id' => 2, 'day_of_week' => 'Selasa', 'start_time' => '08:00', 'end_time' => '08:50', 'room' => 'Studio A'],
            ['gym_class_id' => 6, 'trainer_id' => 2, 'day_of_week' => 'Kamis',  'start_time' => '08:00', 'end_time' => '08:50', 'room' => 'Studio A'],

            // Spinning Fury - Coach Dimas (trainer_id = 3)
            ['gym_class_id' => 7, 'trainer_id' => 3, 'day_of_week' => 'Senin',  'start_time' => '19:00', 'end_time' => '19:45', 'room' => 'Spinning Room'],
            ['gym_class_id' => 7, 'trainer_id' => 3, 'day_of_week' => 'Rabu',   'start_time' => '19:00', 'end_time' => '19:45', 'room' => 'Spinning Room'],
            ['gym_class_id' => 7, 'trainer_id' => 3, 'day_of_week' => 'Jumat',  'start_time' => '19:00', 'end_time' => '19:45', 'room' => 'Spinning Room'],

            // Muay Thai Basics - Coach Bagus (trainer_id = 5)
            ['gym_class_id' => 8, 'trainer_id' => 5, 'day_of_week' => 'Selasa', 'start_time' => '19:00', 'end_time' => '20:00', 'room' => 'Area Combat'],
            ['gym_class_id' => 8, 'trainer_id' => 5, 'day_of_week' => 'Sabtu',  'start_time' => '11:00', 'end_time' => '12:00', 'room' => 'Area Combat'],
        ];

        foreach ($schedules as $schedule) {
            DB::table('class_schedules')->insert(array_merge($schedule, [
                'is_active'  => true,
                'created_at' => now(),
                'updated_at' => now(),
            ]));
        }
    }
}
