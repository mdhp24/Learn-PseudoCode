<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Member extends Model
{
    protected $fillable = [
        'user_id', 'member_code', 'phone', 'gender', 'date_of_birth',
        'address', 'emergency_contact', 'emergency_phone', 'photo',
        'blood_type', 'health_notes', 'status', 'joined_date',
    ];

    protected $casts = [
        'date_of_birth' => 'date',
        'joined_date'   => 'date',
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function memberships()
    {
        return $this->hasMany(MemberMembership::class);
    }

    public function activeMembership()
    {
        return $this->hasOne(MemberMembership::class)->where('status', 'active')->latest();
    }

    public function attendances()
    {
        return $this->hasMany(Attendance::class);
    }

    public function payments()
    {
        return $this->hasMany(Payment::class);
    }

    public function bodyMetrics()
    {
        return $this->hasMany(BodyMetric::class);
    }

    public function classBookings()
    {
        return $this->hasMany(ClassBooking::class);
    }
}
