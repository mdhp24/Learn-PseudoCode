<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - MDHP GYM</title>

    {{-- Vite: compile asset CSS dan JS utama aplikasi --}}
    @vite(['resources/css/app.css', 'resources/js/app.js'])

    {{-- Google Fonts: Inter (weight 300–800) untuk tipografi konsisten --}}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap"
        rel="stylesheet">

    {{-- Font Awesome 6.5.1: ikon UI (mata, spinner, dll.) --}}
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>

{{-- Body: background gradient gelap, full-height, konten terpusat secara vertikal & horizontal --}}

<body
    class="bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 min-h-screen flex items-center justify-center font-sans">

    {{-- Wrapper: membatasi lebar maksimum form agar tetap proporsional di semua layar --}}
    <div class="w-full max-w-md px-4">

        <!-- Card -->
        {{-- Card: kontainer utama form login dengan efek glassmorphism --}}
        <div class="bg-slate-900/80 backdrop-blur-xl border border-slate-700 rounded-3xl p-8 shadow-xl">

            <!-- Header -->
            {{-- Menampilkan logo gym, nama aplikasi, dan subjudul --}}
            <div class="text-center mb-6">
                {{-- Logo gym: ditampilkan sebagai avatar bulat dengan ring oranye --}}
                <img src="{{ asset('images/logo_gym.png') }}"
                    class="w-24 h-24 mx-auto rounded-full ring-4 ring-orange-500/40 mb-4" />
                <h1 class="text-3xl font-bold text-white">MDHP GYM</h1>
                <p class="text-slate-400 text-sm">Masuk ke akun Anda</p>
            </div>

            {{-- ===== ALERT / NOTIFIKASI ===== --}}

            {{-- Pesan sukses (contoh: setelah logout atau registrasi berhasil) --}}
            @if (session('success'))
                <div class="mb-4 text-green-400 text-sm">{{ session('success') }}</div>
            @endif

            {{-- Pesan error validasi: menampilkan error pertama dari stack --}}
            @if ($errors->any())
                <div class="mb-4 text-red-400 text-sm">
                    {{ $errors->first() }}
                </div>
            @endif

            {{-- ===== FORM LOGIN ===== --}}
            {{--
                - method POST  : sesuai standar autentikasi Laravel
                - action       : diarahkan ke route bernama 'login'
                - autocomplete : diaktifkan agar browser dapat mengisi otomatis
            --}}
            <!-- Form -->
            <form method="POST" action="{{ route('login') }}" id="loginForm" class="space-y-5" autocomplete="on">
                @csrf {{-- Token CSRF: wajib ada untuk melindungi dari serangan Cross-Site Request Forgery --}}

                {{-- ----- Field: Email ----- --}}
                <div>
                    <label class="text-sm text-slate-300">Email</label>
                    <input type="email" name="email" value="{{ old('email') }}" required autofocus
                        autocomplete="email"
                        class="w-full mt-1 px-4 py-3 bg-slate-800 border border-slate-600 rounded-xl text-white focus:ring-2 focus:ring-orange-500 outline-none">
                </div>

                <!-- Password -->
                <div>
                    <label class="text-sm text-slate-300">Password</label>
                    <div class="relative mt-1">
                        <input type="password" name="password" id="password" required autocomplete="current-password"
                            class="w-full px-4 py-3 bg-slate-800 border border-slate-600 rounded-xl text-white focus:ring-2 focus:ring-orange-500 outline-none">

                        <button type="button" id="togglePassword"
                            class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400">
                            <i class="fas fa-eye"></i>
                        </button>
                    </div>
                    <p id="capsWarning" class="text-yellow-400 text-xs mt-1 hidden">Caps Lock aktif</p>
                </div>

                <!-- Remember -->
                <div class="flex items-center">
                    <input type="checkbox" name="remember" class="mr-2">
                    <span class="text-sm text-slate-400">Ingat saya</span>
                </div>

                <!-- Submit -->
                <button type="submit" id="submitBtn"
                    class="w-full py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:opacity-90 transition">
                    <span id="btnText">Masuk</span>
                    <span id="btnLoading" class="hidden">
                        <i class="fas fa-spinner fa-spin"></i> Loading...
                    </span>
                </button>
            </form>
        </div>

        <!-- Footer -->
        <p class="text-center text-xs text-slate-500 mt-6">© {{ date('Y') }} MDHP GYM</p>

    </div>

    <script>
        const form = document.getElementById('loginForm');
        const submitBtn = document.getElementById('submitBtn');
        const btnText = document.getElementById('btnText');
        const btnLoading = document.getElementById('btnLoading');
        const password = document.getElementById('password');
        const togglePassword = document.getElementById('togglePassword');
        const capsWarning = document.getElementById('capsWarning');

        // Submit handling
        form.addEventListener('submit', function() {
            submitBtn.disabled = true;
            btnText.classList.add('hidden');
            btnLoading.classList.remove('hidden');
        });

        // Toggle password
        togglePassword.addEventListener('click', function() {
            const type = password.type === 'password' ? 'text' : 'password';
            password.type = type;
        });

        // CapsLock detection
        password.addEventListener('keyup', function(e) {
            if (e.getModifierState('CapsLock')) {
                capsWarning.classList.remove('hidden');
            } else {
                capsWarning.classList.add('hidden');
            }
        });
    </script>

</body>

</html>
