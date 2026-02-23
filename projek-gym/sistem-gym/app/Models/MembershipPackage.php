<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class MembershipPackage extends Model
{
    protected $fillable = [
        'name', 'description', 'duration_days', 'price',
        'includes_trainer', 'includes_classes', 'includes_locker', 'is_active',
    ];

    protected $casts = [
        'price'            => 'decimal:2',
        'includes_trainer' => 'boolean',
        'includes_classes' => 'boolean',
        'includes_locker'  => 'boolean',
        'is_active'        => 'boolean',
    ];

    public function memberships()
    {
        return $this->hasMany(MemberMembership::class);
    }
}
