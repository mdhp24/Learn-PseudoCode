<?php

namespace App\Http\Controllers;

use App\Models\Member;
use App\Models\MembershipPackage;
use App\Models\MemberMembership;
use App\Models\Payment;
use App\Models\User;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;

class MemberController extends Controller
{
    public function index(Request $request)
    {
        $query = Member::with(['user', 'activeMembership.package']);

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('member_code', 'like', "%{$search}%")
                  ->orWhere('phone', 'like', "%{$search}%")
                  ->orWhereHas('user', function ($q2) use ($search) {
                      $q2->where('name', 'like', "%{$search}%")
                         ->orWhere('email', 'like', "%{$search}%");
                  });
            });
        }

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $members = $query->latest()->paginate(10)->withQueryString();
        return view('members.index', compact('members'));
    }

    public function create()
    {
        $packages = MembershipPackage::where('is_active', true)->get();
        return view('members.create', compact('packages'));
    }

    public function store(Request $request)
    {
        $request->validate([
            'name'               => 'required|string|max:255',
            'email'              => 'required|email|unique:users,email',
            'phone'              => 'required|string|max:20',
            'gender'             => 'required|in:Laki-laki,Perempuan',
            'date_of_birth'      => 'nullable|date',
            'address'            => 'nullable|string',
            'emergency_contact'  => 'nullable|string',
            'emergency_phone'    => 'nullable|string|max:20',
            'blood_type'         => 'nullable|in:A,B,AB,O',
            'health_notes'       => 'nullable|string',
            'membership_package_id' => 'required|exists:membership_packages,id',
            'payment_method'     => 'required|in:cash,transfer,debit,credit_card,e_wallet',
        ]);

        DB::beginTransaction();
        try {
            // Buat user
            $user = User::create([
                'name'     => $request->name,
                'email'    => $request->email,
                'password' => Hash::make('password123'),
                'role'     => 'member',
            ]);

            // Generate member code
            $lastMember = Member::orderBy('id', 'desc')->first();
            $nextNumber = $lastMember ? ((int) substr($lastMember->member_code, 4)) + 1 : 1;
            $memberCode = 'GYM-' . str_pad($nextNumber, 4, '0', STR_PAD_LEFT);

            // Buat member
            $member = Member::create([
                'user_id'           => $user->id,
                'member_code'       => $memberCode,
                'phone'             => $request->phone,
                'gender'            => $request->gender,
                'date_of_birth'     => $request->date_of_birth,
                'address'           => $request->address,
                'emergency_contact' => $request->emergency_contact,
                'emergency_phone'   => $request->emergency_phone,
                'blood_type'        => $request->blood_type,
                'health_notes'      => $request->health_notes,
                'status'            => 'active',
                'joined_date'       => Carbon::today(),
            ]);

            // Buat membership
            $package = MembershipPackage::findOrFail($request->membership_package_id);
            $startDate = Carbon::today();
            $endDate   = $startDate->copy()->addDays($package->duration_days);

            $membership = MemberMembership::create([
                'member_id'             => $member->id,
                'membership_package_id' => $package->id,
                'start_date'            => $startDate,
                'end_date'              => $endDate,
                'status'                => 'active',
            ]);

            // Buat payment
            $invoiceNumber = 'INV-' . Carbon::today()->format('Ymd') . '-' .
                             str_pad(Payment::whereDate('created_at', Carbon::today())->count() + 1, 3, '0', STR_PAD_LEFT);

            Payment::create([
                'invoice_number'       => $invoiceNumber,
                'member_id'            => $member->id,
                'member_membership_id' => $membership->id,
                'payment_type'         => 'membership',
                'amount'               => $package->price,
                'discount'             => 0,
                'total'                => $package->price,
                'payment_method'       => $request->payment_method,
                'status'               => 'paid',
                'payment_date'         => Carbon::today(),
                'notes'                => 'Pendaftaran member baru - ' . $package->name,
                'processed_by'         => Auth::id(),
            ]);

            DB::commit();
            return redirect()->route('members.index')->with('success', "Member {$user->name} berhasil didaftarkan dengan kode {$memberCode}!");

        } catch (\Exception $e) {
            DB::rollBack();
            return back()->withInput()->with('error', 'Gagal mendaftarkan member: ' . $e->getMessage());
        }
    }

    public function show(Member $member)
    {
        $member->load([
            'user',
            'memberships.package',
            'attendances' => fn($q) => $q->latest('date')->take(20),
            'payments' => fn($q) => $q->latest('payment_date'),
            'bodyMetrics' => fn($q) => $q->latest('measured_at'),
            'classBookings' => fn($q) => $q->with('schedule.gymClass')->latest('booking_date')->take(10),
        ]);

        return view('members.show', compact('member'));
    }

    public function edit(Member $member)
    {
        $member->load('user');
        return view('members.edit', compact('member'));
    }

    public function update(Request $request, Member $member)
    {
        $request->validate([
            'name'              => 'required|string|max:255',
            'email'             => 'required|email|unique:users,email,' . $member->user_id,
            'phone'             => 'required|string|max:20',
            'gender'            => 'required|in:Laki-laki,Perempuan',
            'date_of_birth'     => 'nullable|date',
            'address'           => 'nullable|string',
            'emergency_contact' => 'nullable|string',
            'emergency_phone'   => 'nullable|string|max:20',
            'blood_type'        => 'nullable|in:A,B,AB,O',
            'health_notes'      => 'nullable|string',
            'status'            => 'required|in:active,inactive,expired,suspended',
        ]);

        $member->user->update([
            'name'  => $request->name,
            'email' => $request->email,
        ]);

        $member->update($request->only([
            'phone', 'gender', 'date_of_birth', 'address',
            'emergency_contact', 'emergency_phone', 'blood_type',
            'health_notes', 'status',
        ]));

        return redirect()->route('members.show', $member)->with('success', 'Data member berhasil diperbarui!');
    }

    public function destroy(Member $member)
    {
        $name = $member->user->name;
        $member->user->delete();
        return redirect()->route('members.index')->with('success', "Member {$name} berhasil dihapus.");
    }
}
