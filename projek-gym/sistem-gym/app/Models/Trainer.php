<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Trainer extends Model
{
    protected $fillable = [
        'user_id', 'trainer_code', 'phone', 'specialization', 'bio',
        'certification', 'experience_years', 'photo', 'hourly_rate', 'status',
    ];

    protected $casts = [
        'hourly_rate' => 'decimal:2',
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function classSchedules()
    {
        return $this->hasMany(ClassSchedule::class);
    }
}
