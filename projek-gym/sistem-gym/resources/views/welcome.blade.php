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
    </nav>
</body>

</html>
