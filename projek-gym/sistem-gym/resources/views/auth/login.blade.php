<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - MDHP GYM</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        .hero-gradient { background: linear-gradient(135deg, #111827 0%, #1f2937 50%, #111827 100%); }
        .glow-effect { box-shadow: 0 0 40px rgba(249, 115, 22, 0.2); }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
        .float-animation { animation: float 4s ease-in-out infinite; }
    </style>
</head>
<body class="hero-gradient min-h-screen flex items-center justify-center relative overflow-hidden font-sans">
    
    {{-- Background Effects --}}
    <div class="absolute inset-0 opacity-10">
        <div class="absolute top-20 left-10 w-96 h-96 bg-primary-500 rounded-full blur-3xl"></div>
        <div class="absolute bottom-20 right-10 w-96 h-96 bg-danger-500 rounded-full blur-3xl"></div>
    </div>

    {{-- Back to Home --}}
    <a href="{{ route('home') }}" class="absolute top-6 left-6 text-dark-400 hover:text-primary-400 transition z-10">
        <i class="fas fa-arrow-left mr-2"></i> Kembali ke Home
    </a>

    {{-- Login Container --}}
    <div class="relative z-10 w-full max-w-md mx-auto px-4">
        
        {{-- Logo & Title --}}
        <div class="text-center mb-8">
            <div class="flex justify-center mb-4 float-animation">
                <img src="{{ asset('images/logo_gym.png') }}" alt="Logo" class="w-20 h-20 rounded-full object-cover ring-4 ring-primary-500/50 glow-effect">
            </div>
            <h1 class="font-heading font-black text-4xl mb-2">
                <span class="bg-gradient-to-r from-primary-400 to-danger-400 bg-clip-text text-transparent">MDHP GYM</span>
            </h1>
            <p class="text-dark-400 text-sm">Masuk ke akun Anda</p>
        </div>

        {{-- Login Card --}}
        <div class="bg-dark-800/80 backdrop-blur-xl border border-dark-700 rounded-3xl p-8 shadow-2xl">
            
            {{-- Success Message --}}
            @if(session('success'))
            <div class="mb-6 p-4 bg-green-500/10 border border-green-500/30 rounded-xl text-green-400 text-sm">
                <i class="fas fa-check-circle mr-2"></i> {{ session('success') }}
            </div>
            @endif

            {{-- Error Messages --}}
            @if($errors->any())
            <div class="mb-6 p-4 bg-danger-500/10 border border-danger-500/30 rounded-xl text-danger-400 text-sm">
                <i class="fas fa-exclamation-circle mr-2"></i>
                @foreach($errors->all() as $error)
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
                    <input 
                        type="email" 
                        name="email" 
                        id="email" 
                        value="{{ old('email') }}"
                        required
                        autofocus
                        class="w-full px-4 py-3 bg-dark-900 border border-dark-600 rounded-xl text-white placeholder-dark-500 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 transition outline-none"
                        placeholder="nama@email.com"
                    >
                </div>

                {{-- Password --}}
                <div>
                    <label for="password" class="block text-sm font-medium text-dark-300 mb-2">
                        <i class="fas fa-lock mr-2 text-primary-400"></i> Password
                    </label>
                    <div class="relative">
                        <input 
                            type="password" 
                            name="password" 
                            id="password" 
                            required
                            class="w-full px-4 py-3 pr-12 bg-dark-900 border border-dark-600 rounded-xl text-white placeholder-dark-500 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 transition outline-none"
                            placeholder="••••••••"
                        >
                        <button 
                            type="button"
                            id="togglePassword"
                            class="absolute right-3 top-1/2 -translate-y-1/2 text-dark-400 hover:text-primary-400 transition-colors focus:outline-none"
                        >
                            <i id="passwordIcon" class="fas fa-eye"></i>
                        </button>
                    </div>
                </div>

                {{-- Remember Me --}}
                <div class="flex items-center justify-between">
                    <label class="flex items-center cursor-pointer">
                        <input 
                            type="checkbox" 
                            name="remember" 
                            class="w-4 h-4 text-primary-500 bg-dark-900 border-dark-600 rounded focus:ring-primary-500/20"
                        >
                        <span class="ml-2 text-sm text-dark-400">Ingat saya</span>
                    </label>
                </div>

                {{-- Submit Button --}}
                <button 
                    type="submit" 
                    class="w-full py-3.5 bg-gradient-to-r from-primary-500 to-danger-500 text-white font-bold rounded-xl hover:shadow-lg hover:shadow-primary-500/30 transition-all transform hover:-translate-y-0.5 text-sm"
                >
                    <i class="fas fa-sign-in-alt mr-2"></i> Masuk
                </button>
            </form>
        </div>

        {{-- Footer --}}
        <div class="text-center mt-6">
            <p class="text-dark-500 text-xs">
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
