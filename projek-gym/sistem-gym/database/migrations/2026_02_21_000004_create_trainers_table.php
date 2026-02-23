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
        Schema::create('trainers', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
            $table->string('trainer_code')->unique();          // Kode trainer (TRN-001)
            $table->string('phone', 20)->nullable();
            $table->string('specialization');                   // Spesialisasi (Cardio, Strength, Yoga, dll)
            $table->text('bio')->nullable();                    // Biografi singkat
            $table->string('certification')->nullable();        // Sertifikasi
            $table->integer('experience_years')->default(0);    // Pengalaman dalam tahun
            $table->string('photo')->nullable();
            $table->decimal('hourly_rate', 10, 2)->nullable();  // Tarif per jam
            $table->enum('status', ['active', 'inactive', 'on_leave'])->default('active');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('trainers');
    }
};
