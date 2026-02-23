<?php

namespace App\Http\Controllers;

use App\Models\BodyMetric;
use App\Models\Member;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class BodyMetricController extends Controller
{
    public function index(Request $request)
    {
        $query = BodyMetric::with('member.user');

        if ($request->filled('member_id')) {
            $query->where('member_id', $request->member_id);
        }

        if ($request->filled('search')) {
            $search = $request->search;
            $query->whereHas('member.user', function ($q) use ($search) {
                $q->where('name', 'like', "%{$search}%");
            })->orWhereHas('member', function ($q) use ($search) {
                $q->where('member_code', 'like', "%{$search}%");
            });
        }

        $metrics = $query->latest('measured_at')->paginate(15)->withQueryString();
        $members = Member::with('user')->where('status', 'active')->get();

        return view('body-metrics.index', compact('metrics', 'members'));
    }

    public function create(Request $request)
    {
        $members = Member::with('user')->where('status', 'active')->get();
        $selectedMember = $request->filled('member_id') 
            ? Member::with('user')->find($request->member_id) 
            : null;

        return view('body-metrics.create', compact('members', 'selectedMember'));
    }

    public function store(Request $request)
    {
        $request->validate([
            'member_id'     => 'required|exists:members,id',
            'weight'        => 'required|numeric|min:0|max:500',
            'height'        => 'nullable|numeric|min:0|max:300',
            'body_fat'      => 'nullable|numeric|min:0|max:100',
            'muscle_mass'   => 'nullable|numeric|min:0|max:200',
            'bmi'           => 'nullable|numeric|min:0|max:100',
            'chest'         => 'nullable|numeric|min:0|max:300',
            'waist'         => 'nullable|numeric|min:0|max:300',
            'hips'          => 'nullable|numeric|min:0|max:300',
            'arms'          => 'nullable|numeric|min:0|max:100',
            'thighs'        => 'nullable|numeric|min:0|max:150',
            'notes'         => 'nullable|string',
            'measured_at'   => 'nullable|date',
        ]);

        // Auto-calculate BMI if height and weight provided
        $bmi = $request->bmi;
        if (!$bmi && $request->weight && $request->height) {
            $heightInMeters = $request->height / 100;
            $bmi = round($request->weight / ($heightInMeters * $heightInMeters), 2);
        }

        $metric = BodyMetric::create([
            'member_id'    => $request->member_id,
            'weight'       => $request->weight,
            'height'       => $request->height,
            'body_fat'     => $request->body_fat,
            'muscle_mass'  => $request->muscle_mass,
            'bmi'          => $bmi,
            'chest'        => $request->chest,
            'waist'        => $request->waist,
            'hips'         => $request->hips,
            'arms'         => $request->arms,
            'thighs'       => $request->thighs,
            'notes'        => $request->notes,
            'measured_at'  => $request->measured_at ?? Carbon::now(),
            'measured_by'  => Auth::id(),
        ]);

        $member = $metric->member;
        return redirect()->route('body-metrics.show', $metric)
            ->with('success', "Data body metric untuk {$member->user->name} berhasil ditambahkan!");
    }

    public function show(BodyMetric $bodyMetric)
    {
        $bodyMetric->load('member.user', 'measuredBy');
        
        // Get previous measurement for comparison
        $previous = BodyMetric::where('member_id', $bodyMetric->member_id)
            ->where('measured_at', '<', $bodyMetric->measured_at)
            ->latest('measured_at')
            ->first();

        // Calculate changes
        $changes = null;
        if ($previous) {
            $changes = [
                'weight'      => $bodyMetric->weight - $previous->weight,
                'body_fat'    => $bodyMetric->body_fat ? ($bodyMetric->body_fat - ($previous->body_fat ?? 0)) : null,
                'muscle_mass' => $bodyMetric->muscle_mass ? ($bodyMetric->muscle_mass - ($previous->muscle_mass ?? 0)) : null,
                'bmi'         => $bodyMetric->bmi ? ($bodyMetric->bmi - ($previous->bmi ?? 0)) : null,
            ];
        }

        // Get member's history
        $history = BodyMetric::where('member_id', $bodyMetric->member_id)
            ->latest('measured_at')
            ->take(10)
            ->get();

        return view('body-metrics.show', compact('bodyMetric', 'previous', 'changes', 'history'));
    }

    public function edit(BodyMetric $bodyMetric)
    {
        $bodyMetric->load('member.user');
        return view('body-metrics.edit', compact('bodyMetric'));
    }

    public function update(Request $request, BodyMetric $bodyMetric)
    {
        $request->validate([
            'weight'        => 'required|numeric|min:0|max:500',
            'height'        => 'nullable|numeric|min:0|max:300',
            'body_fat'      => 'nullable|numeric|min:0|max:100',
            'muscle_mass'   => 'nullable|numeric|min:0|max:200',
            'bmi'           => 'nullable|numeric|min:0|max:100',
            'chest'         => 'nullable|numeric|min:0|max:300',
            'waist'         => 'nullable|numeric|min:0|max:300',
            'hips'          => 'nullable|numeric|min:0|max:300',
            'arms'          => 'nullable|numeric|min:0|max:100',
            'thighs'        => 'nullable|numeric|min:0|max:150',
            'notes'         => 'nullable|string',
            'measured_at'   => 'nullable|date',
        ]);

        // Auto-calculate BMI if height and weight provided
        $bmi = $request->bmi;
        if (!$bmi && $request->weight && $request->height) {
            $heightInMeters = $request->height / 100;
            $bmi = round($request->weight / ($heightInMeters * $heightInMeters), 2);
        }

        $bodyMetric->update([
            'weight'       => $request->weight,
            'height'       => $request->height,
            'body_fat'     => $request->body_fat,
            'muscle_mass'  => $request->muscle_mass,
            'bmi'          => $bmi,
            'chest'        => $request->chest,
            'waist'        => $request->waist,
            'hips'         => $request->hips,
            'arms'         => $request->arms,
            'thighs'       => $request->thighs,
            'notes'        => $request->notes,
            'measured_at'  => $request->measured_at ?? $bodyMetric->measured_at,
        ]);

        return redirect()->route('body-metrics.show', $bodyMetric)
            ->with('success', 'Data body metric berhasil diperbarui!');
    }

    public function destroy(BodyMetric $bodyMetric)
    {
        $memberName = $bodyMetric->member->user->name;
        $bodyMetric->delete();

        return redirect()->route('body-metrics.index')
            ->with('success', "Data body metric untuk {$memberName} berhasil dihapus.");
    }

    public function history(Member $member)
    {
        $metrics = BodyMetric::where('member_id', $member->id)
            ->latest('measured_at')
            ->get();

        return view('body-metrics.history', compact('member', 'metrics'));
    }
}
