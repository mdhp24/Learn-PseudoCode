<?php

namespace App\Http\Controllers;

use App\Models\Equipment;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class EquipmentController extends Controller
{
    public function index(Request $request)
    {
        $query = Equipment::query();

        if ($request->filled('search')) {
            $query->where(function ($q) use ($request) {
                $q->where('name', 'like', "%{$request->search}%")
                  ->orWhere('code', 'like', "%{$request->search}%")
                  ->orWhere('brand', 'like', "%{$request->search}%");
            });
        }

        if ($request->filled('category')) {
            $query->where('category', $request->category);
        }

        if ($request->filled('condition')) {
            $query->where('condition', $request->condition);
        }

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $equipment = $query->orderBy('name')->paginate(12)->withQueryString();

        // Get categories for filter
        $categories = Equipment::select('category')
            ->distinct()
            ->whereNotNull('category')
            ->pluck('category');

        return view('equipment.index', compact('equipment', 'categories'));
    }

    public function create()
    {
        return view('equipment.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name'              => 'required|string|max:255',
            'code'              => 'required|string|max:50|unique:equipment,code',
            'category'          => 'required|string|max:100',
            'brand'             => 'nullable|string|max:100',
            'model'             => 'nullable|string|max:100',
            'purchase_date'     => 'nullable|date',
            'purchase_price'    => 'nullable|numeric|min:0',
            'condition'         => 'required|in:excellent,good,fair,poor,broken',
            'status'            => 'required|in:available,in_use,maintenance,out_of_service',
            'location'          => 'nullable|string|max:100',
            'warranty_until'    => 'nullable|date',
            'last_maintenance'  => 'nullable|date',
            'next_maintenance'  => 'nullable|date|after_or_equal:last_maintenance',
            'notes'             => 'nullable|string',
        ]);

        $equipment = Equipment::create($request->all());

        return redirect()->route('equipment.show', $equipment)
            ->with('success', "Equipment {$equipment->name} berhasil ditambahkan!");
    }

    public function show(Equipment $equipment)
    {
        // Calculate days until next maintenance
        $maintenanceDue = null;
        if ($equipment->next_maintenance) {
            $nextMaintenance = Carbon::parse($equipment->next_maintenance);
            $maintenanceDue = Carbon::today()->diffInDays($nextMaintenance, false);
        }

        // Check warranty status
        $warrantyStatus = null;
        if ($equipment->warranty_until) {
            $warrantyExpiry = Carbon::parse($equipment->warranty_until);
            $warrantyStatus = [
                'is_active' => $warrantyExpiry->isFuture(),
                'days_remaining' => max(0, Carbon::today()->diffInDays($warrantyExpiry, false)),
            ];
        }

        return view('equipment.show', compact('equipment', 'maintenanceDue', 'warrantyStatus'));
    }

    public function edit(Equipment $equipment)
    {
        return view('equipment.edit', compact('equipment'));
    }

    public function update(Request $request, Equipment $equipment)
    {
        $request->validate([
            'name'              => 'required|string|max:255',
            'code'              => 'required|string|max:50|unique:equipment,code,' . $equipment->id,
            'category'          => 'required|string|max:100',
            'brand'             => 'nullable|string|max:100',
            'model'             => 'nullable|string|max:100',
            'purchase_date'     => 'nullable|date',
            'purchase_price'    => 'nullable|numeric|min:0',
            'condition'         => 'required|in:excellent,good,fair,poor,broken',
            'status'            => 'required|in:available,in_use,maintenance,out_of_service',
            'location'          => 'nullable|string|max:100',
            'warranty_until'    => 'nullable|date',
            'last_maintenance'  => 'nullable|date',
            'next_maintenance'  => 'nullable|date|after_or_equal:last_maintenance',
            'notes'             => 'nullable|string',
        ]);

        $equipment->update($request->all());

        return redirect()->route('equipment.show', $equipment)
            ->with('success', 'Data equipment berhasil diperbarui!');
    }

    public function destroy(Equipment $equipment)
    {
        $name = $equipment->name;
        $equipment->delete();

        return redirect()->route('equipment.index')
            ->with('success', "Equipment {$name} berhasil dihapus.");
    }

    public function maintenance(Request $request)
    {
        $query = Equipment::query();

        // Show equipment that needs maintenance
        if (!$request->filled('show_all')) {
            $query->where(function ($q) {
                $q->where('next_maintenance', '<=', Carbon::today()->addDays(30))
                  ->orWhere('status', 'maintenance')
                  ->orWhere('condition', 'poor')
                  ->orWhere('condition', 'broken');
            });
        }

        if ($request->filled('category')) {
            $query->where('category', $request->category);
        }

        $equipment = $query->orderBy('next_maintenance', 'asc')
            ->orderBy('condition', 'desc')
            ->paginate(15)
            ->withQueryString();

        // Categorize equipment by maintenance urgency
        $equipment->getCollection()->transform(function ($item) {
            if ($item->next_maintenance) {
                $daysUntil = Carbon::today()->diffInDays(Carbon::parse($item->next_maintenance), false);
                
                if ($daysUntil < 0) {
                    $item->maintenance_urgency = 'overdue';
                } elseif ($daysUntil <= 7) {
                    $item->maintenance_urgency = 'urgent';
                } elseif ($daysUntil <= 30) {
                    $item->maintenance_urgency = 'soon';
                } else {
                    $item->maintenance_urgency = 'scheduled';
                }
            } else {
                $item->maintenance_urgency = 'not_scheduled';
            }
            
            return $item;
        });

        $categories = Equipment::select('category')
            ->distinct()
            ->whereNotNull('category')
            ->pluck('category');

        return view('equipment.maintenance', compact('equipment', 'categories'));
    }

    public function recordMaintenance(Request $request, Equipment $equipment)
    {
        $request->validate([
            'maintenance_date'      => 'required|date',
            'next_maintenance_date' => 'nullable|date|after:maintenance_date',
            'condition'             => 'required|in:excellent,good,fair,poor,broken',
            'status'                => 'required|in:available,in_use,maintenance,out_of_service',
            'maintenance_notes'     => 'nullable|string',
        ]);

        $equipment->update([
            'last_maintenance'  => $request->maintenance_date,
            'next_maintenance'  => $request->next_maintenance_date,
            'condition'         => $request->condition,
            'status'            => $request->status,
            'notes'             => $equipment->notes ? $equipment->notes . "\n\n[" . Carbon::now()->format('Y-m-d H:i') . "] " . $request->maintenance_notes : $request->maintenance_notes,
        ]);

        return redirect()->route('equipment.show', $equipment)
            ->with('success', 'Data maintenance berhasil dicatat!');
    }

    public function updateStatus(Request $request, Equipment $equipment)
    {
        $request->validate([
            'status' => 'required|in:available,in_use,maintenance,out_of_service',
        ]);

        $equipment->update(['status' => $request->status]);

        $statusLabels = [
            'available' => 'Tersedia',
            'in_use' => 'Sedang Digunakan',
            'maintenance' => 'Dalam Maintenance',
            'out_of_service' => 'Tidak Beroperasi',
        ];

        return back()->with('success', 
            "Status equipment diubah menjadi: {$statusLabels[$request->status]}");
    }

    public function stats()
    {
        $stats = [
            'total' => Equipment::count(),
            'available' => Equipment::where('status', 'available')->count(),
            'in_use' => Equipment::where('status', 'in_use')->count(),
            'maintenance' => Equipment::where('status', 'maintenance')->count(),
            'out_of_service' => Equipment::where('status', 'out_of_service')->count(),
            'needs_maintenance' => Equipment::where('next_maintenance', '<=', Carbon::today()->addDays(30))->count(),
            'overdue_maintenance' => Equipment::where('next_maintenance', '<', Carbon::today())->count(),
            'by_condition' => Equipment::select('condition', DB::raw('count(*) as count'))
                ->groupBy('condition')
                ->pluck('count', 'condition'),
            'by_category' => Equipment::select('category', DB::raw('count(*) as count'))
                ->groupBy('category')
                ->orderBy('count', 'desc')
                ->pluck('count', 'category'),
        ];

        return view('equipment.stats', compact('stats'));
    }
}

