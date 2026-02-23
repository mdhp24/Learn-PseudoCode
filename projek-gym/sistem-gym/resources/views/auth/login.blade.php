<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - MDHP GYM</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>

<body class="bg-gray-950 min-h-screen flex items-center justify-center font-['Inter']">

    <div class="w-full max-w-md px-6">

        {{-- Logo --}}
        <div class="text-center mb-10">
            <img src="{{ asset('images/logo_gym.png') }}" 
                 class="w-14 h-14 mx-auto mb-4 object-cover rounded-xl">
            <h1 class="text-2xl font-semibold text-white tracking-tight">
                MDHP GYM
            </h1>
            <p class="text-sm text-gray-400 mt-1">
                Masuk ke dashboard
            </p>
        </div>

        {{-- Card --}}
        <div class="bg-gray-900 border border-gray-800 rounded-2xl p-8 shadow-xl">

            {{-- Success --}}
            @if(session('success'))
                <div class="mb-5 text-sm text-green-400 bg-green-500/10 border border-green-500/20 p-3 rounded-lg">
                    {{ session('success') }}
                </div>
            @endif

            {{-- Error --}}
            @if($errors->any())
                <div class="mb-5 text-sm text-red-400 bg-red-500/10 border border-red-500/20 p-3 rounded-lg">
                    {{ $errors->first() }}
                </div>
            @endif

            <form action="{{ route('login') }}" method="POST" class="space-y-5">
                @csrf

                {{-- Email --}}
                <div>
                    <label class="block text-sm text-gray-400 mb-2">
                        Email
                    </label>
                    <input type="email"
                           name="email"
                           value="{{ old('email') }}"
                           required
                           class="w-full bg-gray-950 border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:ring-2 focus:ring-white/10 focus:border-gray-600 transition"
                           placeholder="nama@email.com">
                </div>

                {{-- Password --}}
                <div>
                    <label class="block text-sm text-gray-400 mb-2">
                        Password
                    </label>
                    <input type="password"
                           name="password"
                           required
                           class="w-full bg-gray-950 border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:ring-2 focus:ring-white/10 focus:border-gray-600 transition"
                           placeholder="••••••••">
                </div>

                {{-- Remember --}}
                <div class="flex items-center justify-between text-sm">
                    <label class="flex items-center gap-2 text-gray-400">
                        <input type="checkbox"
                               name="remember"
                               class="bg-gray-800 border-gray-700 rounded">
                        Ingat saya
                    </label>
                </div>

                {{-- Button --}}
                <button type="submit"
                        class="w-full bg-white text-gray-900 font-medium py-3 rounded-lg hover:bg-gray-200 transition">
                    Masuk
                </button>

            </form>
        </div>

        {{-- Footer --}}
        <p class="text-center text-xs text-gray-600 mt-8">
            &copy; {{ date('Y') }} MDHP GYM
        </p>

    </div>

</body>
</html>