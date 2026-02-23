<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Payment extends Model
{
    protected $fillable = [
        'invoice_number', 'member_id', 'member_membership_id', 'payment_type',
        'amount', 'discount', 'total', 'payment_method', 'status',
        'payment_date', 'proof_of_payment', 'notes', 'processed_by',
    ];

    protected $casts = [
        'amount'       => 'decimal:2',
        'discount'     => 'decimal:2',
        'total'        => 'decimal:2',
        'payment_date' => 'date',
    ];

    public function member()
    {
        return $this->belongsTo(Member::class);
    }

    public function membership()
    {
        return $this->belongsTo(MemberMembership::class, 'member_membership_id');
    }

    public function processedBy()
    {
        return $this->belongsTo(User::class, 'processed_by');
    }
}
