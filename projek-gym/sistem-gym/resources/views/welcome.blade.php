<!DOCTYPE html>
<html lang="en">
{{-- ============================================================
     HEAD SECTION
     Berisi konfigurasi meta, judul halaman, asset CSS/JS,
     font dari Google Fonts, ikon Font Awesome, dan Alpine.js
     untuk interaktivitas ringan (mobile menu toggle).
     ============================================================ --}}

<head>
    {{-- Encoding & Viewport --}}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MDHP GYM</title>

    {{-- Favicon --}}
    <link rel="icon" type="image/png" href="{{ asset('images/logo_gym.png') }}">

    {{-- Vite Asset Bundler: Kompilasi CSS Tailwind & JS utama --}}
    @vite(['resources/css/app.css', 'resources/js/app.js'])

    {{-- Google Fonts: Inter (body text) & Poppins (heading) --}}
    <link rel="preconnect" href="https://fonts.googleapis.com">

    {{-- Font Awesome 6: Library ikon yang digunakan di seluruh halaman --}}
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    {{-- Alpine.js: Framework JS ringan untuk interaktivitas (mobile menu) --}}
    {{-- defer = dimuat setelah HTML selesai di-parse --}}
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>


{{-- ============================================================
     BODY
     x-data="{ mobileMenu: false }" → inisialisasi state Alpine.js
     untuk mengontrol buka/tutup menu mobile di navbar.
     ============================================================ --}}

<body class="bg-dark-950 text-white font-sans" x-data="{ mobileMenu: false }">

    {{-- ===== NAVBAR ===== --}}
    {{-- ============================================================
         Navigasi utama yang fixed di atas (z-50) dengan efek
         glassmorphism (backdrop-blur). Berisi:
         - Logo & nama gym (link ke section #home)
         - Menu navigasi desktop (tersembunyi di mobile)
         - Tombol Login/Dashboard (kondisional berdasarkan auth)
         - Tombol hamburger untuk mobile menu
         - Mobile dropdown menu (dikontrol Alpine.js)
         ============================================================ --}}
    <nav class="fixed top-0 w-full z-50 bg-dark-900/80 backdrop-blur-xl border-b border-dark-700/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">

                {{-- Logo & Nama Gym --}}
                <a href="#home" class="flex items-center gap-3 group cursor-pointer">
                    <img src="{{ asset('images/logo_gym.png') }}" alt="Logo"
                        class="w-12 h-12 rounded-full object-cover ring-2 ring-primary-500 group-hover:ring-primary-400 transition-all duration-300">
                    <div>
                        <h1
                            class="font-heading font-bold text-xl text-white group-hover:text-primary-400 transition-colors duration-300">
                            MDHP GYM</h1>
                        <p
                            class="text-xs text-primary-400 font-medium tracking-wide group-hover:text-primary-300 transition-colors duration-300">
                            GYM & FITNESS</p>
                    </div>
                </a>

                {{-- Menu Navigasi Desktop (hidden di mobile, tampil mulai md:) --}}
                <div class="hidden md:flex items-center gap-8">
                    <a href="#home"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Beranda</a>
                    <a href="#packages"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Paket</a>
                    <a href="#classes"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Kelas</a>
                    <a href="#trainers"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Trainer</a>

                    {{-- Tombol CTA: Tampilkan "Dashboard" jika sudah login, "Login" jika belum --}}
                    @auth
                        <a href="{{ route('dashboard') }}"
                            class="px-6 py-2.5 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold rounded-full text-sm hover:shadow-lg hover:shadow-primary-500/30 transition-all">Dashboard</a>
                    @else
                        <a href="{{ route('login') }}"
                            class="px-6 py-2.5 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold rounded-full text-sm hover:shadow-lg hover:shadow-primary-500/30 transition-all">Login</a>
                    @endauth
                </div>

                {{-- Tombol Hamburger (hanya tampil di mobile) --}}
                {{-- @click toggle state mobileMenu via Alpine.js --}}
                <button @click="mobileMenu = !mobileMenu" class="md:hidden text-white">
                    <i class="fas fa-bars text-xl"></i>
                </button>
            </div>
        </div>
        {{-- Mobile Dropdown Menu
             x-show     = tampil/sembunyi berdasarkan state mobileMenu
             x-cloak    = cegah flash konten sebelum Alpine.js siap
             x-transition = animasi fade saat buka/tutup --}}
        <div x-show="mobileMenu" x-cloak x-transition
            class="md:hidden bg-dark-900 border-t border-dark-700 px-6 py-4 space-y-3">
            <a href="#home" class="block text-dark-300 hover:text-primary-400">Beranda</a>
            <a href="#packages" class="block text-dark-300 hover:text-primary-400">Paket</a>
            <a href="#classes" class="block text-dark-300 hover:text-primary-400">Kelas</a>
            <a href="#trainers" class="block text-dark-300 hover:text-primary-400">Trainer</a>

            {{-- CTA Mobile: Kondisional berdasarkan status autentikasi --}}
            @auth
                <a href="{{ route('dashboard') }}"
                    class="block px-4 py-2 bg-primary-500 text-white rounded-lg text-center">Dashboard</a>
            @else
                <a href="{{ route('login') }}"
                    class="block px-4 py-2 bg-primary-500 text-white rounded-lg text-center">Login</a>
            @endauth
        </div>
    </nav>

    {{-- ===== HERO SECTION ===== --}}
    {{-- ============================================================
         Section pertama yang terlihat saat halaman dibuka (full screen).
         Berisi:
         - Dekorasi background (blur orbs animasi)
         - Headline utama dengan gradient text
         - Deskripsi singkat gym
         - Tombol CTA: "Daftar Sekarang" & "Lihat Kelas"
         - Statistik singkat: Member Aktif, Trainer, Jenis Kelas
         - Logo gym dengan badge-badge fitur (desktop only)
         ============================================================ --}}
    <section id="home" class="hero-gradient min-h-screen flex items-center relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-20 left-10 w-72 h-72 bg-primary-500 rounded-full blur-3xl"></div>
            <div class="absolute bottom-20 right-10 w-96 h-96 bg-danger-500 rounded-full blur-3xl"></div>
        </div>

        {{-- Dekorasi Background: Blur orbs berwarna untuk efek atmosfer --}}
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 relative z-10">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                {{-- Kolom Kiri: Konten teks utama --}}
                <div>
                    {{-- Badge Status "Open 24 Hours" --}}
                    <div
                        class="inline-flex items-center gap-2 px-4 py-1.5 bg-primary-500/10 border border-primary-500/30 rounded-full mb-6">
                        <span class="w-2 h-2 bg-primary-500 rounded-full animate-pulse"></span>
                        <span class="text-primary-400 text-sm font-medium">Open 24 Hours</span>
                    </div>
                    {{-- Headline Utama dengan Gradient Text --}}
                    <h1 class="font-heading font-black text-5xl lg:text-7xl leading-tight mb-6">
                        <span class="bg-gradient-to-r from-primary-400 to-danger-400 bg-clip-text text-transparent">MDHP
                            GYM</span><br>
                        <span class="text-white text-4xl lg:text-5xl">Your Fitness Partner</span>
                    </h1>
                    {{-- Deskripsi Singkat --}}
                    <p class="text-dark-400 text-lg mb-8 max-w-lg leading-relaxed">
                        Transformasi tubuhmu dimulai di sini. Bergabunglah dengan ribuan member yang telah merasakan
                        perubahan nyata bersama MDHP GYM.
                    </p>

                    {{-- Tombol CTA: Daftar & Lihat Kelas --}}
                    <div class="flex flex-wrap gap-4">

                        {{-- CTA Primer: Mengarah ke section packages --}}
                        <a href="#packages"
                            class="px-8 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-bold rounded-2xl text-lg hover:shadow-2xl hover:shadow-primary-500/30 transition-all transform hover:-translate-y-1">
                            <i class="fas fa-fire mr-2"></i> Daftar Sekarang
                        </a>

                        {{-- CTA Sekunder: Mengarah ke section classes --}}
                        <a href="#classes"
                            class="px-8 py-4 border-2 border-dark-600 text-white font-bold rounded-2xl text-lg hover:border-primary-500 hover:text-primary-400 transition-all">
                            <i class="fas fa-calendar-days mr-2"></i> Lihat Kelas
                        </a>
                    </div>

                    {{-- Statistik Singkat Gym --}}
                    <div class="flex items-center gap-8 mt-10">

                        {{-- Stat: Total Member Aktif --}}
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">100+</p>
                            <p class="text-dark-500 text-sm">Member Aktif</p>
                        </div>

                        {{-- Stat: Jumlah Trainer --}}
                        <div class="w-px h-12 bg-dark-700"></div>
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">15+</p>
                            <p class="text-dark-500 text-sm">Trainer Profesional</p>
                        </div>

                        {{-- Stat: Jenis Kelas Tersedia --}}
                        <div class="w-px h-12 bg-dark-700"></div>
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">8+</p>
                            <p class="text-dark-500 text-sm">Jenis Kelas</p>
                        </div>
                    </div>
                </div>

                {{-- Kolom Kanan: Logo dengan floating badge (desktop only) --}}
                <div class="hidden lg:flex justify-center">
                    <div class="relative">

                        {{-- Logo Utama dengan efek animasi shine --}}
                        <img src="{{ asset('images/logo_gym.png') }}" alt="MDHP GYM"
                            class="w-80 h-80 object-contain drop-shadow-2xl shine-animation">

                        {{-- Badge Pojok Kiri Atas: Komunitas Aktif --}}
                        <div
                            class="absolute -top-6 -left-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-primary-400 font-semibold text-sm"><i class="fas fa-users mr-1.5"></i>
                                Komunitas Aktif</p>
                        </div>

                        {{-- Badge Pojok Kanan Atas: Jumlah Alat --}}
                        <div
                            class="absolute -top-6 -right-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-primary-400 font-semibold text-sm"><i class="fas fa-dumbbell mr-1.5"></i> 50+
                                Alat</p>
                        </div>

                        {{-- Badge Pojok Kiri Bawah: Fasilitas AC --}}
                        <div
                            class="absolute -bottom-6 -left-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-danger-400 font-semibold text-sm"><i class="fas fa-heart-pulse mr-1.5"></i>
                                Full AC</p>
                        </div>

                        {{-- Badge Pojok Kanan Bawah: Keamanan 24/7 --}}
                        <div
                            class="absolute -bottom-6 -right-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-success-400 font-semibold text-sm"><i class="fas fa-shield-alt mr-1.5"></i>
                                24/7 Keamanan</p>
                        </div>
                    </div>
                </div>
            </div>
    </section>
    {{-- ===== MEMBERSHIP PACKAGES ===== --}}
    {{-- ============================================================
         Section daftar paket keanggotaan yang diambil dari database.
         Fitur utama:
         - Grid 4 kolom responsif (1 kolom mobile → 4 kolom desktop)
         - Badge "BEST VALUE" untuk paket >= 360 hari
         - Badge "POPULER" untuk paket >= 180 hari
         - Harga diformat dalam ribuan (contoh: Rp 150K)
         - Benefit ditampilkan dari kolom 'benefits' yang dipisah koma
         - Tombol CTA berbeda berdasarkan status login
         ============================================================ --}}
    <section id="packages"
        class="py-24 bg-gradient-to-b from-dark-900 via-dark-950 to-dark-900 relative overflow-hidden">
        {{-- Dekorasi Background: Blur orbs transparan --}}
        <div class="absolute inset-0 opacity-5">
            <div class="absolute top-1/4 left-10 w-96 h-96 bg-primary-500 rounded-full blur-3xl"></div>
            <div class="absolute bottom-1/4 right-10 w-96 h-96 bg-danger-500 rounded-full blur-3xl"></div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            {{-- Section Header --}}
            <div class="text-center mb-20">
                {{-- Label Badge --}}
                <div
                    class="inline-flex items-center gap-2 px-6 py-2 bg-gradient-to-r from-primary-500/20 to-danger-500/20 border border-primary-500/30 text-primary-400 text-sm font-bold rounded-full mb-6">
                    <i class="fas fa-crown text-gold-400"></i>
                    <span>PAKET MEMBERSHIP EKSKLUSIF</span>
                </div>
                <h2 class="font-heading font-black text-5xl lg:text-6xl text-white mb-6">
                    Pilih <span
                        class="bg-gradient-to-r from-primary-400 via-danger-400 to-primary-400 bg-clip-text text-transparent">Paketmu</span>
                </h2>
                <p class="text-dark-400 text-xl max-w-3xl mx-auto leading-relaxed">Investasi terbaik untuk kesehatan
                    dan kebugaran tubuhmu dengan berbagai pilihan paket membership yang fleksibel</p>
            </div>

            {{-- Grid Kartu Paket --}}
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-8 items-stretch">
                {{-- PHP Variables: Array ikon & gradien untuk tiap kartu paket
                     Diakses dengan modulo ($index % 4) agar berulang jika paket > 4 --}}
                @php
                    $packageIcons = ['fa-bolt', 'fa-fire', 'fa-star', 'fa-crown'];
                    $packageGradients = [
                        'from-blue-500/10 to-cyan-500/10',
                        'from-orange-500/10 to-red-500/10',
                        'from-purple-500/10 to-pink-500/10',
                        'from-gold-500/10 to-primary-500/10',
                    ];
                @endphp

                {{-- Loop Kartu Paket dari Database --}}
                @foreach ($packages as $index => $package)
                    <div
                        class="package-card bg-gradient-to-br {{ $packageGradients[$index % 4] }} backdrop-blur-sm border {{ $package->duration_days >= 180 ? 'border-primary-500/50' : 'border-dark-700/50' }} rounded-3xl p-8 relative group overflow-hidden h-full flex flex-col">
                        {{-- Dekorasi Sudut Kartu --}}
                        <div
                            class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br from-primary-500/20 to-transparent rounded-bl-full">
                        </div>

                        {{-- Header Kartu: Ikon + Badge Status Paket --}}
                        <div class="mb-6 flex items-center gap-4">
                            {{-- Ikon Paket --}}
                            <div
                                class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-primary-500 to-danger-500 shadow-lg group-hover:scale-110 transition-transform duration-300">
                                <i class="fas {{ $packageIcons[$index % 4] }} text-white text-2xl"></i>
                            </div>

                            {{-- Badge Kondisional:
                                 >= 360 hari → "BEST VALUE" (animated pulse + gradient emas)
                                 >= 180 hari → "POPULER" (gradient merah-oranye) --}}
                            @if ($package->duration_days >= 360)
                                <div
                                    class="px-4 py-1.5 bg-gradient-to-r from-gold-400 via-primary-500 to-danger-500 text-white text-xs font-black rounded-full shadow-2xl flex items-center gap-2 animate-pulse">
                                    <i class="fas fa-gem"></i>
                                    <span>BEST VALUE</span>
                                </div>
                            @elseif($package->duration_days >= 180)
                                <div
                                    class="px-4 py-1.5 bg-gradient-to-r from-primary-500 to-danger-500 text-white text-xs font-bold rounded-full shadow-lg">
                                    <i class="fas fa-fire"></i> POPULER
                                </div>
                            @endif
                        </div>

                        {{-- Nama & Durasi Paket --}}
                        <div class="mb-6">
                            <h3 class="font-heading font-black text-2xl text-white mb-2">{{ $package->name }}</h3>
                            <div class="flex items-center gap-2 text-primary-400 text-sm font-semibold">
                                <i class="fas fa-calendar-days"></i>
                                <span>{{ $package->duration_days }} hari akses penuh</span>
                            </div>
                        </div>

                        {{-- Harga Paket
                             Format: Rp XXXk (dibagi 1000, tanpa desimal)
                             Keterangan durasi: tampil dalam bulan jika >= 30 hari --}}
                        <div class="mb-6">
                            <div class="flex items-end gap-2 mb-1">
                                <span class="font-heading font-black text-4xl text-white price-glow">Rp
                                    {{ number_format($package->price / 1000, 0, ',', '.') }}K</span>
                            </div>
                            @if ($package->duration_days > 1)
                                <p class="text-dark-500 text-sm">
                                    {{ $package->duration_days >= 30 ? round($package->duration_days / 30) . ' bulan' : $package->duration_days . ' hari' }}
                                    membership
                                </p>
                            @endif
                        </div>

                        {{-- Daftar Benefit Paket
                             Diambil dari kolom 'benefits' yang dipisah koma (CSV)
                             Fallback default: 'Akses Gym,Locker Gratis,Free Konsultasi' --}}
                        <div class="mb-6 flex-grow">
                            <div class="space-y-3">
                                @foreach (explode(',', $package->benefits ?? 'Akses Gym,Locker Gratis,Free Konsultasi') as $benefit)
                                    <div class="flex items-start gap-3 text-dark-200 text-sm">
                                        <div
                                            class="flex-shrink-0 w-5 h-5 rounded-full bg-gradient-to-r from-primary-500 to-danger-500 flex items-center justify-center mt-0.5">
                                            <i class="fas fa-check text-white text-xs"></i>
                                        </div>
                                        <span class="leading-relaxed">{{ trim($benefit) }}</span>
                                    </div>
                                @endforeach
                            </div>
                        </div>

                        {{-- CTA Button --}}
                        <div class="mt-auto">
                            @auth
                                <a href="{{ route('members.create') }}"
                                    class="block w-full py-4 text-center rounded-2xl font-bold text-base transition-all duration-300 {{ $package->duration_days >= 180 ? 'bg-gradient-to-r from-primary-500 to-danger-500 text-white hover:shadow-2xl hover:shadow-primary-500/50 hover:scale-105' : 'bg-dark-700 text-white hover:bg-gradient-to-r hover:from-dark-600 hover:to-dark-700 hover:shadow-xl' }} transform">
                                    <i class="fas fa-rocket mr-2"></i> Pilih Paket Ini
                                </a>
                            @else
                                <a href="{{ route('login') }}"
                                    class="block w-full py-4 text-center rounded-2xl font-bold text-base transition-all duration-300 {{ $package->duration_days >= 180 ? 'bg-gradient-to-r from-primary-500 to-danger-500 text-white hover:shadow-2xl hover:shadow-primary-500/50 hover:scale-105' : 'bg-dark-700 text-white hover:bg-gradient-to-r hover:from-dark-600 hover:to-dark-700 hover:shadow-xl' }} transform">
                                    <i class="fas fa-arrow-right mr-2"></i> Daftar Sekarang
                                </a>
                            @endauth
                        </div>
                    </div>
                @endforeach
            </div>

            {{-- Additional Info --}}
            <div class="mt-16 text-center">
                <div class="inline-flex flex-wrap items-center justify-center gap-8 text-sm text-dark-400">
                    <div class="flex items-center gap-2">
                        <i class="fas fa-clock text-primary-500 text-lg"></i>
                        <span>Akses 24/7</span>
                    </div>
                </div>
                <div class="flex items-center gap-2">
                    <i class="fas fa-users text-primary-500 text-lg"></i>
                    <span>Trainer Profesional</span>
                </div>
                <div class="flex items-center gap-2">
                    <i class="fas fa-dumbbell text-primary-500 text-lg"></i>
                    <span>50+ Alat Modern</span>
                </div>
            </div>
        </div>
    </section>
    {{-- ===== CLASSES ===== --}}
    <section id="classes"
        class="py-20 bg-gradient-to-b from-dark-900 via-dark-950 to-dark-900 relative overflow-hidden">
        <!-- Multi-Layer Background Decoration -->
        <div class="absolute inset-0">
            <!-- Animated Gradient Orbs -->
            <div
                class="absolute top-10 left-10 w-96 h-96 bg-gradient-to-br from-danger-500 to-orange-600 rounded-full blur-3xl opacity-10 animate-pulse">
            </div>
            <div
                class="absolute top-40 right-20 w-80 h-80 bg-gradient-to-br from-primary-500 to-blue-600 rounded-full blur-3xl opacity-10 float-6">
            </div>
            <div
                class="absolute bottom-20 left-1/4 w-96 h-96 bg-gradient-to-br from-purple-500 to-pink-500 rounded-full blur-3xl opacity-10 float-8-reverse">
            </div>
            <div
                class="absolute bottom-10 right-1/3 w-72 h-72 bg-gradient-to-br from-cyan-500 to-teal-500 rounded-full blur-3xl opacity-10 animate-pulse">
            </div>

            <!-- Grid Pattern Overlay -->
            <div class="absolute inset-0 opacity-5 grid-bg-orange"></div>

            <!-- Diagonal Lines -->
            <div class="absolute inset-0 opacity-5">
                <div class="absolute top-0 left-0 w-full h-full diagonal-bg-orange"></div>
            </div>

            <!-- Light Spots -->
            <div
                class="absolute top-1/4 left-1/2 w-64 h-64 bg-gradient-radial from-primary-400/10 to-transparent rounded-full blur-2xl">
            </div>
            <div
                class="absolute bottom-1/3 right-1/4 w-56 h-56 bg-gradient-radial from-danger-400/10 to-transparent rounded-full blur-2xl">
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-16">
                <div
                    class="inline-flex items-center gap-2 px-6 py-2.5 bg-gradient-to-r from-danger-500/10 to-primary-500/10 border border-danger-500/20 rounded-full mb-4">
                    <span class="w-2 h-2 bg-danger-500 rounded-full animate-pulse"></span>
                    <span class="text-danger-400 text-sm font-bold tracking-wider">KELAS KAMI</span>
                </div>
                <h2 class="font-heading font-black text-4xl lg:text-5xl text-white mb-4">
                    Kelas Fitness <span
                        class="bg-gradient-to-r from-danger-400 to-primary-400 bg-clip-text text-transparent">Terbaik</span>
                </h2>
                <p class="text-dark-400 text-lg max-w-2xl mx-auto">Dipandu oleh trainer bersertifikat untuk hasil
                    maksimal</p>
            </div>

            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
                @php
                    $classIcons = [
                        'Yoga' => 'fa-spa',
                        'HIIT' => 'fa-fire-flame-curved',
                        'Zumba' => 'fa-music',
                        'Body Combat' => 'fa-hand-fist',
                        'CrossFit' => 'fa-person-running',
                        'Pilates' => 'fa-child-reaching',
                        'Spinning' => 'fa-bicycle',
                        'Muay Thai' => 'fa-mitten',
                    ];
                    $classColors = [
                        'from-blue-500 to-blue-600',
                        'from-red-500 to-orange-500',
                        'from-pink-500 to-purple-500',
                        'from-yellow-500 to-red-500',
                        'from-green-500 to-teal-500',
                        'from-indigo-500 to-purple-500',
                        'from-cyan-500 to-blue-500',
                        'from-orange-500 to-red-600',
                    ];
                    $popularClasses = ['HIIT', 'Zumba', 'CrossFit']; // Kelas populer
                @endphp
                @foreach ($classes as $i => $class)
                    <div
                        class="group relative bg-gradient-to-br from-dark-800/90 via-dark-850 to-dark-900/90 backdrop-blur-sm border border-dark-700/50 rounded-3xl p-7 transition-all duration-700 hover:border-transparent overflow-hidden hover:shadow-2xl hover:shadow-{{ explode(' ', $classColors[$i % count($classColors)])[0] }}/20 hover:-translate-y-2 cursor-pointer">
                        <!-- Animated Background Gradient -->
                        <div
                            class="absolute inset-0 bg-gradient-to-br {{ $classColors[$i % count($classColors)] }} opacity-0 group-hover:opacity-10 transition-all duration-700 rounded-3xl">
                        </div>

                        <!-- Glowing Border Effect -->
                        <div
                            class="absolute inset-0 bg-gradient-to-br {{ $classColors[$i % count($classColors)] }} opacity-0 group-hover:opacity-100 transition-opacity duration-700 rounded-3xl blur-xl -z-10">
                        </div>
                        <div
                            class="absolute inset-px bg-gradient-to-br from-dark-800 via-dark-850 to-dark-900 rounded-3xl">
                        </div>

                        <!-- Decorative Corner Accent -->
                        <div
                            class="absolute top-0 right-0 w-24 h-24 bg-gradient-to-br {{ $classColors[$i % count($classColors)] }} opacity-10 rounded-bl-full -z-0">
                        </div>
                        <div
                            class="absolute bottom-0 left-0 w-20 h-20 bg-gradient-to-tr {{ $classColors[$i % count($classColors)] }} opacity-5 rounded-tr-full -z-0">
                        </div>

                        <!-- Content -->
                        <div class="relative z-10">
                            <!-- Popular Badge -->
                            @if (in_array($class->name, $popularClasses))
                                <div
                                    class="absolute -top-3 -right-3 bg-gradient-to-r from-primary-500 via-primary-600 to-danger-500 text-white text-xs font-bold px-3.5 py-1.5 rounded-full shadow-xl animate-pulse">
                                    <i class="fas fa-star mr-1 text-yellow-300"></i>Populer
                                </div>
                            @endif

                            <!-- Icon with Enhanced Glow -->
                            <div class="relative w-20 h-20 mb-5 group-hover:mb-6 transition-all duration-500">
                                <!-- Outer Glow -->
                                <div
                                    class="absolute -inset-2 bg-gradient-to-br {{ $classColors[$i % count($classColors)] }} rounded-3xl blur-xl opacity-0 group-hover:opacity-70 group-hover:blur-2xl transition-all duration-700 group-hover:animate-pulse">
                                </div>

                                <!-- Middle Glow -->
                                <div
                                    class="absolute inset-0 bg-gradient-to-br {{ $classColors[$i % count($classColors)] }} rounded-3xl blur-lg opacity-40 group-hover:opacity-80 transition-all duration-500">
                                </div>

                                <!-- Icon Container -->
                                <div
                                    class="relative w-20 h-20 rounded-3xl bg-gradient-to-br {{ $classColors[$i % count($classColors)] }} flex items-center justify-center shadow-2xl group-hover:scale-110 transition-all duration-700 group-hover:shadow-{{ explode(' ', $classColors[$i % count($classColors)])[0] }}/50">
                                    <i
                                        class="fas {{ $classIcons[$class->name] ?? 'fa-dumbbell' }} text-white text-3xl group-hover:scale-125 transition-transform duration-500"></i>
                                </div>
                            </div>

                            <!-- Class Name with Gradient -->
                            <div class="mb-3">
                                <h3
                                    class="font-heading font-black text-2xl text-white mb-1 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:{{ $classColors[$i % count($classColors)] }} group-hover:bg-clip-text transition-all duration-500 leading-tight">
                                    {{ $class->name }}
                                </h3>
                                <div
                                    class="h-1 w-0 bg-gradient-to-r {{ $classColors[$i % count($classColors)] }} rounded-full group-hover:w-16 transition-all duration-500">
                                </div>
                            </div>

                            <!-- Description -->
                            <p
                                class="text-dark-400 text-sm leading-relaxed mb-5 group-hover:text-dark-300 transition-colors duration-300 min-h-[3rem]">
                                {{ Str::limit($class->description, 75) }}
                            </p>

                            <!-- Divider Line -->
                            <div
                                class="h-px bg-gradient-to-r from-transparent via-dark-700 to-transparent mb-4 group-hover:via-{{ explode(' ', $classColors[$i % count($classColors)])[0] }}/30 transition-colors duration-500">
                            </div>

                            <!-- Info Tags with Icons -->
                            <div class="flex items-center gap-2.5 text-xs mb-4">
                                <div
                                    class="flex items-center gap-2 px-3.5 py-2 bg-dark-700/40 backdrop-blur-sm rounded-xl text-dark-400 group-hover:bg-gradient-to-r group-hover:{{ $classColors[$i % count($classColors)] }}/20 group-hover:text-white group-hover:shadow-lg transition-all duration-500 border border-dark-600/30 group-hover:border-{{ explode(' ', $classColors[$i % count($classColors)])[0] }}/30">
                                    <i
                                        class="fas fa-clock text-{{ explode(' ', $classColors[$i % count($classColors)])[0] }}"></i>
                                    <span class="font-semibold">{{ $class->duration_minutes }} min</span>
                                </div>
                                <div
                                    class="flex items-center gap-2 px-3.5 py-2 bg-dark-700/40 backdrop-blur-sm rounded-xl text-dark-400 group-hover:bg-gradient-to-r group-hover:{{ $classColors[$i % count($classColors)] }}/20 group-hover:text-white group-hover:shadow-lg transition-all duration-500 border border-dark-600/30 group-hover:border-{{ explode(' ', $classColors[$i % count($classColors)])[0] }}/30">
                                    <i
                                        class="fas fa-signal text-{{ explode(' ', $classColors[$i % count($classColors)])[0] }}"></i>
                                    <span class="font-semibold">{{ $class->difficulty }}</span>
                                </div>
                            </div>

                            <!-- CTA Button with Shine Effect -->
                            <a href="{{ route('login') }}"
                                class="block relative overflow-hidden rounded-xl opacity-0 group-hover:opacity-100 transform translate-y-3 group-hover:translate-y-0 transition-all duration-500">
                                <div
                                    class="absolute inset-0 bg-gradient-to-r {{ $classColors[$i % count($classColors)] }} opacity-100">
                                </div>
                                <div
                                    class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000">
                                </div>
                                <div class="relative px-4 py-2.5 text-center">
                                    <span class="text-white font-bold text-sm flex items-center justify-center gap-2">
                                        <span>Gabung Kelas</span>
                                        <i
                                            class="fas fa-arrow-right group-hover:translate-x-1 transition-transform duration-300"></i>
                                    </span>
                                </div>
                            </a>
                        </div>

                        <!-- Floating Particles Effect -->
                        <div
                            class="absolute top-1/4 right-1/4 w-2 h-2 bg-{{ explode(' ', $classColors[$i % count($classColors)])[0] }} rounded-full opacity-0 group-hover:opacity-40 transition-opacity duration-700 blur-sm">
                        </div>
                        <div
                            class="absolute bottom-1/3 left-1/4 w-1.5 h-1.5 bg-{{ explode(' ', $classColors[$i % count($classColors)])[0] }} rounded-full opacity-0 group-hover:opacity-30 transition-opacity duration-700 blur-sm">
                        </div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    {{-- ===== TRAINERS ===== --}}
    <section id="trainers"
        class="py-24 bg-gradient-to-b from-dark-900 via-dark-950 to-dark-900 relative overflow-hidden">
        {{-- Multi-Layer Background Decoration --}}
        <div class="absolute inset-0">
            <!-- Animated Gradient Orbs -->
            <div
                class="absolute top-20 left-10 w-96 h-96 bg-gradient-to-br from-gold-500 via-primary-500 to-orange-600 rounded-full blur-3xl opacity-10 animate-pulse">
            </div>
            <div
                class="absolute top-1/3 right-20 w-80 h-80 bg-gradient-to-br from-primary-500 to-purple-600 rounded-full blur-3xl opacity-10 float-6">
            </div>
            <div
                class="absolute bottom-20 left-1/3 w-96 h-96 bg-gradient-to-br from-danger-500 to-pink-500 rounded-full blur-3xl opacity-10 float-8-reverse">
            </div>
            <div
                class="absolute bottom-32 right-1/4 w-72 h-72 bg-gradient-to-br from-gold-400 to-primary-500 rounded-full blur-3xl opacity-10 animate-pulse">
            </div>

            <!-- Grid Pattern Overlay -->
            <div class="absolute inset-0 opacity-5 grid-bg-gold"></div>

            <!-- Diagonal Lines -->
            <div class="absolute inset-0 opacity-5">
                <div class="absolute top-0 left-0 w-full h-full diagonal-bg-gold"></div>
            </div>

            <!-- Light Spots -->
            <div
                class="absolute top-1/4 left-1/2 w-64 h-64 bg-gradient-radial from-gold-400/10 to-transparent rounded-full blur-2xl">
            </div>
            <div
                class="absolute bottom-1/3 right-1/4 w-56 h-56 bg-gradient-radial from-primary-400/10 to-transparent rounded-full blur-2xl">
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-20">
                <div
                    class="inline-flex items-center gap-2 px-6 py-2.5 bg-gradient-to-r from-gold-500/10 to-primary-500/10 border border-gold-500/20 rounded-full mb-4">
                    <i class="fas fa-crown text-gold-400 animate-pulse"></i>
                    <span class="text-gold-400 text-sm font-bold tracking-wider">TRAINER KAMI</span>
                </div>
                <h2 class="font-heading font-black text-5xl lg:text-6xl text-white mb-6">
                    <span
                        class="bg-gradient-to-r from-gold-400 via-primary-400 to-gold-400 bg-clip-text text-transparent">Trainer
                        Profesional</span>
                </h2>
                <p class="text-dark-400 text-xl max-w-3xl mx-auto leading-relaxed">Bimbingan dari para ahli
                    bersertifikat untuk membantu Anda mencapai target fitness dengan maksimal</p>
            </div>

            <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
                @php
                    $trainerGradients = [
                        'from-blue-500/10 to-cyan-500/10',
                        'from-purple-500/10 to-pink-500/10',
                        'from-orange-500/10 to-red-500/10',
                        'from-green-500/10 to-teal-500/10',
                        'from-gold-500/10 to-primary-500/10',
                        'from-indigo-500/10 to-purple-500/10',
                    ];
                    $trainerBorderColors = [
                        'from-blue-500 to-cyan-500',
                        'from-purple-500 to-pink-500',
                        'from-orange-500 to-red-500',
                        'from-green-500 to-teal-500',
                        'from-gold-500 to-primary-500',
                        'from-indigo-500 to-purple-500',
                    ];
                    $iconBgColors = [
                        'from-blue-500 to-cyan-600',
                        'from-purple-500 to-pink-600',
                        'from-orange-500 to-red-600',
                        'from-green-500 to-teal-600',
                        'from-gold-500 to-primary-600',
                        'from-indigo-500 to-purple-600',
                    ];
                @endphp
                @foreach ($trainers as $index => $trainer)
                    <div
                        class="group relative bg-gradient-to-br {{ $trainerGradients[$index % 6] }} backdrop-blur-sm border border-dark-700/50 rounded-3xl overflow-hidden transition-all duration-700 hover:border-transparent hover:shadow-2xl hover:-translate-y-3 cursor-pointer">
                        {{-- Animated Gradient Border on Hover --}}
                        <div
                            class="absolute inset-0 bg-gradient-to-br {{ $trainerBorderColors[$index % 6] }} opacity-0 group-hover:opacity-100 transition-opacity duration-700 rounded-3xl blur-xl -z-10">
                        </div>
                        <div
                            class="absolute inset-px bg-gradient-to-br from-dark-800 via-dark-850 to-dark-900 rounded-3xl">
                        </div>

                        {{-- Top Gradient Bar --}}
                        <div
                            class="relative h-2 bg-gradient-to-r {{ $trainerBorderColors[$index % 6] }} group-hover:h-3 transition-all duration-300">
                        </div>

                        {{-- Card Content --}}
                        <div class="relative p-8">
                            {{-- Decorative Corner --}}
                            <div
                                class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br {{ $trainerGradients[$index % 6] }} opacity-20 rounded-bl-full">
                            </div>

                            {{-- Certified Badge --}}
                            @if ($trainer->certification)
                                <div
                                    class="absolute top-6 right-6 bg-gradient-to-r {{ $iconBgColors[$index % 6] }} text-white text-xs font-bold px-3 py-1.5 rounded-full shadow-lg flex items-center gap-1.5 opacity-0 group-hover:opacity-100 transition-all duration-500 transform group-hover:scale-100 scale-90">
                                    <i class="fas fa-certificate"></i>
                                    <span>Certified</span>
                                </div>
                            @endif

                            {{-- Profile Image with Enhanced Styling --}}
                            <div class="relative w-32 h-32 mx-auto mb-6 group-hover:mb-7 transition-all duration-500">
                                {{-- Outer Glow Effect --}}
                                <div
                                    class="absolute -inset-3 bg-gradient-to-br {{ $trainerBorderColors[$index % 6] }} rounded-full blur-xl opacity-0 group-hover:opacity-70 transition-all duration-700 animate-pulse">
                                </div>

                                {{-- Middle Ring --}}
                                <div
                                    class="absolute -inset-2 bg-gradient-to-br {{ $trainerBorderColors[$index % 6] }} rounded-full blur-lg opacity-40 group-hover:opacity-80 transition-all duration-500">
                                </div>

                                {{-- Image Container --}}
                                <div
                                    class="relative w-32 h-32 rounded-full overflow-hidden shadow-2xl ring-4 ring-dark-700 group-hover:ring-0 transition-all duration-500 group-hover:scale-110">
                                    <div
                                        class="absolute inset-0 bg-gradient-to-br {{ $trainerBorderColors[$index % 6] }} opacity-20">
                                    </div>
                                    <img src="{{ asset('images/logo_gym.png') }}"
                                        alt="{{ $trainer->user->name ?? 'Trainer' }}"
                                        class="w-full h-full object-cover relative z-10 group-hover:scale-110 transition-transform duration-700">
                                </div>

                                {{-- Status Indicator --}}
                                <div
                                    class="absolute bottom-2 right-2 w-5 h-5 bg-green-500 border-4 border-dark-800 rounded-full shadow-lg group-hover:scale-110 transition-transform duration-300">
                                </div>
                            </div>

                            {{-- Trainer Info --}}
                            <div class="text-center mb-5">
                                <h3
                                    class="font-heading font-black text-2xl text-white mb-2 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:{{ $trainerBorderColors[$index % 6] }} group-hover:bg-clip-text transition-all duration-500">
                                    {{ $trainer->user->name ?? 'Trainer' }}
                                </h3>
                                <div
                                    class="h-1 w-0 bg-gradient-to-r {{ $trainerBorderColors[$index % 6] }} rounded-full mx-auto group-hover:w-20 transition-all duration-500 mb-3">
                                </div>

                                {{-- Specialization Badge --}}
                                <div
                                    class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r {{ $trainerGradients[$index % 6] }} border border-dark-600/30 rounded-full mb-3 group-hover:border-transparent group-hover:shadow-lg transition-all duration-300">
                                    <i class="fas fa-dumbbell text-primary-400 text-sm"></i>
                                    <span
                                        class="text-primary-400 text-sm font-bold">{{ $trainer->specialization }}</span>
                                </div>

                                {{-- Certification --}}
                                <p
                                    class="text-dark-400 text-sm leading-relaxed mb-4 group-hover:text-dark-300 transition-colors duration-300 px-4">
                                    {{ $trainer->certification }}
                                </p>
                            </div>

                            {{-- Divider Line --}}
                            <div
                                class="h-px bg-gradient-to-r from-transparent via-dark-700 to-transparent mb-5 group-hover:via-gold-500/30 transition-colors duration-500">
                            </div>

                            {{-- Stats Grid --}}
                            <div class="grid grid-cols-2 gap-4 mb-5">
                                {{-- Experience --}}
                                <div
                                    class="bg-dark-700/40 backdrop-blur-sm rounded-xl p-4 border border-dark-600/30 group-hover:bg-gradient-to-br group-hover:{{ $trainerGradients[$index % 6] }} group-hover:border-transparent group-hover:shadow-lg transition-all duration-500">
                                    <div class="flex items-center justify-center gap-2 mb-1">
                                        <i class="fas fa-star text-gold-400 text-lg"></i>
                                        <span
                                            class="font-heading font-black text-2xl text-white">{{ $trainer->experience_years ?? 3 }}</span>
                                    </div>
                                    <p
                                        class="text-dark-400 text-xs font-medium text-center group-hover:text-dark-300 transition-colors">
                                        Tahun Experience</p>
                                </div>

                                {{-- Hourly Rate --}}
                                <div
                                    class="bg-dark-700/40 backdrop-blur-sm rounded-xl p-4 border border-dark-600/30 group-hover:bg-gradient-to-br group-hover:{{ $trainerGradients[$index % 6] }} group-hover:border-transparent group-hover:shadow-lg transition-all duration-500">
                                    <div class="flex items-center justify-center gap-1 mb-1">
                                        <i class="fas fa-money-bill-wave text-green-400 text-sm"></i>
                                        <span
                                            class="font-heading font-black text-lg text-white">{{ number_format($trainer->hourly_rate / 1000, 0) }}K</span>
                                    </div>
                                    <p
                                        class="text-dark-400 text-xs font-medium text-center group-hover:text-dark-300 transition-colors">
                                        Per Jam</p>
                                </div>
                            </div>

                            {{-- CTA Button with Shine Effect --}}
                            <a href="{{ route('login') }}"
                                class="block relative overflow-hidden rounded-xl opacity-0 group-hover:opacity-100 transform translate-y-3 group-hover:translate-y-0 transition-all duration-500">
                                <div
                                    class="absolute inset-0 bg-gradient-to-r {{ $trainerBorderColors[$index % 6] }} opacity-100">
                                </div>
                                <div
                                    class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000">
                                </div>
                                <div class="relative px-6 py-3 text-center">
                                    <span class="text-white font-bold text-sm flex items-center justify-center gap-2">
                                        <i class="fas fa-user-plus"></i>
                                        <span>Booking Trainer</span>
                                        <i
                                            class="fas fa-arrow-right group-hover:translate-x-1 transition-transform duration-300"></i>
                                    </span>
                                </div>
                            </a>
                            {{-- Alternative Info Display (when not hovering) --}}
                            <div class="group-hover:hidden flex items-center justify-center gap-4 text-sm">
                                <div class="flex items-center gap-2 text-dark-500">
                                    <i class="fas fa-medal text-gold-400"></i>
                                    <span class="font-semibold">{{ $trainer->experience_years ?? 3 }}+ Tahun</span>
                                </div>
                                <div class="w-1 h-4 bg-dark-700 rounded-full"></div>
                                <div class="flex items-center gap-2 text-dark-500">
                                    <i class="fas fa-fire text-primary-400"></i>
                                    <span class="font-semibold">Professional</span>
                                </div>
                            </div>
                        </div>

                        {{-- Floating Particles Effect --}}
                        <div
                            class="absolute top-1/4 right-1/4 w-2 h-2 bg-gold-400 rounded-full opacity-0 group-hover:opacity-40 transition-opacity duration-700 blur-sm">
                        </div>
                        <div
                            class="absolute bottom-1/3 left-1/4 w-1.5 h-1.5 bg-primary-400 rounded-full opacity-0 group-hover:opacity-30 transition-opacity duration-700 blur-sm">
                        </div>
                    </div>
                @endforeach
            </div>

            {{-- Additional Info Section --}}
            <div class="mt-16 text-center">
                <div class="inline-flex flex-wrap items-center justify-center gap-8 text-sm text-dark-400">
                    <a href="{{ route('login') }}" class="flex items-center gap-3 group cursor-pointer">
                        <div
                            class="w-12 h-12 bg-gradient-to-br from-gold-500 to-primary-600 rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                            <i class="fas fa-user-graduate text-white text-lg"></i>
                        </div>
                        <div class="text-left">
                            <p class="text-white font-bold">Bersertifikat</p>
                            <p class="text-xs text-dark-500">Trainer Profesional</p>
                        </div>
                    </a>
                    <a href="{{ route('login') }}" class="flex items-center gap-3 group cursor-pointer">
                        <div class="flex items-center gap-3 group cursor-pointer">
                            <div
                                class="w-12 h-12 bg-gradient-to-br from-primary-500 to-blue-600 rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                                <i class="fas fa-comments text-white text-lg"></i>
                            </div>
                            <div class="text-left">
                                <p class="text-white font-bold">Konsultasi</p>
                                <p class="text-xs text-dark-500">Program Personal</p>
                            </div>
                        </div>
                    </a>
                    <a href="{{ route('login') }}" class="flex items-center gap-3 group cursor-pointer">
                        <div class="flex items-center gap-3 group cursor-pointer">
                            <div
                                class="w-12 h-12 bg-gradient-to-br from-danger-500 to-red-600 rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                                <i class="fas fa-chart-line text-white text-lg"></i>
                            </div>
                            <div class="text-left">
                                <p class="text-white font-bold">Progress</p>
                                <p class="text-xs text-dark-500">Tracking Rutin</p>
                            </div>
                        </div>
                    </a>
                    <a href="{{ route('login') }}" class="flex items-center gap-3 group cursor-pointer">
                        <div class="flex items-center gap-3 group cursor-pointer">
                            <div
                                class="w-12 h-12 bg-gradient-to-br from-green-500 to-teal-600 rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                                <i class="fas fa-trophy text-white text-lg"></i>
                            </div>
                            <div class="text-left">
                                <p class="text-white font-bold">Prestasi</p>
                                <p class="text-xs text-dark-500">Hasil Terbukti</p>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>

    {{-- ===== CTA ===== --}}
    <section class="py-15 bg-orange-500 relative overflow-hidden">
        <!-- Animated Top Border -->
        <div
            class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-white to-transparent border-animate">
        </div>
        <div class="absolute top-0 left-0 right-0 h-1 overflow-hidden">
            <div class="h-full w-1/3 bg-gradient-to-r from-transparent via-yellow-200 to-transparent border-flow-fwd">
            </div>
        </div>

        <!-- Animated Bottom Border -->
        <div
            class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-white to-transparent border-animate">
        </div>
        <div class="absolute bottom-0 left-0 right-0 h-1 overflow-hidden">
            <div class="h-full w-1/3 bg-gradient-to-r from-transparent via-yellow-200 to-transparent border-flow-rev">
            </div>
        </div>
        <!-- Floating Particles -->
        <div class="absolute top-1/4 left-1/4 w-3 h-3 bg-white rounded-full particles-6"></div>
        <div class="absolute top-1/3 right-1/3 w-2 h-2 bg-yellow-200 rounded-full particles-8-d1"></div>
        <div class="absolute bottom-1/3 left-1/3 w-2.5 h-2.5 bg-white rounded-full particles-7-d2"></div>
        <div class="absolute top-2/3 right-1/4 w-2 h-2 bg-yellow-100 rounded-full particles-9-d1-5"></div>
        <!-- Corner Glow Effects -->
        <div
            class="absolute top-0 left-0 w-32 h-32 bg-gradient-radial from-white/30 to-transparent rounded-full blur-2xl glow-anim">
        </div>
        <div
            class="absolute top-0 right-0 w-32 h-32 bg-gradient-radial from-white/30 to-transparent rounded-full blur-2xl glow-anim-d1">
        </div>
        <div
            class="absolute bottom-0 left-0 w-32 h-32 bg-gradient-radial from-white/30 to-transparent rounded-full blur-2xl glow-anim-d2">
        </div>
        <div
            class="absolute bottom-0 right-0 w-32 h-32 bg-gradient-radial from-white/30 to-transparent rounded-full blur-2xl glow-anim-d3">
        </div>

        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-0 left-0 w-40 h-40 bg-white rounded-full blur-3xl"></div>
            <div class="absolute bottom-0 right-0 w-60 h-60 bg-white rounded-full blur-3xl"></div>
        </div>
        <div class="max-w-4xl mx-auto px-4 text-center relative z-10">
            <h2 class="font-heading font-black text-4xl lg:text-5xl text-white mb-6">Siap Untuk Berubah?</h2>
            <p class="text-white/80 text-lg mb-8 max-w-2xl mx-auto">Mulai perjalanan fitnessmu hari ini. Daftar
                sekarang dan dapatkan diskon special untuk member baru!</p>
            @auth
                <a href="{{ route('members.create') }}"
                    class="inline-block px-10 py-4 bg-dark-900 text-white font-bold rounded-2xl text-lg hover:bg-dark-800 transition transform hover:-translate-y-1 shadow-2xl">
                    <i class="fas fa-user-plus mr-2"></i> Daftar Member Baru
                </a>
            @else
                <a href="{{ route('login') }}"
                    class="inline-block px-10 py-4 bg-dark-900 text-white font-bold rounded-2xl text-lg hover:bg-dark-800 transition transform hover:-translate-y-1 shadow-2xl"></a>
                <i class="fas fa-arrow-right mr-2"></i> Mulai Sekarang
                </a>
            @endauth
        </div>
    </section>
    {{-- ===== FOOTER ===== --}}
    <footer class="relative bg-gradient-to-br from-dark-950 via-dark-900 to-dark-950 border-t border-primary-500/20">
        {{-- Decorative Background Elements --}}
        <div class="absolute inset-0 overflow-hidden pointer-events-none">
            <div class="absolute top-0 left-1/4 w-96 h-96 bg-primary-500/5 rounded-full blur-3xl"></div>
            <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-primary-600/5 rounded-full blur-3xl"></div>
        </div>

        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
            {{-- Main Footer Content --}}
            <div class="grid md:grid-cols-4 gap-10 mb-12">
                {{-- Brand Section --}}
                <div class="md:col-span-1">
                    <div class="flex items-center gap-3 mb-6 group">
                        <div class="relative">
                            <div
                                class="absolute inset-0 bg-primary-500/30 rounded-full blur-lg group-hover:bg-primary-400/40 transition-all duration-300">
                            </div>
                            <img src="{{ asset('images/logo_gym.png') }}" alt="Logo"
                                class="relative w-12 h-12 rounded-full object-cover ring-2 ring-primary-500 group-hover:ring-primary-400 transition-all duration-300">
                        </div>
                        <div>
                            <h3 class="font-heading font-bold text-xl text-white">MDHP GYM</h3>
                            <p class="text-xs text-primary-400 font-medium">Your Fitness Partner</p>
                        </div>
                    </div>
                    <p class="text-dark-400 text-sm leading-relaxed mb-6">
                        Tempat fitness terbaik untuk transformasi tubuh dan kesehatanmu.
                        <span class="text-primary-400 font-semibold">Kesehatan itu mahal.</span>
                    </p>
                    {{-- Social Media Links --}}
                    <div class="flex gap-3">
                        <a href="https://www.facebook.com/mdhp_gym"
                            class="group relative w-10 h-10 bg-dark-800 hover:bg-primary-500 rounded-lg flex items-center justify-center transition-all duration-300 hover:scale-110 hover:shadow-lg hover:shadow-primary-500/50">
                            <i class="fab fa-facebook-f text-dark-400 group-hover:text-white transition-colors"></i>
                        </a>
                        <a href="https://www.instagram.com/mdhp_gym/"
                            class="group relative w-10 h-10 bg-dark-800 hover:bg-primary-500 rounded-lg flex items-center justify-center transition-all duration-300 hover:scale-110 hover:shadow-lg hover:shadow-primary-500/50">
                            <i class="fab fa-instagram text-dark-400 group-hover:text-white transition-colors"></i>
                        </a>
                        <a href="https://www.youtube.com/@mdhpgym"
                            class="group relative w-10 h-10 bg-dark-800 hover:bg-primary-500 rounded-lg flex items-center justify-center transition-all duration-300 hover:scale-110 hover:shadow-lg hover:shadow-primary-500/50">
                            <i class="fab fa-youtube text-dark-400 group-hover:text-white transition-colors"></i>
                        </a>
                        <a href="https://www.tiktok.com/@mdhp_gym"
                            class="group relative w-10 h-10 bg-dark-800 hover:bg-primary-500 rounded-lg flex items-center justify-center transition-all duration-300 hover:scale-110 hover:shadow-lg hover:shadow-primary-500/50">
                            <i class="fab fa-tiktok text-dark-400 group-hover:text-white transition-colors"></i>
                        </a>
                    </div>
                </div>
                {{-- Quick Links --}}
                <div class="md:col-span-1">
                    <h4 class="font-heading font-bold text-white mb-6 text-lg flex items-center gap-2">
                        <span class="w-1 h-6 bg-primary-500 rounded-full"></span>
                        Quick Links
                    </h4>
                    <ul class="space-y-3">
                        <li>
                            <a href="#home"
                                class="text-dark-400 hover:text-primary-400 text-sm flex items-center gap-2 group transition-all duration-300">
                                <i
                                    class="fas fa-chevron-right text-xs text-primary-500 group-hover:translate-x-1 transition-transform"></i>
                                Tentang Kami
                            </a>
                        </li>
                        <li>
                            <a href="#packages"
                                class="text-dark-400 hover:text-primary-400 text-sm flex items-center gap-2 group transition-all duration-300">
                                <i
                                    class="fas fa-chevron-right text-xs text-primary-500 group-hover:translate-x-1 transition-transform"></i>
                                Paket Membership
                            </a>
                        </li>
                        <li>
                            <a href="#classes"
                                class="text-dark-400 hover:text-primary-400 text-sm flex items-center gap-2 group transition-all duration-300">
                                <i
                                    class="fas fa-chevron-right text-xs text-primary-500 group-hover:translate-x-1 transition-transform"></i>
                                Kelas & Trainer
                            </a>
                        </li>
                        <li> <a href="#trainers"
                                class="text-dark-400 hover:text-primary-400 text-sm flex items-center gap-2 group transition-all duration-300">
                                <i
                                    class="fas fa-chevron-right text-xs text-primary-500 group-hover:translate-x-1 transition-transform"></i>
                                Personal Trainer
                            </a>
                        </li>
                    </ul>
                </div>
                </li>
                {{-- Operating Hours --}}
                <div class="md:col-span-1">
                    <h4 class="font-heading font-bold text-white mb-6 text-lg flex items-center gap-2">
                        <span class="w-1 h-6 bg-primary-500 rounded-full"></span>
                        Jam Operasional
                    </h4>
                    <div
                        class="bg-dark-800/50 backdrop-blur-sm border border-dark-700 rounded-xl p-5 hover:border-primary-500/50 transition-all duration-300">
                        <div class="flex items-center gap-3 mb-3">
                            <div
                                class="w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-600 rounded-lg flex items-center justify-center animate-pulse">
                                <i class="fas fa-clock text-white text-xl"></i>
                            </div>
                            <div>
                                <p class="text-white font-bold text-lg">24 Jam</p>
                                <p class="text-dark-400 text-xs">Setiap Hari</p>
                            </div>
                        </div>
                        <p class="text-primary-400 text-xs font-medium">
                            <i class="fas fa-shield-alt mr-1"></i>
                            Buka sepanjang waktu untuk Anda
                        </p>
                    </div>
                </div>
                {{-- Contact Info --}}
                <div class="md:col-span-1">
                    <h4 class="font-heading font-bold text-white mb-6 text-lg flex items-center gap-2">
                        <span class="w-1 h-6 bg-primary-500 rounded-full"></span>
                        Hubungi Kami
                    </h4>
                    <ul class="space-y-4">
                        <li class="group">
                            <a href="https://www.google.com/maps/search/?api=1&query=Jl.+Malang+Kota+No.+11+Malang"
                                target="_blank" class="flex items-center gap-3 group">
                                <div
                                    class="w-9 h-9 bg-dark-800 rounded-lg flex items-center justify-center flex-shrink-0 group-hover:bg-primary-500 transition-all duration-300">
                                    <i
                                        class="fas fa-map-marker-alt text-primary-500 group-hover:text-white transition-colors"></i>
                                </div>
                                <div class="flex items-center gap-2">
                                    <p class="text-dark-400 group-hover:text-primary-400 transition-colors">
                                        Jl. Malang Kota No. 11, Malang
                                    </p>
                                </div>
                            </a>
                        </li>
                        <li class="group">
                            <a href="tel:+6281234567890" class="flex items-start gap-3 text-sm">
                                <div
                                    class="w-9 h-9 bg-dark-800 rounded-lg flex items-center justify-center flex-shrink-0 group-hover:bg-primary-500 transition-all duration-300">
                                    <i
                                        class="fas fa-phone text-primary-500 group-hover:text-white transition-colors"></i>
                                </div>
                                <div>
                                    <p class="text-dark-400 group-hover:text-primary-400 transition-colors">
                                        +62 812-3456-7890
                                    </p>
                                </div>
                            </a>
                        </li>
                        <li class="group">
                            <a href="mailto:info@mdhpgym.com" class="flex items-start gap-3 text-sm">
                                <div
                                    class="w-9 h-9 bg-dark-800 rounded-lg flex items-center justify-center flex-shrink-0 group-hover:bg-primary-500 transition-all duration-300">
                                    <i
                                        class="fas fa-envelope text-primary-500 group-hover:text-white transition-colors"></i>
                                </div>
                                <div>
                                    <p class="text-dark-400 group-hover:text-primary-400 transition-colors">
                                        info@mdhpgym.com
                                    </p>
                                </div>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            {{-- Bottom Bar --}}
            <div class="border-t border-dark-800/50 pt-8">
                <div class="flex flex-col md:flex-row items-center justify-between gap-4">
                    <p class="text-dark-500 text-sm">
                        &copy; {{ date('Y') }} <a href="#home"
                            class="text-primary-400 font-semibold hover:text-primary-300 transition-colors">MDHP
                            GYM</a>.
                        All rights reserved.
                    </p>
                    <div class="flex items-center gap-6 text-xs text-dark-500">
                        <a href="#home" class="hover:text-primary-400 transition-colors">Privacy Policy</a>
                        <span class="w-1 h-1 bg-dark-700 rounded-full"></span>
                        <a href="#home" class="hover:text-primary-400 transition-colors">Terms of Service</a>
                        <span class="w-1 h-1 bg-dark-700 rounded-full"></span>
                        <a href="#home" class="hover:text-primary-400 transition-colors">Cookie Policy</a>
                    </div>
                </div>
            </div>
        </div>
        {{-- Decorative Top Border --}}
        <div
            class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-primary-500 to-transparent">
        </div>
    </footer>

</body>

</html>

</body>

</html>
