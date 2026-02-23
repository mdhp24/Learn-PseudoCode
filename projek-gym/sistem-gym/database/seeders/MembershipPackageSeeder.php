<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class MembershipPackageSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $packages = [
            [
                'name'              => 'Harian',
                'description'       => 'Paket harian untuk pengunjung yang ingin mencoba fasilitas gym.',
                'duration_days'     => 1,
                'price'             => 50000,
                'includes_trainer'  => false,
                'includes_classes'  => false,
                'includes_locker'   => false,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
            [
                'name'              => 'Mingguan',
                'description'       => 'Paket mingguan cocok untuk pemula yang ingin mulai rutin berolahraga.',
                'duration_days'     => 7,
                'price'             => 150000,
                'includes_trainer'  => false,
                'includes_classes'  => false,
                'includes_locker'   => true,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
            [
                'name'              => 'Bulanan Basic',
                'description'       => 'Paket bulanan basic dengan akses penuh ke area gym.',
                'duration_days'     => 30,
                'price'             => 350000,
                'includes_trainer'  => false,
                'includes_classes'  => false,
                'includes_locker'   => true,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
            [
                'name'              => 'Bulanan Premium',
                'description'       => 'Paket bulanan premium dengan akses gym, kelas, dan locker.',
                'duration_days'     => 30,
                'price'             => 550000,
                'includes_trainer'  => false,
                'includes_classes'  => true,
                'includes_locker'   => true,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
            [
                'name'              => 'Bulanan VIP',
                'description'       => 'Paket bulanan VIP dengan personal trainer, akses kelas, dan locker.',
                'duration_days'     => 30,
                'price'             => 900000,
                'includes_trainer'  => true,
                'includes_classes'  => true,
                'includes_locker'   => true,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
            [
                'name'              => '3 Bulan',
                'description'       => 'Paket 3 bulan hemat dengan semua fasilitas termasuk personal trainer.',
                'duration_days'     => 90,
                'price'             => 2200000,
                'includes_trainer'  => true,
                'includes_classes'  => true,
                'includes_locker'   => true,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
            [
                'name'              => '6 Bulan',
                'description'       => 'Paket 6 bulan super hemat dengan semua fasilitas premium.',
                'duration_days'     => 180,
                'price'             => 4000000,
                'includes_trainer'  => true,
                'includes_classes'  => true,
                'includes_locker'   => true,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
            [
                'name'              => 'Tahunan',
                'description'       => 'Paket tahunan terbaik! Hemat hingga 40% dengan akses unlimited semua fasilitas.',
                'duration_days'     => 365,
                'price'             => 6500000,
                'includes_trainer'  => true,
                'includes_classes'  => true,
                'includes_locker'   => true,
                'is_active'         => true,
                'created_at'        => now(),
                'updated_at'        => now(),
            ],
        ];

        DB::table('membership_packages')->insert($packages);
    }
}
