<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('gym_classes', function (Blueprint $table) {
            $table->id();
            $table->string('name');                            // Nama kelas (Yoga, Zumba, Boxing, dll)
            $table->text('description')->nullable();
            $table->string('image')->nullable();               // Gambar kelas
            $table->integer('max_participants');                 // Maksimal peserta
            $table->integer('duration_minutes');                 // Durasi dalam menit
            $table->enum('difficulty', ['Pemula', 'Menengah', 'Lanjutan'])->default('Pemula');
            $table->decimal('price_per_session', 10, 2)->default(0); // Harga per sesi (0 = gratis untuk member)
            $table->boolean('is_active')->default(true);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('gym_classes');
    }
};
