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
        Schema::create('membership_packages', function (Blueprint $table) {
            $table->id();
            $table->string('name');                    // Harian, Bulanan, 3 Bulan, 6 Bulan, Tahunan
            $table->text('description')->nullable();
            $table->integer('duration_days');           // Durasi dalam hari
            $table->decimal('price', 12, 2);            // Harga paket
            $table->boolean('includes_trainer')->default(false);  // Termasuk personal trainer
            $table->boolean('includes_classes')->default(false);  // Termasuk akses kelas
            $table->boolean('includes_locker')->default(false);   // Termasuk locker
            $table->boolean('is_active')->default(true);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('membership_packages');
    }
};
