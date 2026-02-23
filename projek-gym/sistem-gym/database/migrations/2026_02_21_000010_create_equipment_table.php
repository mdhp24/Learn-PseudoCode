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
        Schema::create('equipment', function (Blueprint $table) {
            $table->id();
            $table->string('name');                             // Nama alat (Treadmill, Dumbbell, dll)
            $table->string('code')->unique();                   // Kode alat (EQ-001)
            $table->text('description')->nullable();
            $table->string('image')->nullable();
            $table->enum('category', ['Cardio', 'Strength', 'Flexibility', 'Functional', 'Lainnya']);
            $table->string('brand')->nullable();
            $table->integer('quantity')->default(1);
            $table->enum('condition', ['Baik', 'Rusak Ringan', 'Rusak Berat', 'Maintenance'])->default('Baik');
            $table->date('purchase_date')->nullable();
            $table->date('last_maintenance')->nullable();
            $table->date('next_maintenance')->nullable();
            $table->text('notes')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('equipment');
    }
};
