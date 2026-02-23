<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;

class MemberSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        // Buat user member terlebih dahulu lalu insert data member
        $members = [
            [
                'user' => ['name' => 'Budi Santoso',    'email' => 'budi@gmail.com',    'role' => 'member'],
                'phone' => '081234567890', 'gender' => 'Laki-laki', 'date_of_birth' => '1995-03-15',
                'address' => 'Jl. Merdeka No. 10, Jakarta Selatan',
                'emergency_contact' => 'Siti Santoso', 'emergency_phone' => '081234567891',
                'blood_type' => 'A', 'health_notes' => null,
            ],
            [
                'user' => ['name' => 'Dewi Lestari',    'email' => 'dewi@gmail.com',    'role' => 'member'],
                'phone' => '081345678901', 'gender' => 'Perempuan', 'date_of_birth' => '1998-07-22',
                'address' => 'Jl. Sudirman No. 25, Jakarta Pusat',
                'emergency_contact' => 'Andi Lestari', 'emergency_phone' => '081345678902',
                'blood_type' => 'B', 'health_notes' => null,
            ],
            [
                'user' => ['name' => 'Andi Pratama',     'email' => 'andi@gmail.com',     'role' => 'member'],
                'phone' => '082123456789', 'gender' => 'Laki-laki', 'date_of_birth' => '1992-11-08',
                'address' => 'Jl. Gatot Subroto No. 5, Bandung',
                'emergency_contact' => 'Rina Pratama', 'emergency_phone' => '082123456780',
                'blood_type' => 'O', 'health_notes' => 'Asma ringan',
            ],
            [
                'user' => ['name' => 'Sari Wulandari',  'email' => 'sari@gmail.com',    'role' => 'member'],
                'phone' => '083456789012', 'gender' => 'Perempuan', 'date_of_birth' => '2000-01-30',
                'address' => 'Jl. Diponegoro No. 18, Surabaya',
                'emergency_contact' => 'Joko Wulandari', 'emergency_phone' => '083456789013',
                'blood_type' => 'AB', 'health_notes' => null,
            ],
            [
                'user' => ['name' => 'Reza Firmansyah', 'email' => 'reza@gmail.com',    'role' => 'member'],
                'phone' => '085678901234', 'gender' => 'Laki-laki', 'date_of_birth' => '1997-05-12',
                'address' => 'Jl. Ahmad Yani No. 33, Yogyakarta',
                'emergency_contact' => 'Maya Firmansyah', 'emergency_phone' => '085678901235',
                'blood_type' => 'B', 'health_notes' => null,
            ],
            [
                'user' => ['name' => 'Fitri Handayani', 'email' => 'fitri@gmail.com',   'role' => 'member'],
                'phone' => '087890123456', 'gender' => 'Perempuan', 'date_of_birth' => '1999-09-05',
                'address' => 'Jl. Pemuda No. 7, Semarang',
                'emergency_contact' => 'Bambang Handayani', 'emergency_phone' => '087890123457',
                'blood_type' => 'A', 'health_notes' => null,
            ],
            [
                'user' => ['name' => 'Doni Saputra',    'email' => 'doni@gmail.com',    'role' => 'member'],
                'phone' => '081567890123', 'gender' => 'Laki-laki', 'date_of_birth' => '1994-12-20',
                'address' => 'Jl. Veteran No. 42, Malang',
                'emergency_contact' => 'Lina Saputra', 'emergency_phone' => '081567890124',
                'blood_type' => 'O', 'health_notes' => 'Cedera lutut (sudah pulih)',
            ],
            [
                'user' => ['name' => 'Mega Putri',      'email' => 'mega@gmail.com',    'role' => 'member'],
                'phone' => '082345678901', 'gender' => 'Perempuan', 'date_of_birth' => '1996-06-18',
                'address' => 'Jl. Asia Afrika No. 15, Bandung',
                'emergency_contact' => 'Eko Putri', 'emergency_phone' => '082345678902',
                'blood_type' => 'A', 'health_notes' => null,
            ],
            [
                'user' => ['name' => 'Fajar Nugroho',   'email' => 'fajar@gmail.com',   'role' => 'member'],
                'phone' => '083567890123', 'gender' => 'Laki-laki', 'date_of_birth' => '1993-04-25',
                'address' => 'Jl. Pahlawan No. 20, Medan',
                'emergency_contact' => 'Dian Nugroho', 'emergency_phone' => '083567890124',
                'blood_type' => 'B', 'health_notes' => null,
            ],
            [
                'user' => ['name' => 'Rina Oktavia',    'email' => 'rina@gmail.com',    'role' => 'member'],
                'phone' => '084678901234', 'gender' => 'Perempuan', 'date_of_birth' => '2001-10-11',
                'address' => 'Jl. Thamrin No. 8, Jakarta Pusat',
                'emergency_contact' => 'Agus Oktavia', 'emergency_phone' => '084678901235',
                'blood_type' => 'AB', 'health_notes' => null,
            ],
        ];

        $joinDates = [
            '2025-06-01', '2025-07-15', '2025-08-10', '2025-09-01', '2025-09-20',
            '2025-10-05', '2025-11-12', '2025-12-01', '2026-01-10', '2026-02-01',
        ];

        foreach ($members as $index => $data) {
            $user = User::create([
                'name'     => $data['user']['name'],
                'email'    => $data['user']['email'],
                'password' => Hash::make('password123'),
                'role'     => $data['user']['role'],
            ]);

            $memberCode = 'GYM-' . str_pad($index + 1, 4, '0', STR_PAD_LEFT);

            DB::table('members')->insert([
                'user_id'           => $user->id,
                'member_code'       => $memberCode,
                'phone'             => $data['phone'],
                'gender'            => $data['gender'],
                'date_of_birth'     => $data['date_of_birth'],
                'address'           => $data['address'],
                'emergency_contact' => $data['emergency_contact'],
                'emergency_phone'   => $data['emergency_phone'],
                'blood_type'        => $data['blood_type'],
                'health_notes'      => $data['health_notes'],
                'status'            => 'active',
                'joined_date'       => $joinDates[$index],
                'created_at'        => now(),
                'updated_at'        => now(),
            ]);
        }
    }
}
