<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class GymClass extends Model
{
    protected $fillable = [
        'name', 'description', 'image', 'max_participants',
        'duration_minutes', 'difficulty', 'price_per_session', 'is_active',
    ];

    protected $casts = [
        'price_per_session' => 'decimal:2',
        'is_active'         => 'boolean',
    ];

    public function schedules()
    {
        return $this->hasMany(ClassSchedule::class);
    }
}
