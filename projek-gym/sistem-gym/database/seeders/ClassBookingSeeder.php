<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class ClassBookingSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $bookings = [
            // Booking untuk minggu ini
            ['member_id' => 1, 'class_schedule_id' => 1,  'booking_date' => '2026-02-16', 'status' => 'attended'],  // Budi - Yoga Senin
            ['member_id' => 2, 'class_schedule_id' => 1,  'booking_date' => '2026-02-16', 'status' => 'attended'],  // Dewi - Yoga Senin
            ['member_id' => 4, 'class_schedule_id' => 7,  'booking_date' => '2026-02-16', 'status' => 'attended'],  // Sari - Zumba Senin
            ['member_id' => 6, 'class_schedule_id' => 7,  'booking_date' => '2026-02-16', 'status' => 'attended'],  // Fitri - Zumba Senin
            ['member_id' => 5, 'class_schedule_id' => 12, 'booking_date' => '2026-02-16', 'status' => 'attended'],  // Reza - CrossFit Senin
            ['member_id' => 8, 'class_schedule_id' => 17, 'booking_date' => '2026-02-16', 'status' => 'attended'],  // Mega - Spinning Senin

            ['member_id' => 1, 'class_schedule_id' => 4,  'booking_date' => '2026-02-17', 'status' => 'attended'],  // Budi - HIIT Selasa
            ['member_id' => 10,'class_schedule_id' => 10, 'booking_date' => '2026-02-17', 'status' => 'attended'],  // Rina - Body Combat Selasa
            ['member_id' => 5, 'class_schedule_id' => 20, 'booking_date' => '2026-02-17', 'status' => 'attended'],  // Reza - Muay Thai Selasa

            ['member_id' => 2, 'class_schedule_id' => 2,  'booking_date' => '2026-02-18', 'status' => 'attended'],  // Dewi - Yoga Rabu
            ['member_id' => 4, 'class_schedule_id' => 8,  'booking_date' => '2026-02-18', 'status' => 'attended'],  // Sari - Zumba Rabu
            ['member_id' => 8, 'class_schedule_id' => 18, 'booking_date' => '2026-02-18', 'status' => 'no_show'],   // Mega - Spinning Rabu (tidak datang)

            // Booking untuk hari ini & besok
            ['member_id' => 1, 'class_schedule_id' => 5,  'booking_date' => '2026-02-19', 'status' => 'attended'],  // Budi - HIIT Kamis
            ['member_id' => 6, 'class_schedule_id' => 15, 'booking_date' => '2026-02-19', 'status' => 'attended'],  // Fitri - Pilates Kamis
            ['member_id' => 10,'class_schedule_id' => 11, 'booking_date' => '2026-02-19', 'status' => 'attended'],  // Rina - Body Combat Kamis

            ['member_id' => 2, 'class_schedule_id' => 3,  'booking_date' => '2026-02-20', 'status' => 'attended'],  // Dewi - Yoga Jumat
            ['member_id' => 5, 'class_schedule_id' => 14, 'booking_date' => '2026-02-20', 'status' => 'attended'],  // Reza - CrossFit Jumat
            ['member_id' => 8, 'class_schedule_id' => 19, 'booking_date' => '2026-02-20', 'status' => 'attended'],  // Mega - Spinning Jumat

            // Booking hari ini (Sabtu)
            ['member_id' => 1, 'class_schedule_id' => 6,  'booking_date' => '2026-02-21', 'status' => 'booked'],    // Budi - HIIT Sabtu
            ['member_id' => 4, 'class_schedule_id' => 9,  'booking_date' => '2026-02-21', 'status' => 'booked'],    // Sari - Zumba Sabtu
            ['member_id' => 6, 'class_schedule_id' => 9,  'booking_date' => '2026-02-21', 'status' => 'booked'],    // Fitri - Zumba Sabtu
            ['member_id' => 10,'class_schedule_id' => 6,  'booking_date' => '2026-02-21', 'status' => 'booked'],    // Rina - HIIT Sabtu
            ['member_id' => 5, 'class_schedule_id' => 21, 'booking_date' => '2026-02-21', 'status' => 'booked'],    // Reza - Muay Thai Sabtu

            // Beberapa yang dibatalkan
            ['member_id' => 8, 'class_schedule_id' => 6,  'booking_date' => '2026-02-21', 'status' => 'cancelled', 'notes' => 'Tidak bisa hadir, ada acara keluarga'],
        ];

        foreach ($bookings as $booking) {
            DB::table('class_bookings')->insert(array_merge([
                'notes'      => null,
                'created_at' => now(),
                'updated_at' => now(),
            ], $booking));
        }
    }
}
