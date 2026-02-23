<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Equipment extends Model
{
    protected $table = 'equipment';

    protected $fillable = [
        'name', 'code', 'description', 'image', 'category', 'brand',
        'quantity', 'condition', 'purchase_date', 'last_maintenance',
        'next_maintenance', 'notes',
    ];

    protected $casts = [
        'purchase_date'    => 'date',
        'last_maintenance' => 'date',
        'next_maintenance' => 'date',
    ];
}
