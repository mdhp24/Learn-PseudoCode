<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - MDHP GYM</title>

    @vite(['resources/css/app.css', 'resources/js/app.js'])

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>

<body class="hero-gradient min-h-screen flex items-center justify-center relative overflow-hidden font-sans">


    {{-- Back to Home --}}
    <a href="{{ route('home') }}" class="back-btn absolute top-6 left-6 z-20 group">
        <div
            class="flex items-center gap-2 px-4 py-2.5 bg-dark-800/80 backdrop-blur-md border border-dark-600/50 rounded-xl hover:bg-gradient-to-r hover:from-primary-500/20 hover:to-danger-500/20 hover:border-primary-500/50 transition-all duration-300 shadow-lg hover:shadow-primary-500/20">
            <div class="bg-primary-500/20 p-2 rounded-lg group-hover:bg-primary-500/30 transition-all">
                <i class="fas fa-arrow-left text-primary-400 text-sm"></i>
            </div>
            <span class="text-dark-300 group-hover:text-white font-medium text-sm">Kembali ke Home</span>
        </div>
    </a>

    {{-- Login Container --}}
    <div class="relative z-10 w-full max-w-md mx-auto px-4">

        {{-- Gym Motivation Banner --}}
        <div
            class="mb-6 bg-gradient-to-r from-primary-500/20 to-danger-500/20 backdrop-blur-sm border border-primary-500/30 rounded-2xl p-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="bg-primary-500/20 p-3 rounded-xl">
                        <i class="fas fa-dumbbell text-primary-400 text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-white font-bold text-sm">Transform Your Body</h3>
                        <p class="text-dark-400 text-xs">Start your fitness journey today</p>
                    </div>
                </div>
                <div class="text-right">
                    <div class="flex items-center gap-1 text-primary-400">
                        <i class="fas fa-fire text-xl"></i>
                        <span class="font-bold text-lg">24/7</span>
                    </div>
                </div>
            </div>
        </div>

        {{-- Logo & Title --}}
        <div class="text-center mb-8">
            <div class="flex justify-center mb-4">
                <img src="{{ asset('images/logo_gym.png') }}" alt="Logo"
                    class="w-28 h-28 rounded-full object-cover ring-4 ring-primary-500/50 glow-effect logo-hover">
            </div>
            <h1 class="font-heading font-black text-4xl mb-3">
                <span class="bg-gradient-to-r from-primary-400 to-danger-400 bg-clip-text text-transparent">MDHP
                    GYM</span>
            </h1>
            <div class="flex items-center justify-center gap-2 text-dark-300">
                <div class="h-px w-8 bg-gradient-to-r from-transparent to-primary-500/50"></div>
                <p class="text-sm font-medium tracking-wide">Login</p>
                <div class="h-px w-8 bg-gradient-to-l from-transparent to-primary-500/50"></div>
            </div>
        </div>

        {{-- Login Card --}}
        <div class="card-glow backdrop-blur-xl rounded-3xl p-8">
            <div class="card-content">
                {{-- Success Message --}}
                @if (session('success'))
                    <div class="mb-6 p-4 bg-green-500/10 border border-green-500/30 rounded-xl text-green-400 text-sm">
                        <i class="fas fa-check-circle mr-2"></i> {{ session('success') }}
                    </div>
                @endif

                {{-- Error Messages --}}
                @if ($errors->any())
                    <div
                        class="mb-6 p-4 bg-danger-500/10 border border-danger-500/30 rounded-xl text-danger-400 text-sm">
                        <i class="fas fa-exclamation-circle mr-2"></i>
                        @foreach ($errors->all() as $error)
                            {{ $error }}
                        @endforeach
                    </div>
                @endif
                <i class="fas fa-dumbbell gym-icon gym-icon-rotate text-7xl top-20 left-20"></i>
                <i class="fas fa-weight-hanging gym-icon gym-icon-swing text-6xl bottom-32 right-16"></i>
                <i class="fas fa-fire gym-icon gym-icon-pulse text-8xl top-40 right-32"></i>

                {{-- Login Form --}}
                <form action="{{ route('login') }}" method="POST" class="space-y-5">
                    @csrf
                    {{-- <button type="submit" id="loginBtn"
                        class="w-full py-3.5 bg-gradient-to-r from-primary-500 to-danger-500 text-white font-bold rounded-xl">
                        <span id="loginText">
                            <i class="fas fa-sign-in-alt mr-2"></i> Masuk
                        </span>
                        <span id="loadingText" class="hidden">
                            <i class="fas fa-spinner fa-spin mr-2"></i> Memproses...
                        </span>
                        <script>
                            document.querySelector("form").addEventListener("submit", function() {
                                document.getElementById("loginText").classList.add("hidden");
                                document.getElementById("loadingText").classList.remove("hidden");
                            });
                            passwordInput.addEventListener("keyup", function(event) {
                                const warning = document.getElementById("capsWarning");

                                if (event.getModifierState("CapsLock")) {
                                    warning.classList.remove("hidden");
                                } else {
                                    warning.classList.add("hidden");
                                }
                            });
                        </script>
                    </button> --}}


                    {{-- Email --}}
                    <div>
                        <label for="email" class="block text-sm font-medium text-dark-300 mb-2">
                            <i class="fas fa-envelope mr-2 text-primary-400"></i> Email
                        </label>
                        <input type="email" name="email" id="email" value="{{ old('email') }}" required
                            autofocus
                            class="w-full px-4 py-3 pr-12 bg-dark-900 border border-dark-600 rounded-xl text-white placeholder-dark-500 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 transition outline-none"
                            placeholder="nama@email.com">
                        @error('email')
                            <p class="text-danger-400 text-xs mt-1">{{ $message }}</p>
                        @enderror
                        {{-- <input type="email" name="email" autocomplete="email"> --}}
                    </div>

                    {{-- Password --}}
                    <div>
                        <label for="password" class="block text-sm font-medium text-dark-300 mb-2">
                            <i class="fas fa-lock mr-2 text-primary-400"></i> Password
                        </label>
                        <div class="relative">
                            <input type="password" name="password" id="password" required
                                class="w-full px-4 py-3 pr-12 bg-dark-900 border border-dark-600 rounded-xl text-white placeholder-dark-500 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 transition outline-none"
                                placeholder="••••••••">
                            <button type="button" id="togglePassword"
                                class="absolute right-3 top-1/2 -translate-y-1/2 text-dark-400 hover:text-primary-400 transition-colors focus:outline-none">
                                <i id="passwordIcon" class="fas fa-eye"></i>
                            </button>
                        </div>
                        @error('password')
                            <p class="text-danger-400 text-xs mt-1">{{ $message }}</p>
                        @enderror
                        <p id="capsWarning" class="text-yellow-400 text-xs mt-1 hidden">
                            Caps Lock sedang aktif
                        </p>
                        {{-- <input type="password" name="password" autocomplete="current-password"> --}}
                    </div>

                    {{-- Remember Me --}}
                    <div class="flex items-center justify-between">
                        <label class="flex items-center cursor-pointer">
                            <input type="checkbox" name="remember"
                                class="w-4 h-4 text-primary-500 bg-dark-900 border-dark-600 rounded focus:ring-primary-500/20">
                            <span class="ml-2 text-sm text-dark-400">Ingat saya</span>
                        </label>
                    </div>

                    {{-- Submit Button --}}
                    <button type="submit"
                        class="w-full py-3.5 bg-gradient-to-r from-primary-500 to-danger-500 text-white font-bold rounded-xl hover:shadow-lg hover:shadow-primary-500/30 transition-all transform hover:-translate-y-0.5 text-sm">
                        <i class="fas fa-sign-in-alt mr-2"></i> Masuk
                    </button>
                </form>
            </div>
        </div>

        {{-- Gym Features --}}
        <div class="mt-6 grid grid-cols-3 gap-3">
            <div class="bg-dark-800/50 backdrop-blur-sm border border-dark-700 rounded-xl p-3 text-center">
                <i class="fas fa-users text-primary-400 text-xl mb-1"></i>
                <p class="text-dark-300 text-xs font-medium">Expert Trainers</p>
            </div>
            <div class="bg-dark-800/50 backdrop-blur-sm border border-dark-700 rounded-xl p-3 text-center">
                <i class="fas fa-clock text-primary-400 text-xl mb-1"></i>
                <p class="text-dark-300 text-xs font-medium">24/7 Access</p>
            </div>
            <div class="bg-dark-800/50 backdrop-blur-sm border border-dark-700 rounded-xl p-3 text-center">
                <i class="fas fa-weight text-primary-400 text-xl mb-1"></i>
                <p class="text-dark-300 text-xs font-medium">Modern Equipment</p>
            </div>
        </div>

        {{-- Footer --}}
        <div class="text-center mt-6">
            <p class="text-dark-400 text-xs">
                &copy; {{ date('Y') }} MDHP GYM. All rights reserved.
            </p>
        </div>
    </div>

    <script>
        // Toggle Password Visibility
        const togglePassword = document.getElementById('togglePassword');
        const passwordInput = document.getElementById('password');
        const passwordIcon = document.getElementById('passwordIcon');

        togglePassword.addEventListener('click', function() {
            // Toggle password type
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);

            // Toggle icon
            if (type === 'password') {
                passwordIcon.classList.remove('fa-eye-slash');
                passwordIcon.classList.add('fa-eye');
            } else {
                passwordIcon.classList.remove('fa-eye');
                passwordIcon.classList.add('fa-eye-slash');
            }
        });

        document.querySelector("form").addEventListener("submit", function() {
            document.getElementById("loginText").classList.add("hidden");
            document.getElementById("loadingText").classList.remove("hidden");
        });
    </script>



</body>

</html>
