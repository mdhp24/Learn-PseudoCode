<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class BodyMetricSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $metrics = [
            // Budi Santoso (member 1) - progress 3 bulan
            [
                'member_id'            => 1,
                'measured_at'          => '2025-12-01',
                'weight'               => 85.50,
                'height'               => 175.00,
                'bmi'                  => 27.92,
                'body_fat_percentage'  => 25.00,
                'muscle_mass'          => 35.20,
                'chest'                => 102.00,
                'waist'                => 90.00,
                'hips'                 => 100.00,
                'arms'                 => 34.00,
                'thighs'               => 58.00,
                'notes'                => 'Pengukuran awal',
                'measured_by'          => 1,
            ],
            [
                'member_id'            => 1,
                'measured_at'          => '2026-01-01',
                'weight'               => 83.00,
                'height'               => 175.00,
                'bmi'                  => 27.10,
                'body_fat_percentage'  => 23.50,
                'muscle_mass'          => 36.00,
                'chest'                => 103.00,
                'waist'                => 87.00,
                'hips'                 => 99.00,
                'arms'                 => 35.00,
                'thighs'               => 57.50,
                'notes'                => 'Penurunan berat badan 2.5kg, peningkatan massa otot',
                'measured_by'          => 1,
            ],
            [
                'member_id'            => 1,
                'measured_at'          => '2026-02-01',
                'weight'               => 80.50,
                'height'               => 175.00,
                'bmi'                  => 26.29,
                'body_fat_percentage'  => 21.80,
                'muscle_mass'          => 37.00,
                'chest'                => 104.00,
                'waist'                => 84.00,
                'hips'                 => 98.00,
                'arms'                 => 36.00,
                'thighs'               => 57.00,
                'notes'                => 'Progress sangat baik! Lingkar pinggang turun signifikan',
                'measured_by'          => 1,
            ],

            // Dewi Lestari (member 2) - progress 2 bulan
            [
                'member_id'            => 2,
                'measured_at'          => '2026-01-15',
                'weight'               => 62.00,
                'height'               => 160.00,
                'bmi'                  => 24.22,
                'body_fat_percentage'  => 30.00,
                'muscle_mass'          => 24.00,
                'chest'                => 88.00,
                'waist'                => 75.00,
                'hips'                 => 95.00,
                'arms'                 => 27.00,
                'thighs'               => 55.00,
                'notes'                => 'Pengukuran awal',
                'measured_by'          => 2,
            ],
            [
                'member_id'            => 2,
                'measured_at'          => '2026-02-15',
                'weight'               => 60.00,
                'height'               => 160.00,
                'bmi'                  => 23.44,
                'body_fat_percentage'  => 28.00,
                'muscle_mass'          => 25.00,
                'chest'                => 87.00,
                'waist'                => 72.00,
                'hips'                 => 93.00,
                'arms'                 => 27.50,
                'thighs'               => 54.00,
                'notes'                => 'Penurunan lemak tubuh, peningkatan massa otot',
                'measured_by'          => 2,
            ],

            // Sari Wulandari (member 4) - progress 5 bulan (tahunan member)
            [
                'member_id'            => 4,
                'measured_at'          => '2025-09-01',
                'weight'               => 58.00,
                'height'               => 162.00,
                'bmi'                  => 22.10,
                'body_fat_percentage'  => 28.00,
                'muscle_mass'          => 22.50,
                'chest'                => 85.00,
                'waist'                => 70.00,
                'hips'                 => 92.00,
                'arms'                 => 25.00,
                'thighs'               => 52.00,
                'notes'                => 'Pengukuran awal saat pendaftaran tahunan',
                'measured_by'          => 2,
            ],
            [
                'member_id'            => 4,
                'measured_at'          => '2025-12-01',
                'weight'               => 55.50,
                'height'               => 162.00,
                'bmi'                  => 21.15,
                'body_fat_percentage'  => 24.00,
                'muscle_mass'          => 24.50,
                'chest'                => 84.00,
                'waist'                => 66.00,
                'hips'                 => 90.00,
                'arms'                 => 26.00,
                'thighs'               => 51.00,
                'notes'                => 'Progress 3 bulan: berat turun 2.5kg, otot naik 2kg',
                'measured_by'          => 1,
            ],
            [
                'member_id'            => 4,
                'measured_at'          => '2026-02-01',
                'weight'               => 54.00,
                'height'               => 162.00,
                'bmi'                  => 20.58,
                'body_fat_percentage'  => 22.00,
                'muscle_mass'          => 25.50,
                'chest'                => 83.00,
                'waist'                => 64.00,
                'hips'                 => 89.00,
                'arms'                 => 26.50,
                'thighs'               => 50.00,
                'notes'                => 'Target tercapai! Body fat di bawah 23%',
                'measured_by'          => 1,
            ],

            // Reza Firmansyah (member 5)
            [
                'member_id'            => 5,
                'measured_at'          => '2025-12-01',
                'weight'               => 78.00,
                'height'               => 178.00,
                'bmi'                  => 24.62,
                'body_fat_percentage'  => 18.00,
                'muscle_mass'          => 38.00,
                'chest'                => 100.00,
                'waist'                => 80.00,
                'hips'                 => 96.00,
                'arms'                 => 35.00,
                'thighs'               => 58.00,
                'notes'                => 'Pengukuran awal - target bulking',
                'measured_by'          => 5,
            ],
            [
                'member_id'            => 5,
                'measured_at'          => '2026-02-01',
                'weight'               => 82.00,
                'height'               => 178.00,
                'bmi'                  => 25.88,
                'body_fat_percentage'  => 17.00,
                'muscle_mass'          => 41.00,
                'chest'                => 104.00,
                'waist'                => 81.00,
                'hips'                 => 97.00,
                'arms'                 => 37.50,
                'thighs'               => 60.00,
                'notes'                => 'Clean bulk berhasil! +3kg massa otot, lemak stabil',
                'measured_by'          => 5,
            ],
        ];

        foreach ($metrics as $metric) {
            DB::table('body_metrics')->insert(array_merge($metric, [
                'created_at' => now(),
                'updated_at' => now(),
            ]));
        }
    }
}
