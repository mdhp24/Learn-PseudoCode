<?php

namespace App\Http\Controllers;

use App\Models\MembershipPackage;
use Illuminate\Http\Request;

class MembershipPackageController extends Controller
{
    public function index(Request $request)
    {
        $query = MembershipPackage::query();

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                  ->orWhere('description', 'like', "%{$search}%");
            });
        }

        if ($request->filled('is_active')) {
            $query->where('is_active', $request->is_active);
        }

        $packages = $query->orderBy('price', 'asc')->paginate(10)->withQueryString();
        return view('packages.index', compact('packages'));
    }

    public function create()
    {
        return view('packages.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name'           => 'required|string|max:255',
            'description'    => 'nullable|string',
            'duration_days'  => 'required|integer|min:1',
            'price'          => 'required|numeric|min:0',
            'class_credits'  => 'nullable|integer|min:0',
            'is_active'      => 'boolean',
        ]);

        $package = MembershipPackage::create([
            'name'          => $request->name,
            'description'   => $request->description,
            'duration_days' => $request->duration_days,
            'price'         => $request->price,
            'class_credits' => $request->class_credits ?? 0,
            'is_active'     => $request->has('is_active'),
        ]);

        return redirect()->route('packages.index')
            ->with('success', "Paket {$package->name} berhasil ditambahkan!");
    }

    public function show(MembershipPackage $package)
    {
        $package->loadCount([
            'memberMemberships',
            'memberMemberships as active_members_count' => function ($q) {
                $q->where('status', 'active');
            }
        ]);

        return view('packages.show', compact('package'));
    }

    public function edit(MembershipPackage $package)
    {
        return view('packages.edit', compact('package'));
    }

    public function update(Request $request, MembershipPackage $package)
    {
        $request->validate([
            'name'           => 'required|string|max:255',
            'description'    => 'nullable|string',
            'duration_days'  => 'required|integer|min:1',
            'price'          => 'required|numeric|min:0',
            'class_credits'  => 'nullable|integer|min:0',
            'is_active'      => 'boolean',
        ]);

        $package->update([
            'name'          => $request->name,
            'description'   => $request->description,
            'duration_days' => $request->duration_days,
            'price'         => $request->price,
            'class_credits' => $request->class_credits ?? 0,
            'is_active'     => $request->has('is_active'),
        ]);

        return redirect()->route('packages.show', $package)
            ->with('success', 'Paket berhasil diperbarui!');
    }

    public function destroy(MembershipPackage $package)
    {
        // Check if package has active memberships
        $activeMemberships = $package->memberMemberships()
            ->where('status', 'active')
            ->count();

        if ($activeMemberships > 0) {
            return back()->with('error', 
                'Tidak dapat menghapus paket yang masih memiliki member aktif!');
        }

        $name = $package->name;
        $package->delete();

        return redirect()->route('packages.index')
            ->with('success', "Paket {$name} berhasil dihapus.");
    }

    public function toggleActive(MembershipPackage $package)
    {
        $package->update(['is_active' => !$package->is_active]);
        
        $status = $package->is_active ? 'diaktifkan' : 'dinonaktifkan';
        return back()->with('success', "Paket {$package->name} berhasil {$status}!");
    }
}
