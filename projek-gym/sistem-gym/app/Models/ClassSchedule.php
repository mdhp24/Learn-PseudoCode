<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ClassSchedule extends Model
{
    protected $fillable = [
        'gym_class_id', 'trainer_id', 'day_of_week',
        'start_time', 'end_time', 'room', 'is_active',
    ];

    protected $casts = [
        'is_active' => 'boolean',
    ];

    public function gymClass()
    {
        return $this->belongsTo(GymClass::class);
    }

    public function trainer()
    {
        return $this->belongsTo(Trainer::class);
    }

    public function bookings()
    {
        return $this->hasMany(ClassBooking::class);
    }
}
