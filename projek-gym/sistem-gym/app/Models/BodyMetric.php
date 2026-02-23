<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class BodyMetric extends Model
{
    protected $fillable = [
        'member_id', 'measured_at', 'weight', 'height', 'bmi',
        'body_fat_percentage', 'muscle_mass', 'chest', 'waist',
        'hips', 'arms', 'thighs', 'notes', 'measured_by',
    ];

    protected $casts = [
        'measured_at' => 'date',
    ];

    public function member()
    {
        return $this->belongsTo(Member::class);
    }

    public function measuredBy()
    {
        return $this->belongsTo(Trainer::class, 'measured_by');
    }
}
