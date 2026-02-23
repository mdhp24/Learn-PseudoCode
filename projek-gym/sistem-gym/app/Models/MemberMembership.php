<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class MemberMembership extends Model
{
    protected $fillable = [
        'member_id', 'membership_package_id', 'start_date', 'end_date',
        'status', 'frozen_at', 'frozen_days', 'notes',
    ];

    protected $casts = [
        'start_date' => 'date',
        'end_date'   => 'date',
        'frozen_at'  => 'date',
    ];

    public function member()
    {
        return $this->belongsTo(Member::class);
    }

    public function package()
    {
        return $this->belongsTo(MembershipPackage::class, 'membership_package_id');
    }

    public function payments()
    {
        return $this->hasMany(Payment::class);
    }
}
