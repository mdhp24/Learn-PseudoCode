<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class PaymentSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $payments = [
            [
                'invoice_number'       => 'INV-20260201-001',
                'member_id'            => 1,
                'member_membership_id' => 1,
                'payment_type'         => 'membership',
                'amount'               => 900000,
                'discount'             => 0,
                'total'                => 900000,
                'payment_method'       => 'transfer',
                'status'               => 'paid',
                'payment_date'         => '2026-02-01',
                'notes'                => 'Pembayaran paket Bulanan VIP',
            ],
            [
                'invoice_number'       => 'INV-20260115-001',
                'member_id'            => 2,
                'member_membership_id' => 2,
                'payment_type'         => 'membership',
                'amount'               => 2200000,
                'discount'             => 200000,
                'total'                => 2000000,
                'payment_method'       => 'transfer',
                'status'               => 'paid',
                'payment_date'         => '2026-01-15',
                'notes'                => 'Pembayaran paket 3 Bulan (diskon promo)',
            ],
            [
                'invoice_number'       => 'INV-20260201-002',
                'member_id'            => 3,
                'member_membership_id' => 4,
                'payment_type'         => 'membership',
                'amount'               => 550000,
                'discount'             => 0,
                'total'                => 550000,
                'payment_method'       => 'cash',
                'status'               => 'paid',
                'payment_date'         => '2026-02-01',
                'notes'                => 'Upgrade dari Basic ke Premium',
            ],
            [
                'invoice_number'       => 'INV-20250901-001',
                'member_id'            => 4,
                'member_membership_id' => 5,
                'payment_type'         => 'membership',
                'amount'               => 6500000,
                'discount'             => 500000,
                'total'                => 6000000,
                'payment_method'       => 'credit_card',
                'status'               => 'paid',
                'payment_date'         => '2025-09-01',
                'notes'                => 'Pembayaran paket Tahunan (diskon early bird)',
            ],
            [
                'invoice_number'       => 'INV-20251201-001',
                'member_id'            => 5,
                'member_membership_id' => 6,
                'payment_type'         => 'membership',
                'amount'               => 4000000,
                'discount'             => 0,
                'total'                => 4000000,
                'payment_method'       => 'e_wallet',
                'status'               => 'paid',
                'payment_date'         => '2025-12-01',
                'notes'                => 'Pembayaran paket 6 Bulan',
            ],
            [
                'invoice_number'       => 'INV-20260205-001',
                'member_id'            => 6,
                'member_membership_id' => 7,
                'payment_type'         => 'membership',
                'amount'               => 550000,
                'discount'             => 50000,
                'total'                => 500000,
                'payment_method'       => 'debit',
                'status'               => 'paid',
                'payment_date'         => '2026-02-05',
                'notes'                => 'Pembayaran Bulanan Premium (diskon referral)',
            ],
            [
                'invoice_number'       => 'INV-20260201-003',
                'member_id'            => 7,
                'member_membership_id' => 8,
                'payment_type'         => 'membership',
                'amount'               => 350000,
                'discount'             => 0,
                'total'                => 350000,
                'payment_method'       => 'cash',
                'status'               => 'paid',
                'payment_date'         => '2026-02-01',
                'notes'                => 'Pembayaran Bulanan Basic',
            ],
            [
                'invoice_number'       => 'INV-20260101-001',
                'member_id'            => 8,
                'member_membership_id' => 9,
                'payment_type'         => 'membership',
                'amount'               => 2200000,
                'discount'             => 0,
                'total'                => 2200000,
                'payment_method'       => 'transfer',
                'status'               => 'paid',
                'payment_date'         => '2026-01-01',
                'notes'                => 'Pembayaran paket 3 Bulan',
            ],
            [
                'invoice_number'       => 'INV-20260210-001',
                'member_id'            => 9,
                'member_membership_id' => 10,
                'payment_type'         => 'membership',
                'amount'               => 150000,
                'discount'             => 0,
                'total'                => 150000,
                'payment_method'       => 'cash',
                'status'               => 'paid',
                'payment_date'         => '2026-02-10',
                'notes'                => 'Pembayaran paket Mingguan',
            ],
            [
                'invoice_number'       => 'INV-20260201-004',
                'member_id'            => 10,
                'member_membership_id' => 11,
                'payment_type'         => 'membership',
                'amount'               => 900000,
                'discount'             => 100000,
                'total'                => 800000,
                'payment_method'       => 'e_wallet',
                'status'               => 'paid',
                'payment_date'         => '2026-02-01',
                'notes'                => 'Pembayaran Bulanan VIP (diskon member baru)',
            ],
            // Beberapa pembayaran kelas tambahan
            [
                'invoice_number'       => 'INV-20260215-001',
                'member_id'            => 1,
                'member_membership_id' => null,
                'payment_type'         => 'class',
                'amount'               => 40000,
                'discount'             => 0,
                'total'                => 40000,
                'payment_method'       => 'cash',
                'status'               => 'paid',
                'payment_date'         => '2026-02-15',
                'notes'                => 'Kelas Muay Thai Basics',
            ],
            [
                'invoice_number'       => 'INV-20260218-001',
                'member_id'            => 2,
                'member_membership_id' => null,
                'payment_type'         => 'personal_training',
                'amount'               => 300000,
                'discount'             => 0,
                'total'                => 300000,
                'payment_method'       => 'transfer',
                'status'               => 'paid',
                'payment_date'         => '2026-02-18',
                'notes'                => 'Personal training 2 sesi dengan Coach Arif',
            ],
        ];

        foreach ($payments as $payment) {
            DB::table('payments')->insert(array_merge($payment, [
                'proof_of_payment' => null,
                'processed_by'     => 1,  // Admin
                'created_at'       => now(),
                'updated_at'       => now(),
            ]));
        }
    }
}
