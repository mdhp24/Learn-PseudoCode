<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class MemberMembershipSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $memberships = [
            // Budi - Bulanan VIP (paket 5, 30 hari)
            [
                'member_id'             => 1,
                'membership_package_id' => 5,
                'start_date'            => '2026-02-01',
                'end_date'              => '2026-03-03',
                'status'                => 'active',
            ],
            // Dewi - 3 Bulan (paket 6, 90 hari)
            [
                'member_id'             => 2,
                'membership_package_id' => 6,
                'start_date'            => '2026-01-15',
                'end_date'              => '2026-04-15',
                'status'                => 'active',
            ],
            // Andi - Bulanan Basic (paket 3, 30 hari) - expired
            [
                'member_id'             => 3,
                'membership_package_id' => 3,
                'start_date'            => '2026-01-01',
                'end_date'              => '2026-01-31',
                'status'                => 'expired',
            ],
            // Andi - Bulanan Premium (paket 4, 30 hari) - aktif sekarang
            [
                'member_id'             => 3,
                'membership_package_id' => 4,
                'start_date'            => '2026-02-01',
                'end_date'              => '2026-03-03',
                'status'                => 'active',
            ],
            // Sari - Tahunan (paket 8, 365 hari)
            [
                'member_id'             => 4,
                'membership_package_id' => 8,
                'start_date'            => '2025-09-01',
                'end_date'              => '2026-09-01',
                'status'                => 'active',
            ],
            // Reza - 6 Bulan (paket 7, 180 hari)
            [
                'member_id'             => 5,
                'membership_package_id' => 7,
                'start_date'            => '2025-12-01',
                'end_date'              => '2026-05-30',
                'status'                => 'active',
            ],
            // Fitri - Bulanan Premium (paket 4)
            [
                'member_id'             => 6,
                'membership_package_id' => 4,
                'start_date'            => '2026-02-05',
                'end_date'              => '2026-03-07',
                'status'                => 'active',
            ],
            // Doni - Bulanan Basic (paket 3) - frozen
            [
                'member_id'             => 7,
                'membership_package_id' => 3,
                'start_date'            => '2026-02-01',
                'end_date'              => '2026-03-03',
                'status'                => 'frozen',
                'frozen_at'             => '2026-02-15',
                'frozen_days'           => 6,
            ],
            // Mega - 3 Bulan (paket 6)
            [
                'member_id'             => 8,
                'membership_package_id' => 6,
                'start_date'            => '2026-01-01',
                'end_date'              => '2026-04-01',
                'status'                => 'active',
            ],
            // Fajar - Mingguan (paket 2) - expired
            [
                'member_id'             => 9,
                'membership_package_id' => 2,
                'start_date'            => '2026-02-10',
                'end_date'              => '2026-02-17',
                'status'                => 'expired',
            ],
            // Rina - Bulanan VIP (paket 5)
            [
                'member_id'             => 10,
                'membership_package_id' => 5,
                'start_date'            => '2026-02-01',
                'end_date'              => '2026-03-03',
                'status'                => 'active',
            ],
        ];

        foreach ($memberships as $membership) {
            DB::table('member_memberships')->insert(array_merge([
                'frozen_at'   => null,
                'frozen_days' => 0,
                'notes'       => null,
                'created_at'  => now(),
                'updated_at'  => now(),
            ], $membership));
        }
    }
}
