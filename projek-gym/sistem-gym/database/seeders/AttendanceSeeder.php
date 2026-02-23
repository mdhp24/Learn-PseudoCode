<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Carbon\Carbon;

class AttendanceSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $attendances = [];

        // Buat data absensi untuk 2 minggu terakhir (beberapa member)
        $activeMembers = [1, 2, 4, 5, 6, 8, 10]; // member aktif

        for ($day = 14; $day >= 0; $day--) {
            $date = Carbon::now()->subDays($day);

            // Skip hari Minggu (beberapa member tetap datang)
            if ($date->dayOfWeek === Carbon::SUNDAY && $day % 3 !== 0) {
                continue;
            }

            // Randomize member yang datang hari itu (3-5 member per hari)
            $todayMembers = array_slice($activeMembers, $day % 3, rand(3, 5));

            foreach ($todayMembers as $memberId) {
                $checkInHour  = rand(6, 19);
                $checkInMin   = rand(0, 59);
                $duration     = rand(45, 150);
                $checkIn      = sprintf('%02d:%02d:00', $checkInHour, $checkInMin);

                $checkOutTime = Carbon::createFromFormat('H:i:s', $checkIn)->addMinutes($duration);
                $checkOut     = $checkOutTime->format('H:i:s');

                // Pastikan check_out tidak lewat tengah malam
                if ($checkOutTime->hour >= 22) {
                    $checkOut = '22:00:00';
                    $duration = Carbon::createFromFormat('H:i:s', $checkIn)
                        ->diffInMinutes(Carbon::createFromFormat('H:i:s', $checkOut));
                }

                $attendances[] = [
                    'member_id'        => $memberId,
                    'date'             => $date->format('Y-m-d'),
                    'check_in'         => $checkIn,
                    'check_out'        => $checkOut,
                    'duration_minutes' => $duration,
                    'notes'            => null,
                    'created_at'       => now(),
                    'updated_at'       => now(),
                ];
            }
        }

        // Insert secara batch
        foreach (array_chunk($attendances, 50) as $chunk) {
            DB::table('attendances')->insert($chunk);
        }
    }
}
