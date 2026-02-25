<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MDHP GYM</title>
    <link rel="icon" type="image/png" href="{{ asset('images/logo_gym.png') }}">
    @vite(['resources/css/app.css', 'resources/js/app.js'])
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <style>
        [x-cloak] { display: none !important; }
        .hero-gradient { background: linear-gradient(135deg, #111827 0%, #1f2937 50%, #111827 100%); }
        .card-hover { transition: all 0.3s ease; }
        .card-hover:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(249, 115, 22, 0.15); }
        .glow { box-shadow: 0 0 40px rgba(249, 115, 22, 0.3); }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
        .float-animation { animation: float 3s ease-in-out infinite; }
        html { scroll-behavior: smooth; }
    </style>
</head>
<body class="bg-dark-950 text-white font-sans" x-data="{ mobileMenu: false }">

    {{-- ===== NAVBAR ===== --}}
    <nav class="fixed top-0 w-full z-50 bg-dark-900/80 backdrop-blur-xl border-b border-dark-700/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <div class="flex items-center gap-3">
                    <img src="{{ asset('images/logo_gym.png') }}" alt="Logo" class="w-12 h-12 rounded-full object-cover ring-2 ring-primary-500">
                    <div>
                        <h1 class="font-heading font-bold text-xl text-white">MDHP GYM</h1>
                        <p class="text-xs text-primary-400 font-medium tracking-wide">GYM & FITNESS</p>
                    </div>
                </div>
                <div class="hidden md:flex items-center gap-8">
                    <a href="#home" class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Beranda</a>
                    <a href="#packages" class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Paket</a>
                    <a href="#classes" class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Kelas</a>
                    <a href="#trainers" class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Trainer</a>
                    @auth
                        <a href="{{ route('dashboard') }}" class="px-6 py-2.5 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold rounded-full text-sm hover:shadow-lg hover:shadow-primary-500/30 transition-all">Dashboard</a>
                    @else
                        <a href="{{ route('login') }}" class="px-6 py-2.5 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold rounded-full text-sm hover:shadow-lg hover:shadow-primary-500/30 transition-all">Login</a>
                    @endauth
                </div>
                <button @click="mobileMenu = !mobileMenu" class="md:hidden text-white">
                    <i class="fas fa-bars text-xl"></i>
                </button>
            </div>
        </div>
        {{-- Mobile Menu --}}
        <div x-show="mobileMenu" x-cloak x-transition class="md:hidden bg-dark-900 border-t border-dark-700 px-6 py-4 space-y-3">
            <a href="#home" class="block text-dark-300 hover:text-primary-400">Home</a>
            <a href="#packages" class="block text-dark-300 hover:text-primary-400">Paket</a>
            <a href="#classes" class="block text-dark-300 hover:text-primary-400">Kelas</a>
            <a href="#trainers" class="block text-dark-300 hover:text-primary-400">Trainer</a>
            @auth
                <a href="{{ route('dashboard') }}" class="block px-4 py-2 bg-primary-500 text-white rounded-lg text-center">Dashboard</a>
            @else
                <a href="{{ route('login') }}" class="block px-4 py-2 bg-primary-500 text-white rounded-lg text-center">Login</a>
            @endauth
        </div>
    </nav>

    {{-- ===== HERO SECTION ===== --}}
    <section id="home" class="hero-gradient min-h-screen flex items-center relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-20 left-10 w-72 h-72 bg-primary-500 rounded-full blur-3xl"></div>
            <div class="absolute bottom-20 right-10 w-96 h-96 bg-danger-500 rounded-full blur-3xl"></div>
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 relative z-10">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-primary-500/10 border border-primary-500/30 rounded-full mb-6">
                        <span class="w-2 h-2 bg-primary-500 rounded-full animate-pulse"></span>
                        <span class="text-primary-400 text-sm font-medium">Open 24 Hours</span>
                    </div>
                    <h1 class="font-heading font-black text-5xl lg:text-7xl leading-tight mb-6">
                        <span class="bg-gradient-to-r from-primary-400 to-danger-400 bg-clip-text text-transparent">MDHP GYM</span><br>
                        <span class="text-white text-4xl lg:text-5xl">Your Fitness Partner</span>
                    </h1>
                    <p class="text-dark-400 text-lg mb-8 max-w-lg leading-relaxed">
                        Transformasi tubuhmu dimulai di sini. Bergabunglah dengan ribuan member yang telah merasakan perubahan nyata bersama MDHP GYM.
                    </p>
                    <div class="flex flex-wrap gap-4">
                        <a href="#packages" class="px-8 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-bold rounded-2xl text-lg hover:shadow-2xl hover:shadow-primary-500/30 transition-all transform hover:-translate-y-1">
                            <i class="fas fa-fire mr-2"></i> Daftar Sekarang
                        </a>
                        <a href="#classes" class="px-8 py-4 border-2 border-dark-600 text-white font-bold rounded-2xl text-lg hover:border-primary-500 hover:text-primary-400 transition-all">
                            <i class="fas fa-play-circle mr-2"></i> Lihat Kelas
                        </a>
                    </div>
                    <div class="flex items-center gap-8 mt-10">
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">500+</p>
                            <p class="text-dark-500 text-sm">Member Aktif</p>
                        </div>
                        <div class="w-px h-12 bg-dark-700"></div>
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">15+</p>
                            <p class="text-dark-500 text-sm">Trainer Pro</p>
                        </div>
                        <div class="w-px h-12 bg-dark-700"></div>
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">8+</p>
                            <p class="text-dark-500 text-sm">Jenis Kelas</p>
                        </div>
                    </div>
                </div>
                <div class="hidden lg:flex justify-center">
                    <div class="relative">
                        <div class="w-80 h-80 rounded-full bg-gradient-to-br from-primary-500/20 to-danger-500/20 glow flex items-center justify-center float-animation">
                            <img src="{{ asset('images/logo_gym.png') }}" alt="MDHP GYM" class="w-64 h-64 object-contain drop-shadow-2xl">
                        </div>
                        <div class="absolute -top-4 -right-4 bg-dark-800 border border-dark-700 rounded-2xl px-4 py-3 shadow-xl">
                            <p class="text-primary-400 font-bold text-lg"><i class="fas fa-dumbbell mr-1"></i> 100+ Alat</p>
                        </div>
                        <div class="absolute -bottom-4 -left-4 bg-dark-800 border border-dark-700 rounded-2xl px-4 py-3 shadow-xl">
                            <p class="text-danger-400 font-bold text-lg"><i class="fas fa-heart-pulse mr-1"></i> Full AC</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    {{-- ===== MEMBERSHIP PACKAGES ===== --}}
    <section id="packages" class="py-20 bg-dark-900">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <span class="inline-block px-10 py-3 bg-primary-500/10 text-primary-400 text-sm font-semibold rounded-full mb-4">PAKET MEMBERSHIP</span>
                <h2 class="font-heading font-black text-4xl lg:text-5xl text-white mb-4">Pilih Paketmu</h2>
                <p class="text-dark-400 text-lg max-w-2xl mx-auto">Berbagai pilihan paket membership yang sesuai dengan kebutuhan dan budget kamu</p>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
                @foreach($packages as $package)
                <div class="card-hover bg-dark-800 border border-dark-700 rounded-2xl p-6 relative {{ $package->duration_days >= 180 ? 'ring-2 ring-primary-500' : '' }}">
                    @if($package->duration_days >= 360)
                        <div class="absolute -top-3 left-1/2 -translate-x-1/2 px-4 py-1 bg-gradient-to-r from-primary-500 to-danger-500 text-white text-xs font-bold rounded-full">BEST VALUE</div>
                    @endif
                    <div class="mb-4">
                        <h3 class="font-heading font-bold text-xl text-white">{{ $package->name }}</h3>
                        <p class="text-dark-400 text-sm mt-1">{{ $package->duration_days }} hari</p>
                    </div>
                    <div class="mb-6">
                        <span class="font-heading font-black text-3xl text-primary-400">Rp {{ number_format($package->price / 1000, 0, ',', '.') }}K</span>
                        @if($package->duration_days > 1)
                            <span class="text-dark-500 text-sm ml-1">/ {{ $package->duration_days >= 30 ? round($package->duration_days/30) . ' bulan' : $package->duration_days . ' hari' }}</span>
                        @endif
                    </div>
                    <ul class="space-y-2 mb-6 text-sm">
                        @foreach(explode(',', $package->benefits ?? 'Akses Gym,Locker Gratis') as $benefit)
                        <li class="flex items-center gap-2 text-dark-300">
                            <i class="fas fa-check text-primary-500 text-xs"></i>{{ trim($benefit) }}
                        </li>
                        @endforeach
                    </ul>
                    @auth
                        <a href="{{ route('members.create') }}" class="block w-full py-3 text-center rounded-xl font-semibold text-sm transition {{ $package->duration_days >= 180 ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white hover:shadow-lg hover:shadow-primary-500/30' : 'bg-dark-700 text-dark-200 hover:bg-dark-600' }}">
                            Pilih Paket
                        </a>
                    @else
                        <a href="{{ route('login') }}" class="block w-full py-3 text-center rounded-xl font-semibold text-sm transition {{ $package->duration_days >= 180 ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white hover:shadow-lg hover:shadow-primary-500/30' : 'bg-dark-700 text-dark-200 hover:bg-dark-600' }}">
                            Pilih Paket
                        </a>
                    @endauth
                </div>
                @endforeach
            </div>
        </div>
    </section>

    {{-- ===== CLASSES ===== --}}
    <section id="classes" class="py-20 bg-dark-950">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <span class="inline-block px-10 py-3 bg-danger-500/10 text-danger-400 text-sm font-semibold rounded-full mb-4">KELAS KAMI</span>
                <h2 class="font-heading font-black text-4xl lg:text-5xl text-white mb-4">Kelas Fitness Terbaik</h2>
                <p class="text-dark-400 text-lg max-w-2xl mx-auto">Dipandu oleh trainer bersertifikat untuk hasil maksimal</p>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
                @php
                    $classIcons = ['Yoga' => 'fa-spa', 'HIIT' => 'fa-fire-flame-curved', 'Zumba' => 'fa-music', 'Body Combat' => 'fa-hand-fist', 'CrossFit' => 'fa-person-running', 'Pilates' => 'fa-child-reaching', 'Spinning' => 'fa-bicycle', 'Muay Thai' => 'fa-mitten'];
                    $classColors = ['from-blue-500 to-blue-600', 'from-red-500 to-orange-500', 'from-pink-500 to-purple-500', 'from-yellow-500 to-red-500', 'from-green-500 to-teal-500', 'from-indigo-500 to-purple-500', 'from-cyan-500 to-blue-500', 'from-orange-500 to-red-600'];
                @endphp
                @foreach($classes as $i => $class)
                <div class="card-hover bg-dark-800 border border-dark-700 rounded-2xl p-6 group">
                    <div class="w-14 h-14 rounded-2xl bg-gradient-to-br {{ $classColors[$i % count($classColors)] }} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fas {{ $classIcons[$class->name] ?? 'fa-dumbbell' }} text-white text-xl"></i>
                    </div>
                    <h3 class="font-heading font-bold text-lg text-white mb-2">{{ $class->name }}</h3>
                    <p class="text-dark-400 text-sm leading-relaxed mb-4">{{ Str::limit($class->description, 80) }}</p>
                    <div class="flex items-center gap-4 text-xs text-dark-500">
                        <span><i class="fas fa-clock mr-1"></i> {{ $class->duration_minutes }} menit</span>
                        <span><i class="fas fa-signal mr-1"></i> {{ $class->difficulty }}</span>
                    </div>
                </div>
                @endforeach
            </div>
        </div>
    </section>

    {{-- ===== TRAINERS ===== --}}
    <section id="trainers" class="py-20 bg-dark-900">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <span class="inline-block px-10 py-3 bg-gold-400/10 text-gold-400 text-sm font-semibold rounded-full mb-4">TRAINER KAMI</span>
                <h2 class="font-heading font-black text-4xl lg:text-5xl text-white mb-4">Trainer Berpengalaman</h2>
                <p class="text-dark-400 text-lg max-w-2xl mx-auto">Bimbingan profesional untuk pencapaian fitness terbaikmu</p>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
                @foreach($trainers as $trainer)
                <div class="card-hover bg-dark-800 border border-dark-700 rounded-2xl overflow-hidden">
                    <div class="h-2 bg-gradient-to-r from-primary-500 to-danger-500"></div>
                    <div class="p-6 text-center">
                        <div class="w-24 h-24 mx-auto rounded-full overflow-hidden mb-4 shadow-lg ring-2 ring-primary-500/30">
                            <img src="{{ asset('images/logo_gym.png') }}" alt="{{ $trainer->user->name ?? 'Trainer' }}" class="w-full h-full object-cover">
                        </div>
                        <h3 class="font-heading font-bold text-xl text-white">{{ $trainer->user->name ?? 'Trainer' }}</h3>
                        <p class="text-primary-400 text-sm font-medium mb-3">{{ $trainer->specialization }}</p>
                        <p class="text-dark-400 text-sm mb-4">{{ $trainer->certification }}</p>
                        <div class="flex justify-center gap-4 text-sm text-dark-500">
                            <span><i class="fas fa-star text-gold-400"></i> {{ $trainer->experience_years ?? 3 }} Tahun</span>
                            <span><i class="fas fa-money-bill text-green-400"></i> Rp {{ number_format($trainer->hourly_rate / 1000, 0) }}K/jam</span>
                        </div>
                    </div>
                </div>
                @endforeach
            </div>
        </div>
    </section>

    {{-- ===== CTA ===== --}}
    <section class="py-15 bg-gradient-to-r from-orange-500 via-orange-600 to-blue-900 relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-0 left-0 w-40 h-40 bg-white rounded-full blur-3xl"></div>
            <div class="absolute bottom-0 right-0 w-60 h-60 bg-white rounded-full blur-3xl"></div>
        </div>
        <div class="max-w-4xl mx-auto px-4 text-center relative z-10">
            <h2 class="font-heading font-black text-4xl lg:text-5xl text-white mb-6">Siap Untuk Berubah?</h2>
            <p class="text-white/80 text-lg mb-8 max-w-2xl mx-auto">Mulai perjalanan fitnessmu hari ini. Daftar sekarang dan dapatkan diskon special untuk member baru!</p>
            @auth
                <a href="{{ route('members.create') }}" class="inline-block px-10 py-4 bg-dark-900 text-white font-bold rounded-2xl text-lg hover:bg-dark-800 transition transform hover:-translate-y-1 shadow-2xl">
                    <i class="fas fa-user-plus mr-2"></i> Daftar Member Baru
                </a>
            @else
                <a href="{{ route('login') }}" class="inline-block px-10 py-4 bg-dark-900 text-white font-bold rounded-2xl text-lg hover:bg-dark-800 transition transform hover:-translate-y-1 shadow-2xl">
                    <i class="fas fa-arrow-right mr-2"></i> Mulai Sekarang
                </a>
            @endauth
        </div>
    </section>

    {{-- ===== FOOTER ===== --}}
    <footer class="bg-dark-950 border-t border-dark-800 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-3 gap-8">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <img src="{{ asset('images/logo_gym.png') }}" alt="Logo" class="w-10 h-10 rounded-full object-cover ring-2 ring-primary-500">
                        <div>
                            <h3 class="font-heading font-bold text-white">MDHP GYM</h3>
                            <p class="text-xs text-primary-400">Your Fitness Partner</p>
                        </div>
                    </div>
                    <p class="text-dark-400 text-sm leading-relaxed">Tempat fitness terbaik untuk transformasi tubuh dan kesehatanmu. Kesehatan itu mahal.</p>
                </div>
                <div>
                    <h4 class="font-heading font-bold text-white mb-4">Jam Operasional</h4>
                    <ul class="space-y-2 text-sm text-dark-400">
                        <li><i class="fas fa-clock text-primary-500 w-5"></i> Setiap Hari 24 Jam</li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-heading font-bold text-white mb-4">Kontak</h4>
                    <ul class="space-y-2 text-sm text-dark-400">
                        <li><i class="fas fa-map-marker-alt text-primary-500 w-5"></i> Jl. Malang Kota No. 11, Malang</li>
                        <li><i class="fas fa-phone text-primary-500 w-5"></i> +62 812-3456-7890</li>
                        <li><i class="fas fa-envelope text-primary-500 w-5"></i> info@mdhpgym.com</li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-dark-800 mt-8 pt-8 text-center">
                <p class="text-dark-500 text-sm">&copy; {{ date('Y') }} MDHP GYM. All rights reserved.</p>
            </div>
        </div>
    </footer>

</body>
</html>
