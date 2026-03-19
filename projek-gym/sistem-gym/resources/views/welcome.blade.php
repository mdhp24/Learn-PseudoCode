<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MDHP GYM</title>
    <link rel="icon" type="image/png" href="{{ asset('images/logo_gym.png') }}">
    @vite(['resources/css/app.css', 'resources/js/app.js'])
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>

<body class="bg-dark-950 text-white font-sans" x-data="{ mobileMenu: false }">

    {{-- ===== NAVBAR ===== --}}
    <nav class="fixed top-0 w-full z-50 bg-dark-900/80 backdrop-blur-xl border-b border-dark-700/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
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
                <div class="hidden md:flex items-center gap-8">
                    <a href="#home"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Beranda</a>
                    <a href="#packages"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Paket</a>
                    <a href="#classes"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Kelas</a>
                    <a href="#trainers"
                        class="text-sm font-medium text-dark-300 hover:text-primary-400 transition">Trainer</a>
                    @auth
                        <a href="{{ route('dashboard') }}"
                            class="px-6 py-2.5 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold rounded-full text-sm hover:shadow-lg hover:shadow-primary-500/30 transition-all">Dashboard</a>
                    @else
                        <a href="{{ route('login') }}"
                            class="px-6 py-2.5 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold rounded-full text-sm hover:shadow-lg hover:shadow-primary-500/30 transition-all">Login</a>
                    @endauth
                </div>
                <button @click="mobileMenu = !mobileMenu" class="md:hidden text-white">
                    <i class="fas fa-bars text-xl"></i>
                </button>
            </div>
        </div>
        {{-- Mobile Menu --}}
        <div x-show="mobileMenu" x-cloak x-transition
            class="md:hidden bg-dark-900 border-t border-dark-700 px-6 py-4 space-y-3">
            <a href="#home" class="block text-dark-300 hover:text-primary-400">Beranda</a>
            <a href="#packages" class="block text-dark-300 hover:text-primary-400">Paket</a>
            <a href="#classes" class="block text-dark-300 hover:text-primary-400">Kelas</a>
            <a href="#trainers" class="block text-dark-300 hover:text-primary-400">Trainer</a>
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
    <section id="home" class="hero-gradient min-h-screen flex items-center relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-20 left-10 w-72 h-72 bg-primary-500 rounded-full blur-3xl"></div>
            <div class="absolute bottom-20 right-10 w-96 h-96 bg-danger-500 rounded-full blur-3xl"></div>
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 relative z-10">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div>
                    <div
                        class="inline-flex items-center gap-2 px-4 py-1.5 bg-primary-500/10 border border-primary-500/30 rounded-full mb-6">
                        <span class="w-2 h-2 bg-primary-500 rounded-full animate-pulse"></span>
                        <span class="text-primary-400 text-sm font-medium">Open 24 Hours</span>
                    </div>
                    <h1 class="font-heading font-black text-5xl lg:text-7xl leading-tight mb-6">
                        <span class="bg-gradient-to-r from-primary-400 to-danger-400 bg-clip-text text-transparent">MDHP
                            GYM</span><br>
                        <span class="text-white text-4xl lg:text-5xl">Your Fitness Partner</span>
                    </h1>
                    <p class="text-dark-400 text-lg mb-8 max-w-lg leading-relaxed">
                        Transformasi tubuhmu dimulai di sini. Bergabunglah dengan ribuan member yang telah merasakan
                        perubahan nyata bersama MDHP GYM.
                    </p>
                    <div class="flex flex-wrap gap-4">
                        <a href="#packages"
                            class="px-8 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-bold rounded-2xl text-lg hover:shadow-2xl hover:shadow-primary-500/30 transition-all transform hover:-translate-y-1">
                            <i class="fas fa-fire mr-2"></i> Daftar Sekarang
                        </a>
                        <a href="#classes"
                            class="px-8 py-4 border-2 border-dark-600 text-white font-bold rounded-2xl text-lg hover:border-primary-500 hover:text-primary-400 transition-all">
                            <i class="fas fa-calendar-days mr-2"></i> Lihat Kelas
                        </a>
                    </div>
                    <div class="flex items-center gap-8 mt-10">
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">100+</p>
                            <p class="text-dark-500 text-sm">Member Aktif</p>
                        </div>
                        <div class="w-px h-12 bg-dark-700"></div>
                        <div class="text-center">
                            <p class="font-heading font-black text-3xl text-primary-400">15+</p>
                            <p class="text-dark-500 text-sm">Trainer Profesional</p>
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
                        <img src="{{ asset('images/logo_gym.png') }}" alt="MDHP GYM"
                            class="w-80 h-80 object-contain drop-shadow-2xl shine-animation">

                        <!-- Top Left Badge -->
                        <div
                            class="absolute -top-6 -left-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-primary-400 font-semibold text-sm"><i class="fas fa-users mr-1.5"></i>
                                Komunitas Aktif</p>
                        </div>

                        <!-- Top Right Badge -->
                        <div
                            class="absolute -top-6 -right-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-primary-400 font-semibold text-sm"><i class="fas fa-dumbbell mr-1.5"></i> 50+
                                Alat</p>
                        </div>

                        <!-- Bottom Left Badge -->
                        <div
                            class="absolute -bottom-6 -left-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-danger-400 font-semibold text-sm"><i class="fas fa-heart-pulse mr-1.5"></i>
                                Full AC</p>
                        </div>

                        <!-- Bottom Right Badge -->
                        <div
                            class="absolute -bottom-6 -right-8 bg-dark-800/95 backdrop-blur-sm border border-dark-700 rounded-xl px-3 py-2 shadow-xl">
                            <p class="text-success-400 font-semibold text-sm"><i class="fas fa-shield-alt mr-1.5"></i>
                                24/7 Keamanan</p>
                        </div>
                    </div>
                </div>
            </div>
    </section>

</body>

</html>
