<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - MDHP GYM</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        /* Animated Background Gradient */
        .hero-gradient {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 25%, #450a0a 50%, #1e1b4b 75%, #0f172a 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
        }

        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }

            50% {
                background-position: 100% 50%;
            }

            100% {
                background-position: 0% 50%;
            }
        }

        .glow-effect {
            box-shadow: 0 0 40px rgba(249, 115, 22, 0.2);
        }

        @keyframes float {

            0%,
            100% {
                transform: translateY(0);
            }

            50% {
                transform: translateY(-20px);
            }
        }

        .float-animation {
            animation: float 4s ease-in-out infinite;
        }

        /* Glowing Card Effect */
        .card-glow {
            position: relative;
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(17, 24, 39, 0.95));
            box-shadow:
                0 0 60px rgba(249, 115, 22, 0.3),
                0 0 100px rgba(239, 68, 68, 0.2),
                0 20px 60px rgba(0, 0, 0, 0.5);
        }

        .card-glow::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 1.5rem;
            padding: 2px;
            background: linear-gradient(135deg, #f97316, #ef4444, #f97316);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0.8;
            pointer-events: none;
        }

        .card-glow::after {
            content: '';
            position: absolute;
            inset: -2px;
            border-radius: 1.5rem;
            background: linear-gradient(135deg, #f97316, #ef4444);
            filter: blur(20px);
            opacity: 0.4;
            z-index: -1;
            pointer-events: none;
        }

        .card-content {
            position: relative;
            z-index: 1;
        }

        /* Gym Elements Animation */
        @keyframes rotate {
            from {
                transform: rotate(0deg);
            }

            to {
                transform: rotate(360deg);
            }
        }

        @keyframes swing {

            0%,
            100% {
                transform: rotate(-15deg);
            }

            50% {
                transform: rotate(15deg);
            }
        }

        @keyframes pulse-glow {

            0%,
            100% {
                opacity: 0.3;
                transform: scale(1);
            }

            50% {
                opacity: 0.6;
                transform: scale(1.1);
            }
        }

        .gym-icon {
            position: absolute;
            color: rgba(249, 115, 22, 0.15);
            pointer-events: none;
        }

        .gym-icon-rotate {
            animation: rotate 20s linear infinite;
        }

        .gym-icon-swing {
            animation: swing 3s ease-in-out infinite;
        }

        .gym-icon-pulse {
            animation: pulse-glow 4s ease-in-out infinite;
        }

        /* Back Button Hover Effect */
        .back-btn {
            transition: all 0.3s ease;
        }

        .back-btn:hover {
            transform: translateX(-5px);
        }

        .back-btn i {
            transition: transform 0.3s ease;
        }

        .back-btn:hover i {
            transform: translateX(-3px);
        }

        /* Logo Hover Effect */
        .logo-hover {
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
        }

        .logo-hover:hover {
            transform: scale(1.15);
            /* hanya zoom */
            box-shadow: 0 0 60px rgba(249, 115, 22, 0.6),
                0 0 100px rgba(239, 68, 68, 0.4);
        }
    </style>
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

                {{-- Login Form --}}
                <form action="{{ route('login') }}" method="POST" class="space-y-5">
                    @csrf

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
    </script>

</body>

</html>
