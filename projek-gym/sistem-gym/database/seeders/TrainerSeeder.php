<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;

class TrainerSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $trainers = [
            [
                'user'           => ['name' => 'Coach Arif Rahman',  'email' => 'arif.trainer@gym.com'],
                'phone'          => '081111222333',
                'specialization' => 'Strength & Conditioning',
                'bio'            => 'Berpengalaman lebih dari 8 tahun dalam melatih atlet profesional dan pecinta fitness. Spesialisasi dalam program pembentukan otot dan kekuatan.',
                'certification'  => 'NSCA-CPT, ACE Certified',
                'experience_years' => 8,
                'hourly_rate'    => 150000,
            ],
            [
                'user'           => ['name' => 'Coach Linda Kusuma', 'email' => 'linda.trainer@gym.com'],
                'phone'          => '081222333444',
                'specialization' => 'Yoga & Pilates',
                'bio'            => 'Instruktur yoga bersertifikat internasional dengan fokus pada keseimbangan tubuh dan pikiran. Telah mengajar lebih dari 500 kelas.',
                'certification'  => 'RYT-500, Pilates Method Alliance',
                'experience_years' => 6,
                'hourly_rate'    => 120000,
            ],
            [
                'user'           => ['name' => 'Coach Dimas Prayoga', 'email' => 'dimas.trainer@gym.com'],
                'phone'          => '081333444555',
                'specialization' => 'Cardio & HIIT',
                'bio'            => 'Spesialis program kardio dan HIIT untuk pembakar lemak maksimal. Mantan atlet lari maraton nasional.',
                'certification'  => 'ACE Group Fitness, HIIT Specialist',
                'experience_years' => 5,
                'hourly_rate'    => 130000,
            ],
            [
                'user'           => ['name' => 'Coach Nia Ramadhani', 'email' => 'nia.trainer@gym.com'],
                'phone'          => '081444555666',
                'specialization' => 'Zumba & Dance Fitness',
                'bio'            => 'Energik dan menyenangkan! Membuat olahraga terasa seperti pesta dansa. Berpengalaman dalam kelas group fitness.',
                'certification'  => 'Zumba Licensed Instructor, AFAA',
                'experience_years' => 4,
                'hourly_rate'    => 110000,
            ],
            [
                'user'           => ['name' => 'Coach Bagus Wicaksono', 'email' => 'bagus.trainer@gym.com'],
                'phone'          => '081555666777',
                'specialization' => 'CrossFit & Functional Training',
                'bio'            => 'CrossFit Level 2 Trainer dengan passion dalam functional fitness. Membantu member mencapai versi terbaik diri mereka.',
                'certification'  => 'CrossFit Level 2, NASM-CPT',
                'experience_years' => 7,
                'hourly_rate'    => 140000,
            ],
        ];

        foreach ($trainers as $index => $data) {
            $user = User::create([
                'name'     => $data['user']['name'],
                'email'    => $data['user']['email'],
                'password' => Hash::make('trainer123'),
                'role'     => 'trainer',
            ]);

            $trainerCode = 'TRN-' . str_pad($index + 1, 3, '0', STR_PAD_LEFT);

            DB::table('trainers')->insert([
                'user_id'          => $user->id,
                'trainer_code'     => $trainerCode,
                'phone'            => $data['phone'],
                'specialization'   => $data['specialization'],
                'bio'              => $data['bio'],
                'certification'    => $data['certification'],
                'experience_years' => $data['experience_years'],
                'hourly_rate'      => $data['hourly_rate'],
                'status'           => 'active',
                'created_at'       => now(),
                'updated_at'       => now(),
            ]);
        }
    }
}
