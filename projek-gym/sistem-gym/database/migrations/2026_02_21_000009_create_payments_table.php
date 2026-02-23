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
        Schema::create('payments', function (Blueprint $table) {
            $table->id();
            $table->string('invoice_number')->unique();         // Nomor invoice (INV-20260221-001)
            $table->foreignId('member_id')->constrained()->onDelete('cascade');
            $table->foreignId('member_membership_id')->nullable()->constrained()->onDelete('set null');
            $table->enum('payment_type', ['membership', 'class', 'personal_training', 'other']);
            $table->decimal('amount', 12, 2);                   // Jumlah bayar
            $table->decimal('discount', 12, 2)->default(0);     // Diskon
            $table->decimal('total', 12, 2);                     // Total setelah diskon
            $table->enum('payment_method', ['cash', 'transfer', 'debit', 'credit_card', 'e_wallet']);
            $table->enum('status', ['pending', 'paid', 'failed', 'refunded'])->default('pending');
            $table->date('payment_date');
            $table->string('proof_of_payment')->nullable();     // Bukti pembayaran
            $table->text('notes')->nullable();
            $table->foreignId('processed_by')->nullable()->constrained('users')->onDelete('set null');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('payments');
    }
};
