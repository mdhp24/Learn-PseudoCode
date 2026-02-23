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
        Schema::create('members', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
            $table->string('member_code')->unique();          // Kode member unik (GYM-0001)
            $table->string('phone', 20)->nullable();
            $table->enum('gender', ['Laki-laki', 'Perempuan']);
            $table->date('date_of_birth')->nullable();
            $table->text('address')->nullable();
            $table->string('emergency_contact')->nullable();   // Kontak darurat
            $table->string('emergency_phone', 20)->nullable();
            $table->string('photo')->nullable();               // Foto member
            $table->enum('blood_type', ['A', 'B', 'AB', 'O'])->nullable();
            $table->text('health_notes')->nullable();          // Catatan kesehatan
            $table->enum('status', ['active', 'inactive', 'expired', 'suspended'])->default('active');
            $table->date('joined_date');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('members');
    }
};
