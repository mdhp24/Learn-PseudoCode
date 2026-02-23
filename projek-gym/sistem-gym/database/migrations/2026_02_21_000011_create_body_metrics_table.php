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
        Schema::create('body_metrics', function (Blueprint $table) {
            $table->id();
            $table->foreignId('member_id')->constrained()->onDelete('cascade');
            $table->date('measured_at');                         // Tanggal pengukuran
            $table->decimal('weight', 5, 2)->nullable();         // Berat badan (kg)
            $table->decimal('height', 5, 2)->nullable();         // Tinggi badan (cm)
            $table->decimal('bmi', 5, 2)->nullable();            // Body Mass Index
            $table->decimal('body_fat_percentage', 5, 2)->nullable(); // Persentase lemak tubuh
            $table->decimal('muscle_mass', 5, 2)->nullable();    // Massa otot (kg)
            $table->decimal('chest', 5, 2)->nullable();          // Lingkar dada (cm)
            $table->decimal('waist', 5, 2)->nullable();          // Lingkar pinggang (cm)
            $table->decimal('hips', 5, 2)->nullable();           // Lingkar pinggul (cm)
            $table->decimal('arms', 5, 2)->nullable();           // Lingkar lengan (cm)
            $table->decimal('thighs', 5, 2)->nullable();         // Lingkar paha (cm)
            $table->text('notes')->nullable();
            $table->foreignId('measured_by')->nullable()->constrained('trainers')->onDelete('set null');
            $table->timestamps();

            $table->index(['member_id', 'measured_at']);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('body_metrics');
    }
};
