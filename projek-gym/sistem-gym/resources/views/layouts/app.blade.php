<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>@yield('title', 'NoProtein Gym') - Sistem Manajemen Gym</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: { 50:'#fff7ed',100:'#ffedd5',200:'#fed7aa',300:'#fdba74',400:'#fb923c',500:'#f97316',600:'#ea580c',700:'#c2410c',800:'#9a3412',900:'#7c2d12' },
                        danger: { 50:'#fef2f2',100:'#fee2e2',200:'#fecaca',300:'#fca5a5',400:'#f87171',500:'#ef4444',600:'#dc2626',700:'#b91c1c',800:'#991b1b',900:'#7f1d1d' },
                        dark: { 50:'#f9fafb',100:'#f3f4f6',200:'#e5e7eb',300:'#d1d5db',400:'#9ca3af',500:'#6b7280',600:'#4b5563',700:'#374151',800:'#1f2937',900:'#111827',950:'#0a0a0a' },
                        gold: { 400:'#D4A017',500:'#B8860B',600:'#996515' },
                    },
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        heading: ['Poppins', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        [x-cloak] { display: none !important; }
        .sidebar-link { @apply flex items-center gap-3 px-4 py-3 rounded-xl text-dark-300 hover:bg-dark-800 hover:text-white transition-all duration-200; }
        .sidebar-link.active { @apply bg-gradient-to-r from-primary-600 to-primary-500 text-white shadow-lg shadow-primary-500/25; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #1f2937; }
        ::-webkit-scrollbar-thumb { background: #4b5563; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #6b7280; }
    </style>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    @stack('styles')
</head>
<body class="bg-dark-100 font-sans" x-data="{ sidebarOpen: true, mobileSidebar: false }">
    <div class="flex min-h-screen">

        {{-- ===== SIDEBAR ===== --}}
        <aside class="fixed inset-y-0 left-0 z-50 w-72 bg-dark-900 transform transition-transform duration-300 lg:translate-x-0"
               :class="mobileSidebar ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'">
            <div class="flex flex-col h-full">
                {{-- Logo --}}
                <div class="flex items-center gap-3 px-6 py-5 border-b border-dark-700">
                    <img src="{{ asset('images/logo_gym.png') }}" alt="Logo Gym" class="w-12 h-12 rounded-full object-cover ring-2 ring-primary-500">
                    <div>
                        <h1 class="font-heading font-bold text-white text-lg leading-tight">NoProtein</h1>
                        <p class="text-xs text-primary-400 font-medium">GYM Management</p>
                    </div>
                </div>

                {{-- Navigation --}}
                <nav class="flex-1 px-4 py-6 space-y-1 overflow-y-auto">
                    <p class="px-4 text-xs font-semibold text-dark-500 uppercase tracking-wider mb-3">Menu Utama</p>

                    <a href="{{ route('dashboard') }}" class="sidebar-link {{ request()->routeIs('dashboard') ? 'active' : '' }}">
                        <i class="fas fa-th-large w-5 text-center"></i>
                        <span>Dashboard</span>
                    </a>

                    <a href="{{ route('members.index') }}" class="sidebar-link {{ request()->routeIs('members.*') ? 'active' : '' }}">
                        <i class="fas fa-users w-5 text-center"></i>
                        <span>Data Member</span>
                    </a>

                    <a href="{{ route('members.create') }}" class="sidebar-link {{ request()->routeIs('members.create') ? 'active' : '' }}">
                        <i class="fas fa-user-plus w-5 text-center"></i>
                        <span>Pendaftaran Baru</span>
                    </a>

                    <a href="{{ route('attendances.index') }}" class="sidebar-link {{ request()->routeIs('attendances.*') ? 'active' : '' }}">
                        <i class="fas fa-calendar-check w-5 text-center"></i>
                        <span>Absensi</span>
                    </a>

                    <p class="px-4 text-xs font-semibold text-dark-500 uppercase tracking-wider mb-3 mt-6">Fasilitas</p>

                    <a href="{{ route('classes.index') }}" class="sidebar-link {{ request()->routeIs('classes.*') ? 'active' : '' }}">
                        <i class="fas fa-dumbbell w-5 text-center"></i>
                        <span>Kelas & Jadwal</span>
                    </a>

                    <a href="{{ route('trainers.index') }}" class="sidebar-link {{ request()->routeIs('trainers.*') ? 'active' : '' }}">
                        <i class="fas fa-user-tie w-5 text-center"></i>
                        <span>Trainer</span>
                    </a>

                    <a href="{{ route('equipment.index') }}" class="sidebar-link {{ request()->routeIs('equipment.*') ? 'active' : '' }}">
                        <i class="fas fa-cogs w-5 text-center"></i>
                        <span>Peralatan</span>
                    </a>

                    <p class="px-4 text-xs font-semibold text-dark-500 uppercase tracking-wider mb-3 mt-6">Keuangan</p>

                    <a href="{{ route('payments.index') }}" class="sidebar-link {{ request()->routeIs('payments.*') ? 'active' : '' }}">
                        <i class="fas fa-money-bill-wave w-5 text-center"></i>
                        <span>Pembayaran</span>
                    </a>
                </nav>

                {{-- User Info --}}
                <div class="px-4 py-4 border-t border-dark-700">
                    <div class="flex items-center gap-3 px-2">
                        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-primary-500 to-danger-500 flex items-center justify-center text-white font-bold text-sm">
                            {{ strtoupper(substr(auth()->user()->name ?? 'A', 0, 1)) }}
                        </div>
                        <div class="flex-1 min-w-0">
                            <p class="text-sm font-medium text-white truncate">{{ auth()->user()->name ?? 'Admin' }}</p>
                            <p class="text-xs text-dark-400 capitalize">{{ auth()->user()->role ?? 'admin' }}</p>
                        </div>
                        <form method="POST" action="{{ route('logout') }}">
                            @csrf
                            <button type="submit" class="text-dark-400 hover:text-danger-400 transition" title="Logout">
                                <i class="fas fa-sign-out-alt"></i>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </aside>

        {{-- Mobile Overlay --}}
        <div x-show="mobileSidebar" x-cloak @click="mobileSidebar = false" class="fixed inset-0 z-40 bg-black/60 lg:hidden"></div>

        {{-- ===== MAIN CONTENT ===== --}}
        <main class="flex-1 lg:ml-72">
            {{-- Top Bar --}}
            <header class="sticky top-0 z-30 bg-white/80 backdrop-blur-lg border-b border-dark-200">
                <div class="flex items-center justify-between px-6 py-4">
                    <div class="flex items-center gap-4">
                        <button @click="mobileSidebar = !mobileSidebar" class="lg:hidden text-dark-600 hover:text-dark-900">
                            <i class="fas fa-bars text-xl"></i>
                        </button>
                        <div>
                            <h2 class="font-heading font-bold text-dark-900 text-xl">@yield('page-title', 'Dashboard')</h2>
                            <p class="text-sm text-dark-500">@yield('page-subtitle', 'Selamat datang di sistem manajemen gym')</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">
                        <span class="hidden sm:inline-flex items-center gap-2 text-sm text-dark-500">
                            <i class="fas fa-calendar-alt text-primary-500"></i>
                            {{ now()->translatedFormat('l, d F Y') }}
                        </span>
                    </div>
                </div>
            </header>

            {{-- Flash Messages --}}
            @if(session('success'))
                <div x-data="{ show: true }" x-show="show" x-init="setTimeout(() => show = false, 4000)"
                     class="mx-6 mt-4 px-4 py-3 bg-green-50 border border-green-200 text-green-700 rounded-xl flex items-center gap-3">
                    <i class="fas fa-check-circle text-green-500"></i>
                    <span class="text-sm">{{ session('success') }}</span>
                    <button @click="show = false" class="ml-auto text-green-400 hover:text-green-600"><i class="fas fa-times"></i></button>
                </div>
            @endif
            @if(session('error'))
                <div x-data="{ show: true }" x-show="show" x-init="setTimeout(() => show = false, 4000)"
                     class="mx-6 mt-4 px-4 py-3 bg-danger-50 border border-danger-200 text-danger-700 rounded-xl flex items-center gap-3">
                    <i class="fas fa-exclamation-circle text-danger-500"></i>
                    <span class="text-sm">{{ session('error') }}</span>
                    <button @click="show = false" class="ml-auto text-danger-400 hover:text-danger-600"><i class="fas fa-times"></i></button>
                </div>
            @endif

            {{-- Page Content --}}
            <div class="p-6">
                @yield('content')
            </div>
        </main>
    </div>

    @stack('scripts')
</body>
</html>
