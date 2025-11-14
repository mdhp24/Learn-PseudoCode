# Menentukan nilai berdasarkan input pengguna
# nilai = int(input("Masukkan nilai: "))
# if nilai >= 80:
#     print("Nilai Anda A")
# elif nilai >= 70:
#     print("Nilai Anda B")
# elif nilai >= 60:
#     print("Nilai Anda C")
# else:
#     print("Nilai Anda D")

# Menghitung rata-rata dari beberapa nilai yang dimasukkan pengguna
# jumlah = int(input("Masukkan jumlah nilai: "))
# total = 0

# for i in range(jumlah):
#     nilai = float(input(f"Nilai ke-{i+1}: "))
#     total += nilai
    
#     rata_rata = total / jumlah
#     print("Rata-rata nilai: ", rata_rata)

#Program kalkulator sederhana
# a = float(input("Masukkan angka pertama: "))
# b = float(input("Masukkan angka kedua: "))

# operasi = input("Masukkan operasi (+, -, *, /): ")

# if operasi == "+":
#     hasil = a + b
# elif operasi == "-":
#     hasil = a - b
# elif operasi == "*":
#     hasil = a * b
# elif operasi == "/":
#     hasil = a / b
# else:
#     hasil = None

# if hasil is not None:
#     print("Hasil: ", hasil)
# else:
#     print("Operasi tidak valid.")

# Deteksi bilangan ganjil atau genap
# angka = int(input("Masukkan angkanya bos: "))

# if angka % 2 == 0:
#     print("Angka ini genap cuy")
# else: 
#     print("Angka ini ganjil bro")

#Menampilkan deret Fibonacci
# n = int(input("Masukkan jumlah deret Fibonacci: "))
# a, b = 0, 1

# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# Menyimpan dan Menampilkan Data Mahasiswa (List + Dictionary)
# mahasiswa = []

# for i in range(3):  # Misalnya, kita akan memasukkan data untuk 3 mahasiswa
#     nama = input("Masukkan nama mahasiswa: ")
#     umur = int(input("Masukkan umur mahasiswa: "))
#     jurusan = input("Masukkan jurusan mahasiswa: ")
    
#     data_mahasiswa = {
#         "nama": nama,
#         "umur": umur,
#         "jurusan": jurusan
#     }
    
#     mahasiswa.append(data_mahasiswa)

# # Menampilkan Data Mahasiswa
# print("\nData Mahasiswa:")
# for mhs in mahasiswa:
#     print(f"Nama: {mhs['nama']}, Umur: {mhs['umur']}, Jurusan: {mhs['jurusan']}")

# Program deteksi lulus atau tidak lulus
# nilai = float(input("Masukkan nilai mahasiswa: "))

# if nilai >= 70:
#     status = "Lulus"
# else:
#     status = "Tidak Lulus"

# print("Status Mahasiswa:", status)

#Program kelas mahasiswa lulus atau tidak lulus
# class Mahasiswa:
#     def __init__(self, nama, nilai):
#         self.nama = nama
#         self.nilai = nilai

#     def status(self):
#         if self.nilai >= 70:
#             return "Lulus"
#         else:
#             return "Tidak Lulus"

# mhs1 = Mahasiswa("Dicky", 85)
# print(mhs1.nama, "-", mhs1.status())

# Program menghitung rata-rata nilai mahasiswa
# jumlah = int(input("Masukkan jumlah nilai: "))
# total = 0

# for i in range(jumlah):
#     nilai = float(input(f"Nilai ke-{i+1}: "))
#     total += nilai

# rata = total / jumlah
# print("Rata-rata nilai:", rata)


# Program membaca dan menulis file CSV
# import csv

# with open("nilai.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Nama", "Nilai"])
#     writer.writerow(["Dicky", 85])
#     writer.writerow(["Rina", 90])
#     writer.writerow(["Adi", 65])

# total, count = 0, 0
# with open("nilai.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         total += int(row["Nilai"])
#         count += 1

# print("Rata-rata nilai:", total / count)

# Program menentukan kategori performa mahasiswa
# nilai = float(input("Masukkan nilai mahasiswa: "))

# if nilai < 60:
#     kategori = "Struggling"
# elif nilai < 75:
#     kategori = "Normal"
# else:
#     kategori = "Ideal"

# print("Kategori performa:", kategori)

# Program kelas untuk menentukan kategori performa mahasiswa
# class PerformaMahasiswa:
#     def __init__(self, nama, skor):
#         self.nama = nama
#         self.skor = skor

#     def deteksi(self):
#         if self.skor < 50:
#             return "Struggling"
#         elif self.skor < 70:
#             return "Gaming the System"
#         elif self.skor < 85:
#             return "Normal"
#         else:
#             return "Ideal"

# mhs = PerformaMahasiswa("Zyncron", 78)
# print(mhs.nama, "berada pada kategori:", mhs.deteksi())

# Program menggunakan list comprehension untuk memfilter nilai lulus
# nilai = [45, 67, 88, 92, 55, 73]
# lulus = [n for n in nilai if n >= 70]
# print("Nilai yang lulus:", lulus)


# Program chatbot sederhana
# def chatbot(respon):
#     if "array" in respon.lower():
#         return "Array adalah struktur data untuk menyimpan sekumpulan elemen dengan tipe data yang sama."
#     elif "loop" in respon.lower():
#         return "Loop digunakan untuk melakukan perulangan dalam program."
#     else:
#         return "Saya tidak mengerti, bisa jelaskan lebih spesifik?"

# while True:
#     tanya = input("Kamu: ")
#     if tanya.lower() == "exit":
#         break
#     print("Bot:", chatbot(tanya))


# Program untuk menghitung jumlah kata dalam sebuah kalimat
# kalimat = input("Masukkan sebuah kalimat: ")
# jumlah_kata = len(kalimat.split())
# print("Jumlah kata dalam kalimat:", jumlah_kata)

# Program untuk memeriksa apakah sebuah kata adalah palindrom
# kata = input("Masukkan sebuah kata: ")
# if kata == kata[::-1]:
#     print(f"{kata} adalah palindrom")
# else:
#     print(f"{kata} bukan palindrom")
    
# Program untuk mengonversi suhu dari Celsius ke Fahrenheit
# celsius = float(input("Masukkan suhu dalam Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Suhu dalam Fahrenheit: {fahrenheit}")

# Program untuk menghitung faktorial dari sebuah angka
# def faktorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial(n - 1)
# angka = int(input("Masukkan sebuah angka: "))
# print(f"Faktorial dari {angka} adalah {faktorial(angka)}")

# Program untuk menampilkan bilangan prima dalam rentang tertentu
# def is_prima(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# start = int(input("Masukkan angka awal: "))
# end = int(input("Masukkan angka akhir: "))
# print(f"Bilangan prima antara {start} dan {end}:")
# for n in range(start, end + 1):
#     if is_prima(n):
#         print(n, end=' ')
#         print()
        
# Program untuk mengurutkan daftar angka
# angka = [34, 12, 5, 67, 23, 89, 1]
# angka.sort()
# print("Daftar angka yang diurutkan:", angka)


# Program untuk mencari nilai maksimum dan minimum dalam sebuah daftar
# angka = [34, 12, 5, 67, 23, 89, 1]
# maksimum = max(angka)
# minimum = min(angka)
# print(f"Nilai maksimum: {maksimum}")
# print(f"Nilai minimum: {minimum}")

# Program untuk menghitung jumlah digit dalam sebuah angka
# angka = input("Masukkan sebuah angka: ")
# jumlah_digit = len(angka)
# print("Jumlah digit dalam angka:", jumlah_digit)

# Program untuk memeriksa apakah sebuah tahun adalah tahun kabisat
# tahun = int(input("Masukkan sebuah tahun: "))
# if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     print(f"{tahun} adalah tahun kabisat")
# else:
#     print(f"{tahun} bukan tahun kabisat")

# Program untuk menghitung luas lingkaran
# import math
# radius = float(input("Masukkan jari-jari lingkaran: "))
# luas = math.pi * radius ** 2
# print(f"Luas lingkaran dengan jari-jari {radius} adalah {luas}")

# Program untuk menghitung luas segitiga
# alas = float(input("Masukkan alas segitiga: "))
# tinggi = float(input("Masukkan tinggi segitiga: "))
# luas = 0.5 * alas * tinggi
# print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")


# Program untuk mengonversi bilangan desimal ke biner
# desimal = int(input("Masukkan bilangan desimal: "))
# biner = bin(desimal).replace("0b", "")
# print(f"Bilangan biner dari {desimal} adalah {biner}")


# Program untuk mengonversi bilangan biner ke desimal
# biner = input("Masukkan bilangan biner: ")
# desimal = int(biner, 2)
# print(f"Bilangan desimal dari {biner} adalah {desimal}")

# Program untuk menghitung jumlah huruf vokal dalam sebuah kalimat
# kalimat = input("Masukkan sebuah kalimat: ")
# vokal = "aeiouAEIOU"
# jumlah_vokal = sum(1 for char in kalimat if char in vokal)
# print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)

# Program untuk mencari nilai maksimum dan minimum dalam sebuah daftar tanpa menggunakan fungsi bawaan
# data = [23, 56, 12, 89, 34, 67]
# maks = data[0]
# minn = data[0]

# for i in data:
#     if i > maks:
#         maks = i
#     if i < minn:
#         minn = i

# print("Nilai maksimum:", maks)
# print("Nilai minimum:", minn)

# Program untuk menentukan kategori performa berdasarkan nilai dan waktu pengerjaan
# def prediksi_performa(nilai, waktu_pengerjaan):
#     if nilai < 60 and waktu_pengerjaan > 30:
#         return "Struggling"
#     elif nilai < 70:
#         return "Gaming the System"
#     elif nilai < 85:
#         return "Normal"
#     else:
#         return "Ideal"

# print(prediksi_performa(78, 20))

# Program untuk menampilkan deret Fibonacci hingga n angka
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Masukkan jumlah angka Fibonacci: "))
# for i in range(n):
#     print(fibonacci(i), end=" ")

# Program untuk menghitung rata-rata, nilai tertinggi, dan nilai terendah dari sebuah daftar nilai
# nilai = [70, 85, 60, 90, 75, 88, 92]

# rata = sum(nilai) / len(nilai)
# maks = max(nilai)
# minn = min(nilai)
# print("Rata-rata:", rata)
# print("Tertinggi:", maks)
# print("Terendah:", minn)

# Program chatbot edukasi sederhana
# class EduChatbot:
#     def __init__(self, nama):
#         self.nama = nama

#     def respon(self, pertanyaan):
#         if "array" in pertanyaan.lower():
#             return "Array adalah struktur data yang menyimpan banyak nilai dalam satu variabel."
#         elif "loop" in pertanyaan.lower():
#             return "Loop digunakan untuk perulangan di program."
#         else:
#             return "Saya tidak yakin, coba pertanyaan lain ya!"

# bot = EduChatbot("TutorAI")
# print(bot.respon("Apa itu array?"))

# Program menentukan kategori performa mahasiswa dengan nilai acak
# import random

# mahasiswa = ["Dicky", "Rina", "Adi", "Budi", "Tina"]
# for m in mahasiswa:
#     nilai = random.randint(40, 100)
#     if nilai < 60:
#         kategori = "Struggling"
#     elif nilai < 75:
#         kategori = "Gaming the System"
#     elif nilai < 90:
#         kategori = "Normal"
#     else:
#         kategori = "Ideal"
#     print(f"{m}: Nilai {nilai} → {kategori}")

# Program menentukan kategori performa mahasiswa berdasarkan nilai, waktu, dan percobaan
# def deteksi_kesulitan(nilai, waktu, percobaan):
#     if nilai < 50 or percobaan > 5:
#         return "Struggling"
#     elif nilai < 70:
#         return "Gaming the System"
#     elif nilai < 85:
#         return "Normal"
#     else:
#         return "Ideal"

# mahasiswa = [
#     {"nama": "Dicky", "nilai": 45, "waktu": 35, "percobaan": 6},
#     {"nama": "Tina", "nilai": 80, "waktu": 20, "percobaan": 2},
#     {"nama": "Rina", "nilai": 92, "waktu": 15, "percobaan": 1}
# ]

# for m in mahasiswa:
#     hasil = deteksi_kesulitan(m["nilai"], m["waktu"], m["percobaan"])
#     print(f"{m['nama']} → Kategori: {hasil}")

# Program menghasilkan data mahasiswa acak dan menampilkannya
# import random

# jurusan = ["TI", "RPL", "SI"]
# data_mahasiswa = []

# for i in range(10):
#     nama = f"Mahasiswa_{i+1}"
#     nilai = random.randint(40, 100)
#     waktu = random.randint(10, 40)
#     jur = random.choice(jurusan)
#     data_mahasiswa.append({"nama": nama, "jurusan": jur, "nilai": nilai, "waktu": waktu})

# for m in data_mahasiswa:
#     print(m)

# Program chatbot memberikan feedback berdasarkan nilai dan percobaan
# def chatbot_feedback(nilai, percobaan):
#     if nilai < 60 and percobaan > 3:
#         return "Kamu tampaknya kesulitan. Coba pelajari ulang konsep dasar materi ini."
#     elif nilai < 80:
#         return "Bagus! Tapi coba perkuat logika kodingmu."
#     else:
#         return "Hebat! Kamu berada di level ideal."

# mhs = [
#     {"nama": "Dicky", "nilai": 55, "percobaan": 5},
#     {"nama": "Rina", "nilai": 77, "percobaan": 2},
#     {"nama": "Adi", "nilai": 91, "percobaan": 1}
# ]

# for m in mhs:
#     print(f"{m['nama']} → {chatbot_feedback(m['nilai'], m['percobaan'])}")


# Program menentukan kategori performa berdasarkan daftar nilai
# nilai = [55, 68, 72, 84, 90, 45, 78]
# for n in nilai:
#     if n < 60:
#         kategori = "Struggling"
#     elif n < 75:
#         kategori = "Gaming the System"
#     elif n < 90:
#         kategori = "Normal"
#     else:
#         kategori = "Ideal"
#     print(f"Nilai {n} → {kategori}")

# Program untuk membandingkan kemiripan jawaban mahasiswa dengan jawaban benar
# from difflib import SequenceMatcher

# def similarity(jawaban1, jawaban2):
#     return SequenceMatcher(None, jawaban1, jawaban2).ratio()

# mhs_answer = "Array adalah kumpulan elemen dengan tipe data yang sama"
# correct_answer = "Array menyimpan beberapa elemen bertipe data sama"

# sim = similarity(mhs_answer.lower(), correct_answer.lower())
# print(f"Tingkat kemiripan jawaban: {sim*100:.2f}%")

# Program login sederhana dengan username dan password
# akun = {"admin": "12345", "user": "abcd"}

# username = input("Masukkan username: ")
# password = input("Masukkan password: ")

# if username in akun and akun[username] == password:
#     print("Login berhasil!")
# else:
#     print("Username atau password salah!")

# Program menghitung rata-rata nilai mahasiswa dan menentukan lulus atau remedial
# mahasiswa = {
#     "Dicky": [85, 90, 88],
#     "Rina": [70, 75, 72],
#     "Budi": [60, 65, 63]
# }

# for nama, nilai in mahasiswa.items():
#     rata = sum(nilai) / len(nilai)
#     status = "Lulus" if rata >= 70 else "Remedial"
#     print(f"{nama} → Rata-rata: {rata:.2f} → {status}")

# Program untuk memeriksa apakah sebuah angka adalah bilangan prima
# def is_prima(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# angka = int(input("Masukkan angka: "))
# print(f"{angka} adalah bilangan prima" if is_prima(angka) else f"{angka} bukan bilangan prima")

# Program untuk menghitung jumlah huruf vokal dan konsonan dalam sebuah kalimat
# kalimat = input("Masukkan sebuah kalimat: ")
# vokal = "aeiouAEIOU"
# jumlah_vokal = sum(1 for char in kalimat if char in vokal)
# jumlah_konsonan = sum(1 for char in kalimat if char.isalpha() and char not in vokal)
# print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)
# print("Jumlah huruf konsonan dalam kalimat:", jumlah_konsonan)


# Program untuk mengonversi bilangan desimal ke heksadesimal
# desimal = int(input("Masukkan bilangan desimal: "))
# heksadesimal = hex(desimal).replace("0x", "").upper()
# print(f"Bilangan heksadesimal dari {desimal} adalah {heksadesimal}")

# Program untuk mengonversi bilangan heksadesimal ke desimal
# heksadesimal = input("Masukkan bilangan heksadesimal: ")
# desimal = int(heksadesimal, 16)
# print(f"Bilangan desimal dari {heksadesimal} adalah {desimal}")

# Program untuk menghitung jumlah kata unik dalam sebuah kalimat
# kalimat = input("Masukkan sebuah kalimat: ")
# kata = kalimat.split()
# kata_unik = set(kata)
# print("Jumlah kata unik dalam kalimat:", len(kata_unik))

# Program untuk memeriksa apakah sebuah string adalah anagram
# def is_anagram(str1, str2):
#     return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())
# kata1 = input("Masukkan kata pertama: ")
# kata2 = input("Masukkan kata kedua: ")
# if is_anagram(kata1, kata2):
#     print(f"{kata1} dan {kata2} adalah anagram")
# else:
#     print(f"{kata1} dan {kata2} bukan anagram")

# Program untuk menghitung keliling dan luas persegi panjang
# panjang = float(input("Masukkan panjang persegi panjang: "))
# lebar = float(input("Masukkan lebar persegi panjang: "))
# keliling = 2 * (panjang + lebar)
# luas = panjang * lebar
# print(f"Keliling persegi panjang: {keliling}")
# print(f"Luas persegi panjang: {luas}")

# Program untuk menghitung jumlah digit ganjil dan genap dalam sebuah angka
# angka = input("Masukkan sebuah angka: ")
# jumlah_ganjil = sum(1 for digit in angka if int(digit) % 2 != 0)
# jumlah_genap = sum(1 for digit in angka if int(digit) % 2 == 0)
# print("Jumlah digit ganjil dalam angka:", jumlah_ganjil)
# print("Jumlah digit genap dalam angka:", jumlah_genap)

# program untuk menentukan apakah sebuah kata adalah palindrom atau bukan
# kata = input("Masukkan sebuah kata: ")
# if kata == kata[::-1]:
#     print(f"{kata} adalah palindrom")
# else:
#     print(f"{kata} bukan palindrom")

# Program untuk menghitung luas dan keliling lingkaran
# import math
# radius = float(input("Masukkan jari-jari lingkaran: "))
# luas = math.pi * radius ** 2
# keliling = 2 * math.pi * radius
# print(f"Luas lingkaran dengan jari-jari {radius} adalah {luas}")
# print(f"Keliling lingkaran dengan jari-jari {radius} adalah {keliling}")

# Program untuk menghitung jumlah huruf vokal dalam sebuah kalimat
# kalimat = input("Masukkan sebuah kalimat: ")
# vokal = "aeiouAEIOU"
# jumlah_vokal = sum(1 for char in kalimat if char in vokal)
# jumlah_konsonan = sum(1 for char in kalimat if char.isalpha() and char not in vokal)
# print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)
# print("Jumlah huruf konsonan dalam kalimat:", jumlah_konsonan)

# Program untuk memeriksa apakah sebuah tahun adalah tahun kabisat
# tahun = int(input("Masukkan sebuah tahun: "))
# if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     print(f"{tahun} adalah tahun kabisat")
# else:
#     print(f"{tahun} bukan tahun kabisat")

# Program untuk menghitung faktorial dari sebuah angka
# def faktorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial(n - 1)
# angka = int(input("Masukkan sebuah angka: "))
# print(f"Faktorial dari {angka} adalah {faktorial(angka)}")

# Program untuk menampilkan bilangan prima dalam rentang tertentu
# def is_prima(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# start = int(input("Masukkan angka awal: "))
# end = int(input("Masukkan angka akhir: "))
# print(f"Bilangan prima antara {start} dan {end}:")
# for n in range(start, end + 1):
#     if is_prima(n):
#         print(n, end=' ')
#         print()
#     else:
#         print("Bukan bilangan prima")

# Program untuk mengurutkan daftar angka
# angka = [34, 12, 5, 67, 23, 89, 1]
# angka.sort()
# print("Daftar angka setelah diurutkan:", angka)

# Sistem Rekomendasi Lomba Berdasarkan Nilai
# def rekomendasi_lomba(nilai_web, nilai_jaringan, nilai_ai):
#     if nilai_ai > nilai_web and nilai_ai > nilai_jaringan:
#         return "Rekomendasi: Lomba AI & Data Science"
#     elif nilai_web > nilai_ai and nilai_web > nilai_jaringan:
#         return "Rekomendasi: Lomba Web Programming"
#     elif nilai_jaringan > nilai_ai:
#         return "Rekomendasi: Lomba Jaringan Komputer"
#     else:
#         return "Rekomendasi: Lomba Umum"

# hasil = rekomendasi_lomba(78, 65, 92)
# print(hasil)

# Sistem Deteksi Performa Mahasiswa Berdasarkan Waktu dan Percobaan
# def deteksi_performa(nilai, waktu, percobaan):
#     if nilai < 50 or percobaan > 5:
#         return "Struggling"
#     elif nilai < 70:
#         return "Gaming the System"
#     elif nilai < 85:
#         return "Normal"
#     else:
#         return "Ideal"

# print(deteksi_performa(68, 25, 4))

# Analisis Statistik Nilai Otomatis
# nilai = [78, 85, 67, 90, 88, 74, 56, 80]
# rata = sum(nilai) / len(nilai)
# maks = max(nilai)
# minn = min(nilai)

# print(f"Rata-rata: {rata:.2f}")
# print(f"Nilai Tertinggi: {maks}")
# print(f"Nilai Terendah: {minn}")

#Sistem Chatbot Adaptif
# def chatbot_input(pesan):
#     pesan = pesan.lower()
#     if "array" in pesan:
#         return "Array adalah struktur data untuk menyimpan elemen dengan tipe data sama."
#     elif "loop" in pesan:
#         return "Loop digunakan untuk mengulang perintah."
#     elif "if" in pesan:
#         return "If adalah kondisi logika untuk pengambilan keputusan."
#     else:
#         return "Maaf, saya belum memahami topik itu."

# while True:
#     teks = input("Kamu: ")
#     if teks.lower() == "keluar":
#         break
#     print("Bot:", chatbot_input(teks))

# sistem konversi desimal ke biner 
# def konversi_biner(angka):
#     biner = ""
#     while angka > 0:
#         biner = str(angka % 2) + biner
#         angka //= 2
#     return biner

# angka = int(input("Masukkan angka desimal: "))
# print("Biner:", konversi_biner(angka))

#Simulasi Dataset & Klasifikasi Manual
# import random

# def klasifikasi(nilai):
#     if nilai < 60:
#         return "Struggling"
#     elif nilai < 75:
#         return "Gaming"
#     elif nilai < 90:
#         return "Normal"
#     else:
#         return "Ideal"

# data = []
# for i in range(10):
#     nilai = random.randint(40, 100)
#     data.append((f"Mahasiswa_{i+1}", nilai, klasifikasi(nilai)))

# for m in data:
#     print(f"{m[0]} → Nilai: {m[1]} → Kategori: {m[2]}")

# Menyimpan dan Menampilkan Data Mahasiswa (List + Dictionary)
# mahasiswa = []

# for i in range(3):
#     nama = input("Masukkan nama mahasiswa: ")
#     nilai = int(input("Masukkan nilai: "))
#     mahasiswa.append({"nama": nama, "nilai": nilai})

# print("\nData Mahasiswa:")
# for m in mahasiswa:
#     print(f"{m['nama']} - Nilai: {m['nilai']}")

# sistem rekomendasi lomba berdasarkan nilai
# def rekomendasi_lomba(nilai_web, nilai_jaringan, nilai_ai):
#     if nilai_ai > nilai_web and nilai_ai > nilai_jaringan:
#         return "Rekomendasi: Lomba AI & Data Science"
#     elif nilai_web > nilai_ai and nilai_web > nilai_jaringan:
#         return "Rekomendasi: Lomba Web Programming"
#     elif nilai_jaringan > nilai_ai:
#         return "Rekomendasi: Lomba Jaringan Komputer"
#     else:
#         return "Rekomendasi: Lomba Umum"
# hasil = rekomendasi_lomba(78, 65, 92)
# print(hasil)

# sistem deteksi performa mahasiswa berdasarkan waktu dan percobaan
# def deteksi_performa(nilai, waktu, percobaan):
#     if nilai < 50 or percobaan > 5:
#         return "Struggling"
#     elif nilai < 70:
#         return "Gaming the System"
#     elif nilai < 85:
#         return "Normal"
#     else:
#         return "Ideal"
# print(deteksi_performa(68, 25, 4))

# sistem analisis statistik nilai otomatis
# nilai = [78, 85, 67, 90, 88, 74, 56, 80]
# rata = sum(nilai) / len(nilai)
# maks = max(nilai)
# minn = min(nilai)
# print(f"Rata-rata: {rata:.2f}")
# print(f"Nilai Tertinggi: {maks}")
# print(f"Nilai Terendah: {minn}")


# sistem pembelian sederhana
# def pembelian_sederhana():
#     harga_barang = float(input("Masukkan harga barang: "))
#     jumlah_barang = int(input("Masukkan jumlah barang: "))
#     total_harga = harga_barang * jumlah_barang

#     print(f"Total harga sebelum diskon: {total_harga}")

#     if total_harga > 500000:
#         diskon = 0.1 * total_harga
#     elif total_harga > 200000:
#         diskon = 0.05 * total_harga
#     else:
#         diskon = 0

#     total_bayar = total_harga - diskon
#     print(f"Diskon: {diskon}")
#     print(f"Total yang harus dibayar: {total_bayar}")
# pembelian_sederhana()


# sistem penilaian ujian
# def penilaian_ujian():
#     nilai = float(input("Masukkan nilai ujian: "))

#     if nilai >= 85:
#         grade = "A"
#     elif nilai >= 70:
#         grade = "B"
#     elif nilai >= 55:
#         grade = "C"
#     elif nilai >= 40:
#         grade = "D"
#     else:
#         grade = "E"

#     print(f"Grade Anda: {grade}")
# penilaian_ujian()

# sistem rekomendasi film
# def rekomendasi_film(genre):
#     if genre.lower() == "aksi":
#         return "Rekomendasi: Avengers, John Wick"
#     elif genre.lower() == "komedi":
#         return "Rekomendasi: The Hangover, Superbad"
#     elif genre.lower() == "drama":
#         return "Rekomendasi: The Shawshank Redemption, Forrest Gump"
#     else:
#         return "Rekomendasi: Film genre lain seperti horor atau sci-fi"
# genre_input = input("Masukkan genre film favorit Anda (aksi, komedi, drama): ")
# print(rekomendasi_film(genre_input))

# sistem deteksi kecepatan internet
# def deteksi_kecepatan(kecepatan):
#     if kecepatan < 5:
#         return "Kecepatan internet Anda lambat."
#     elif kecepatan < 20:
#         return "Kecepatan internet Anda sedang."
#     else:
#         return "Kecepatan internet Anda cepat."
# kecepatan_input = float(input("Masukkan kecepatan internet Anda (Mbps): "))
# print(deteksi_kecepatan(kecepatan_input))


# Sistem palidrom deteksi
# def is_palindrome(text):
#     text = text.replace(" ", "").lower()
#     return text == text[::-1]

# kata = input("Masukkan kata: ")
# if is_palindrome(kata):
#     print("✅ Kata ini palindrome!")
# else:
#     print("❌ Bukan palindrome.")


# KONVERSI DESIMAL KE BINNER, OKTAL, HEKSADESIMAL
# angka = int(input("Masukkan bilangan desimal: "))
# print(f"Biner: {bin(angka)[2:]}")
# print(f"Oktal: {oct(angka)[2:]}")
# print(f"Heksadesimal: {hex(angka)[2:].upper()}")

# Permainan Tebak Angka
# import random

# angka_rahasia = random.randint(1, 20)
# percobaan = 0

# while True:
#     tebakan = int(input("Tebak angka (1-20): "))
#     percobaan += 1
#     if tebakan < angka_rahasia:
#         print("Terlalu kecil!")
#     elif tebakan > angka_rahasia:
#         print("Terlalu besar!")
#     else:
#         print(f"🎉 Benar! Angka {angka_rahasia} ditemukan dalam {percobaan} percobaan.")
#         break

# Hitung Umur Berdasarkan Tahun Lahir
# from datetime import date

# tahun_lahir = int(input("Masukkan tahun lahir: "))
# tahun_sekarang = date.today().year
# umur = tahun_sekarang - tahun_lahir

# print(f"Umur kamu adalah {umur} tahun.")


# Sistem Pembelian Sederhana
# total = 0
# while True:
#     nama = input("Masukkan nama barang (atau 'selesai'): ")
#     if nama.lower() == "selesai":
#         break
#     harga = float(input("Masukkan harga barang: "))
#     total += harga

# print(f"Total belanja: Rp{total:,.2f}")


# Menampilkan Deret Fibonacci
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# n = int(input("Masukkan jumlah deret Fibonacci: "))
# fibonacci(n)

# Hitung Jumlah Huruf Vokal dan Konsonan
# teks = input("Masukkan teks: ").lower()
# vokal = "aiueo"
# jumlah_vokal = sum(1 for huruf in teks if huruf in vokal)
# jumlah_konsonan = sum(1 for huruf in teks if huruf.isalpha() and huruf not in vokal)

# print(f"Jumlah huruf vokal: {jumlah_vokal}")
# print(f"Jumlah huruf konsonan: {jumlah_konsonan}")

# Simulasi Dataset & Klasifikasi Manual
# import random

# mahasiswa = []
# for i in range(10):
#     nilai = random.randint(40, 100)
#     waktu = random.randint(10, 50)
#     kategori = (
#         "Struggling" if nilai < 60 else
#         "Gaming" if nilai < 75 else
#         "Normal" if nilai < 90 else
#         "Ideal"
#     )
#     mahasiswa.append({"nama": f"Mahasiswa_{i+1}", "nilai": nilai, "waktu": waktu, "kategori": kategori})

# for m in mahasiswa:
#     print(m)
    
# Sistem Rekomendasi Film
# def rekomendasi_film(genre):
#     if genre.lower() == "aksi":
#         return "Rekomendasi: Avengers, John Wick"
#     elif genre.lower() == "komedi":
#         return "Rekomendasi: The Hangover, Superbad"
#     elif genre.lower() == "drama":
#         return "Rekomendasi: The Shawshank Redemption, Forrest Gump"
#     else:
#         return "Rekomendasi: Film genre lain seperti horor atau sci-fi"
# genre_input = input("Masukkan genre film favorit Anda (aksi, komedi, drama): ")
# print(rekomendasi_film(genre_input))

# Sistem Deteksi Kecepatan Internet
# def deteksi_kecepatan(kecepatan):
#     if kecepatan < 5:
#         return "Kecepatan internet Anda lambat."
#     elif kecepatan < 20:
#         return "Kecepatan internet Anda sedang."
#     else:
#         return "Kecepatan internet Anda cepat."
# kecepatan_input = float(input("Masukkan kecepatan internet Anda (Mbps): "))
# print(deteksi_kecepatan(kecepatan_input))

# Sistem Penilaian Ujian
# def penilaian_ujian():
#     nilai = float(input("Masukkan nilai ujian: "))

#     if nilai >= 85:
#         grade = "A"
#     elif nilai >= 70:
#         grade = "B"
#     elif nilai >= 55:
#         grade = "C"
#     elif nilai >= 40:
#         grade = "D"
#     else:
#         grade = "E"

#     print(f"Grade Anda: {grade}")
# penilaian_ujian()


# Sistem conversi rupiah ke dollar
# def konversi_rupiah_ke_dollar(rupiah, kurs=15000):
#     dollar = rupiah / kurs
#     return dollar
# rupiah_input = float(input("Masukkan jumlah rupiah: "))
# dollar_output = konversi_rupiah_ke_dollar(rupiah_input)
# print(f"Jumlah dalam dollar: ${dollar_output:.2f}")

# Sistem konversi suhu derajat celsius ke fahrenheit
# def konversi_celsius_ke_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# celsius_input = float(input("Masukkan suhu dalam Celsius: "))
# fahrenheit_output = konversi_celsius_ke_fahrenheit(celsius_input)
# print(f"Jumlah dalam Fahrenheit: {fahrenheit_output:.2f}")

# Sistem kalkulator sederhana
# def kalkulator(angka1, angka2, operasi):
#     if operasi == "+":
#         return angka1 + angka2
#     elif operasi == "-":
#         return angka1 - angka2
#     elif operasi == "*":
#         return angka1 * angka2
#     elif operasi == "/":
#         return angka1 / angka2
#     else:
#         return "Operasi tidak dikenali."
# angka1_input = float(input("Masukkan angka pertama: "))
# angka2_input = float(input("Masukkan angka kedua: "))
# operasi_input = input("Masukkan operasi (+, -, *, /): ")
# hasil = kalkulator(angka1_input, angka2_input, operasi_input)
# print(f"Hasil: {hasil}")

# Sistem deteksi performa mahasiswa menggunakan kelas
# class PerformaMahasiswa:
#     def __init__(self, nama, skor):
#         self.nama = nama
#         self.skor = skor

#     def deteksi(self):
#         if self.skor < 50:
#             return "Struggling"
#         elif self.skor < 70:
#             return "Gaming the System"
#         elif self.skor < 85:
#             return "Normal"
#         else:
#             return "Ideal"
        
# mahasiswa1 = PerformaMahasiswa("Dicky", 45)
# print(f"{mahasiswa1.nama} → Kategori: {mahasiswa1.deteksi()}")

# mahasiswa2 = PerformaMahasiswa("Rina", 78)
# print(f"{mahasiswa2.nama} → Kategori: {mahasiswa2.deteksi()}")

# mahasiswa3 = PerformaMahasiswa("Adi", 92)
# print(f"{mahasiswa3.nama} → Kategori: {mahasiswa3.deteksi()}")

# Sistem chatbot edukasi sederhana menggunakan kelas
# class EduChatbot:
#     def __init__(self, nama):
#         self.nama = nama

#     def respon(self, pertanyaan):
#         if "array" in pertanyaan.lower():
#             return "Array adalah struktur data yang menyimpan banyak nilai dalam satu variabel."
#         elif "loop" in pertanyaan.lower():
#             return "Loop digunakan untuk perulangan di program."
#         else:
#             return "Saya tidak yakin, coba pertanyaan lain ya!"
# bot = EduChatbot("TutorAI")
# print(bot.respon("Apa itu array?"))
# print(bot.respon("Jelaskan tentang loop."))
# print(bot.respon("Apa itu fungsi?"))
# def chatbot_interaktif():
#     bot = EduChatbot("TutorAI")
#     while True:
#         pertanyaan = input("Kamu: ")
#         if pertanyaan.lower() == "keluar":
#             print("Bot: Sampai jumpa!")
#             break
#         jawaban = bot.respon(pertanyaan)
#         print(f"Bot: {jawaban}")
# chatbot_interaktif()

# Sistem rekomendasi lomba berdasarkan nilai 
# def rekomendasi_lomba(nilai_web, nilai_jaringan, nilai_ai):
#     if nilai_ai > nilai_web and nilai_ai > nilai_jaringan:
#         return "Rekomendasi: Lomba AI & Data Science"
#     elif nilai_web > nilai_ai and nilai_web > nilai_jaringan:
#         return "Rekomendasi: Lomba Web Programming"
#     elif nilai_jaringan > nilai_ai:
#         return "Rekomendasi: Lomba Jaringan Komputer"
#     else:
#         return "Rekomendasi: Lomba Umum"
# hasil = rekomendasi_lomba(78, 65, 92)
# print(hasil)

# Sistem deteksi performa mahasiswa berdasarkan nilai, waktu, dan percobaan
# def deteksi_kesulitan(nilai, waktu, percobaan):
#     if nilai < 50 or percobaan > 5:
#         return "Struggling"
#     elif nilai < 70:
#         return "Gaming the System"
#     elif nilai < 85:
#         return "Normal"
#     else:
#         return "Ideal"
# mahasiswa = [
#     {"nama": "Dicky", "nilai": 45, "waktu": 35, "percobaan": 6},
#     {"nama": "Tina", "nilai": 80, "waktu": 20, "percobaan": 2},
#     {"nama": "Rina", "nilai": 92, "waktu": 15, "percobaan": 1}
# ]
# for mhs in mahasiswa:
#     kategori = deteksi_kesulitan(mhs["nilai"], mhs["waktu"], mhs["percobaan"])
#     print(f"{mhs['nama']} → Kategori: {kategori}")
    
# Sistem chatbot memberikan feedback berdasarkan nilai dan percobaan
# def chatbot_feedback(nilai, percobaan):
#     if nilai < 60 and percobaan > 3:
#         return "Kamu tampaknya kesulitan. Coba pelajari ulang konsep dasar materi ini."
#     elif nilai < 80:
#         return "Bagus! Tapi coba perkuat logika kodingmu."
#     else:
#         return "Hebat! Kamu berada di level ideal."
# mhs = [
#     {"nama": "Dicky", "nilai": 55, "percobaan": 5},
#     {"nama": "Rina", "nilai": 77, "percobaan": 2},
#     {"nama": "Adi", "nilai": 91, "percobaan": 1}
# ]
# for m in mhs:
#     print(f"{m['nama']} → {chatbot_feedback(m['nilai'], m['percobaan'])}")
    
# Sistem konversi desimal ke biner, oktal, heksadesimal
# def konversi_bilangan(desimal):
#     biner = bin(desimal).replace("0b", "")
#     oktal = oct(desimal).replace("0o", "")
#     heksadesimal = hex(desimal).replace("0x", "").upper()
#     return biner, oktal, heksadesimal
# desimal_input = int(input("Masukkan bilangan desimal: "))
# biner_output, oktal_output, heksadesimal_output = konversi_bilangan(desimal_input)
# print(f"Biner: {biner_output}")
# print(f"Oktal: {oktal_output}")
# print(f"Heksadesimal: {heksadesimal_output}")

# Sistem permainan tebak angka
# import random
# angka_rahasia = random.randint(1, 20)
# percobaan = 0
# while True:
#     tebakan = int(input("Tebak angka (1-20): "))
#     percobaan += 1
#     if tebakan == angka_rahasia:
#         print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
#         break
#     elif tebakan < angka_rahasia:
#         print("Tebakan Anda terlalu rendah.")
#     else:
#         print("Tebakan Anda terlalu tinggi.")
        
# Sistem hitung umur berdasarkan tahun lahir
# from datetime import date
# tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
# tahun_sekarang = date.today().year
# umur = tahun_sekarang - tahun_lahir
# print(f"Umur Anda: {umur} tahun")

# Sistem kalkulator sederhana
# def kalkulator(a, b, operasi):
#     if operasi == '+':
#         return a + b
#     elif operasi == '-':
#         return a - b
#     elif operasi == '*':
#         return a * b
#     elif operasi == '/':
#         return a / b
#     else:
#         return "Operasi tidak dikenal"

# a = float(input("Masukkan angka pertama: "))
# b = float(input("Masukkan angka kedua: "))
# op = input("Masukkan operasi (+, -, *, /): ")

# print("Hasil:", kalkulator(a, b, op))

# Sistem hitung faktorial dari sebuah angka
# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# n = int(input("Masukkan angka: "))
# print(f"Faktorial dari {n} adalah {faktorial(n)}")

# Sistem analisis statistik nilai otomatis
# data = [int(x) for x in input("Masukkan angka (pisahkan dengan spasi): ").split()]
# print(f"Nilai maksimum: {max(data)}")
# print(f"Nilai minimum: {min(data)}")
# print(f"Rata-rata: {sum(data) / len(data)}")

# Sistem login sederhana dengan username dan password
# akun = {"dicky": "12345", "admin": "admin123"}

# user = input("Masukkan username: ")
# pwd = input("Masukkan password: ")

# if user in akun and akun[user] == pwd:
#     print("✅ Login berhasil!")
# else:
#     print("❌ Username atau password salah!")

# Sistem hitung jumlah kata dalam sebuah kalimat
# kalimat = input("Masukkan kalimat: ")
# jumlah_kata = len(kalimat.split())
# print(f"Jumlah kata: {jumlah_kata}")

# Sistem memeriksa bilangan prima
# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# angka = int(input("Masukkan angka: "))
# print("Prima" if prima(angka) else "Bukan prima")

# Sistem kuis sederhana
# soal = {
#     "Apa ibukota Indonesia?": "jakarta",
#     "Berapa hasil 5 * 6?": "30",
#     "Bahasa pemrograman yang digunakan untuk AI?": "python"
# }

# skor = 0
# for pertanyaan, jawaban in soal.items():
#     user_jawab = input(pertanyaan + " ").lower()
#     if user_jawab == jawaban:
#         print("Benar ✅")
#         skor += 1
#     else:
#         print("Salah ❌")

# print(f"Skor akhir kamu: {skor}/{len(soal)}")

# Sistem hitung jumlah huruf vokal dan konsonan
# teks = input("Masukkan kata: ").lower()
# vokal = "aiueo"
# jumlah_vokal = sum(1 for huruf in teks if huruf in vokal)
# jumlah_konsonan = sum(1 for huruf in teks if huruf.isalpha() and huruf not in vokal)

# print(f"Jumlah huruf vokal: {jumlah_vokal}")
# print(f"Jumlah huruf konsonan: {jumlah_konsonan}")

# Sistem stack sederhana menggunakan list
# stack = []

# while True:
#     print("\n1. Push\n2. Pop\n3. Lihat Stack\n4. Keluar")
#     pilihan = input("Pilih: ")

#     if pilihan == '1':
#         data = input("Masukkan data: ")
#         stack.append(data)
#     elif pilihan == '2':
#         if stack:
#             print("Data dihapus:", stack.pop())
#         else:
#             print("Stack kosong!")
#     elif pilihan == '3':
#         print("Isi stack:", stack)
#     elif pilihan == '4':
#         break

# konversi desimal ke biner
# def desimal_ke_biner(angka):
#     return bin(angka)[2:]

# n = int(input("Masukkan bilangan desimal: "))
# print(f"Bentuk biner: {desimal_ke_biner(n)}")

# sistem penilaian ujian
# uts = float(input("Masukkan nilai UTS: "))
# uas = float(input("Masukkan nilai UAS: "))
# tugas = float(input("Masukkan nilai Tugas: "))

# rata = (uts + uas + tugas) / 3

# if rata >= 85:
#     kategori = "Sangat Baik"
# elif rata >= 70:
#     kategori = "Baik"
# elif rata >= 60:
#     kategori = "Cukup"
# else:
#     kategori = "Kurang"

# print(f"Nilai akhir: {rata:.2f} ({kategori})")

# Sistem permainan tebak angka
# import random
# angka_rahasia = random.randint(1, 10)

# while True:
#     tebak = int(input("Tebak angka (1-10): "))
#     if tebak == angka_rahasia:
#         print("🎉 Tebakan kamu benar!")
#         break
#     elif tebak < angka_rahasia:
#         print("Terlalu kecil!")
#     else:
#         print("Terlalu besar!")

# Sistem kamus sederhana
# kamus = {
#     "apple": "apel",
#     "car": "mobil",
#     "house": "rumah",
#     "book": "buku"
# }

# kata = input("Masukkan kata (inggris): ").lower()
# print(f"Terjemahan: {kamus.get(kata, 'Tidak ditemukan dalam kamus.')}")

# Sistem penjumlahan matriks
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# hasil = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
# print("Hasil penjumlahan matriks:")
# for baris in hasil:
#     print(baris)

# Sistem hitung jumlah huruf dan angka dalam teks
# teks = input("Masukkan teks campuran: ")
# huruf = sum(1 for c in teks if c.isalpha())
# angka = sum(1 for c in teks if c.isdigit())

# print(f"Jumlah huruf: {huruf}")
# print(f"Jumlah angka: {angka}")

# Sistem menampilkan bilangan prima dalam rentang tertentu
# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# batas = int(input("Masukkan batas angka: "))
# print("Bilangan prima dari 1 sampai", batas, "adalah:")
# for i in range(1, batas + 1):
#     if prima(i):
#         print(i, end=" ")
       
# Sistem simulasi ATM sederhana 
# saldo = 100000
# while True:
#     print("\nSaldo Anda:", saldo)
#     print("1. Tambah Saldo\n2. Tarik Saldo\n3. Keluar")
#     pilih = input("Pilih menu: ")

#     if pilih == "1":
#         jumlah = int(input("Masukkan jumlah: "))
#         saldo += jumlah
#     elif pilih == "2":
#         jumlah = int(input("Masukkan jumlah: "))
#         if jumlah <= saldo:
#             saldo -= jumlah
#         else:
#             print("Saldo tidak cukup!")
#     elif pilih == "3":
#         break

# Sistem hitung volume bangun ruang
# import math

# print("Pilih bangun ruang:")
# print("1. Kubus\n2. Balok\n3. Tabung")
# pilih = input("Pilih: ")

# if pilih == "1":
#     sisi = float(input("Masukkan sisi: "))
#     print("Volume Kubus =", sisi ** 3)
# elif pilih == "2":
#     p = float(input("Panjang: "))
#     l = float(input("Lebar: "))
#     t = float(input("Tinggi: "))
#     print("Volume Balok =", p * l * t)
# elif pilih == "3":
#     r = float(input("Jari-jari: "))
#     t = float(input("Tinggi: "))
#     print("Volume Tabung =", math.pi * r**2 * t)

# Sistem membalik angka
# angka = int(input("Masukkan angka: "))
# reversed_num = 0

# while angka > 0:
#     sisa = angka % 10
#     reversed_num = reversed_num * 10 + sisa
#     angka //= 10

# print("Angka terbalik:", reversed_num)

# Sistem analisis statistik nilai otomatis
# data = [int(x) for x in input("Masukkan deret angka (pisahkan spasi): ").split()]

# rata = sum(data) / len(data)
# maks = max(data)
# minim = min(data)

# print(f"Rata-rata: {rata:.2f}")
# print(f"Nilai maksimum: {maks}")
# print(f"Nilai minimum: {minim}")

# Sistem permainan pertarungan sederhana
# monster_hp = 50
# player_hp = 40

# while monster_hp > 0 and player_hp > 0:
#     print(f"\nPlayer HP: {player_hp} | Monster HP: {monster_hp}")
#     serangan = int(input("Masukkan kekuatan serangan (1-10): "))
#     monster_hp -= serangan

#     if monster_hp <= 0:
#         print("🎉 Monster dikalahkan!")
#         break

#     player_hp -= 5
#     if player_hp <= 0:
#         print("💀 Kamu kalah!")
#         

# Sistem palindrom deteksi
# kata = input("Masukkan kata: ").lower().replace(" ", "")
# if kata == kata[::-1]:
#     print("Kata ini adalah palindrom!")
# else:
#     print("Bukan palindrom.")
    
# Sistem hitung frekuensi kata dalam kalimat
# teks = input("Masukkan kalimat: ").lower().split()
# frekuensi = {}

# for kata in teks:
#     frekuensi[kata] = frekuensi.get(kata, 0) + 1

# print("Frekuensi tiap kata:")
# for k, v in frekuensi.items():
#     print(f"{k}: {v} kali")

# Sistem menyimpan dan menampilkan data dari file
# nama_file = "catatan.txt"
# tulis = input("Tulis sesuatu untuk disimpan di file: ")

# with open(nama_file, "w") as file:
#     file.write(tulis)

# print("Isi file:")
# with open(nama_file, "r") as file:
#     print(file.read())

# Menampilkan Deret Fibonacci
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# batas = int(input("Masukkan jumlah deret Fibonacci: "))
# for i in range(batas):
#     print(fibonacci(i), end=" ")

# Simulasi Lempar Dadu
# import random

# while True:
#     roll = random.randint(1, 6)
#     print("🎲 Kamu mendapatkan angka:", roll)
#     lagi = input("Lempar lagi? (y/n): ")
#     if lagi.lower() != 'y':
#         break
    
 # Sistem login sederhana dengan username dan password   
# akun = {"user1": "1234", "admin": "adminpass"}

# username = input("Masukkan username: ")
# password = input("Masukkan password: ")

# if username in akun and akun[username] == password:
#     print("✅ Login berhasil! Selamat datang,", username)
# else:
#     print("❌ Username atau password salah!")

# Sistem to-do list sederhana
# tugas = []

# while True:
#     print("\n1. Tambah Tugas\n2. Lihat Tugas\n3. Hapus Tugas\n4. Keluar")
#     pilih = input("Pilih menu: ")

#     if pilih == "1":
#         isi = input("Masukkan nama tugas: ")
#         tugas.append(isi)
#     elif pilih == "2":
#         print("Daftar tugas:")
#         for i, t in enumerate(tugas, 1):
#             print(f"{i}. {t}")
#     elif pilih == "3":
#         no = int(input("Nomor tugas yang dihapus: "))
#         if 0 < no <= len(tugas):
#             del tugas[no - 1]
#     elif pilih == "4":
#         break

# sistem hitung faktorial dari sebuah angka
# n = int(input("Masukkan angka: "))
# hasil = 1

# for i in range(1, n + 1):
#     hasil *= i

# print(f"Faktorial dari {n} adalah {hasil}")

# sistem menampilkan bilangan prima dalam rentang tertentu
# batas = int(input("Masukkan batas angka: "))
# print(f"Bilangan prima dari 1 sampai {batas} adalah:")
# for num in range(2, batas + 1):
#     is_prima = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prima = False
#             break
#     if is_prima:
#         print(num, end=" ")

# sistem membalik kalimat
# kalimat = input("Masukkan kalimat: ")
# reversed_text = ""
# for char in kalimat:
#     reversed_text = char + reversed_text

# print("Kalimat terbalik:", reversed_text)

# Sistem operasi pecahan dasar
# from fractions import Fraction

# a = Fraction(input("Masukkan pecahan pertama (misal 1/2): "))
# b = Fraction(input("Masukkan pecahan kedua (misal 3/4): "))

# print("Hasil penjumlahan:", a + b)
# print("Hasil pengurangan:", a - b)
# print("Hasil perkalian:", a * b)
# print("Hasil pembagian:", a / b)
        
# Sistem konversi suhu derajat Celsius ke Fahrenheit dan Kelvin
# print("1. Celsius ke Fahrenheit")
# print("2. Fahrenheit ke Celsius")
# print("3. Celsius ke Kelvin")

# pilihan = input("Pilih konversi: ")

# if pilihan == "1":
#     c = float(input("Masukkan suhu (°C): "))
#     print(f"Hasil: {c * 9/5 + 32} °F")
# elif pilihan == "2":
#     f = float(input("Masukkan suhu (°F): "))
#     print(f"Hasil: {(f - 32) * 5/9} °C")
# elif pilihan == "3":
#     c = float(input("Masukkan suhu (°C): "))
#     print(f"Hasil: {c + 273.15} K")

# Sistem enkripsi teks menggunakan metode Caesar Cipher
# def caesar_cipher(teks, shift):
#     hasil = ""
#     for huruf in teks:
#         if huruf.isalpha():
#             ascii_offset = 65 if huruf.isupper() else 97
#             hasil += chr((ord(huruf) - ascii_offset + shift) % 26 + ascii_offset)
#         else:
#             hasil += huruf
#     return hasil

# pesan = input("Masukkan teks: ")
# geser = int(input("Geser berapa huruf: "))
# print("Teks terenkripsi:", caesar_cipher(pesan, geser))

# Sistem chatbot sederhana
# while True:
#     tanya = input("Kamu: ").lower()
#     if "halo" in tanya:
#         print("Bot: Hai juga! Apa kabar?")
#     elif "kabarmu" in tanya:
#         print("Bot: Aku baik, terima kasih sudah bertanya 😊")
#     elif "bye" in tanya:
#         print("Bot: Sampai jumpa lagi!")
#         break
#     else:
#         print("Bot: Aku belum paham maksudmu.")

# sistem antrian toko sederhana
# from collections import deque
# antrian = deque()
# while True:
#     print("\n1. Tambah Antrian\n2. Layani Antrian\n3. Lihat Antrian\n4. Keluar")
#     pilih = input("Pilih menu: ")

#     if pilih == "1":
#         nama = input("Masukkan nama pelanggan: ")
#         antrian.append(nama)
#         print(f"{nama} ditambahkan ke antrian.")
#     elif pilih == "2":
#         if antrian:
#             dilayani = antrian.popleft()
#             print(f"{dilayani} telah dilayani.")
#         else:
#             print("Antrian kosong!")
#     elif pilih == "3":
#         print("Daftar antrian saat ini:")
#         for i, nama in enumerate(antrian, 1):
#             print(f"{i}. {nama}")
#     elif pilih == "4":
#         break

# Sistem daftar produk toko gym
# produk = {
#     "Dumbbell": 150000,
#     "Yoga Mat": 100000,
#     "Pull Up Bar": 250000,
#     "Protein Shake": 300000
# }

# print("=== DAFTAR PRODUK TOKO GYM ===")
# for nama, harga in produk.items():
#     print(f"{nama:15} : Rp. {harga}")

# Sistem pembelian produk toko gym
# produk = {"Dumbbell": 150000, "Yoga Mat": 100000, "Pull Up Bar": 250000, "Protein Shake": 300000}

# pilihan = input("Pilih produk yang ingin dibeli: ")
# if pilihan in produk:
#     jumlah = int(input("Masukkan jumlah barang: "))
#     total = produk[pilihan] * jumlah
#     print(f"Total harga: Rp{total}")
# else:
#     print("Produk tidak tersedia.")

# Sistem pembelian dengan diskon di toko gym
# produk = {"Treadmill": 3000000, "Sepeda Statis": 2500000, "Kettlebell": 200000}

# pilihan = input("Masukkan produk yang dibeli: ")
# jumlah = int(input("Masukkan jumlah: "))

# if pilihan in produk:
#     total = produk[pilihan] * jumlah
#     if total > 1000000:
#         diskon = total * 0.1
#         total -= diskon
#         print(f"Dapat diskon Rp{diskon:.0f}!")
#     print(f"Total bayar: Rp{total:.0f}")
# else:
#     print("Produk tidak ditemukan.")

# Sistem kembalian pembayaran di toko gym
# harga = int(input("Masukkan total harga belanja: "))
# bayar = int(input("Masukkan uang yang dibayarkan: "))

# if bayar < harga:
#     print("⚠️ Uang tidak cukup!")
# else:
#     print(f"Kembalian Anda: Rp{bayar - harga}")

# Sistem member dengan diskon di toko gym
# class Member:
#     def __init__(self, nama, level):
#         self.nama = nama
#         self.level = level

#     def get_diskon(self):
#         if self.level == "gold":
#             return 0.2
#         elif self.level == "silver":
#             return 0.1
#         else:
#             return 0

# nama = input("Masukkan nama Anda: ")
# level = input("Masukkan level member (gold/silver/reguler): ").lower()

# member = Member(nama, level)
# total = int(input("Masukkan total belanja: "))
# total_bayar = total - (total * member.get_diskon())

# print(f"\nMember {member.nama} ({member.level}) mendapat diskon {member.get_diskon()*100:.0f}%")
# print(f"Total bayar akhir: Rp{total_bayar:.0f}")

# Sistem pembelian produk dengan keranjang di toko gym
# produk = {"Gloves": 75000, "Jump Rope": 50000, "Whey Protein": 350000}
# keranjang = []
# total = 0

# while True:
#     print("\nProduk tersedia:", list(produk.keys()))
#     pilih = input("Pilih produk (atau ketik 'selesai'): ")

#     if pilih == "selesai":
#         break
#     elif pilih in produk:
#         keranjang.append(pilih)
#         total += produk[pilih]
#         print(f"{pilih} ditambahkan ke keranjang.")
#     else:
#         print("Produk tidak tersedia.")

# print("\n🧾 Daftar belanja:", keranjang)
# print(f"Total bayar: Rp{total}")


# sistem hitung volume bola
# import math
# radius = float(input("Masukkan jari-jari bola: "))
# volume = (4/3) * math.pi * radius**3
# print(f"Volume bola dengan jari-jari {radius} adalah {volume}")

# sistem palindrom deteksi
# kata = input("Masukkan kata: ").lower().replace(" ", "")
# if kata == kata[::-1]:
#     print("Kata ini adalah palindrom!")
# else:
#     print("Bukan palindrom")

# sistem operasi pecahan dasar
# from fractions import Fraction
# a = Fraction(input("Masukkan pecahan pertama (misal 1/2): "))
# b = Fraction(input("Masukkan pecahan kedua (misal 3/4): "))
# print("Hasil penjumlahan:", a + b)
# print("Hasil pengurangan:", a - b)
# print("Hasil perkalian:", a * b)
# print("Hasil pembagian:", a / b)

# sistem enkripsi teks menggunakan metode Caesar Cipher
# def caesar_cipher(teks, shift):
#     hasil = ""
#     for huruf in teks:
#         if huruf.isalpha():
#             ascii_offset = 65 if huruf.isupper() else 97
#             hasil += chr((ord(huruf) - ascii_offset + shift) % 26 + ascii_offset)
#         else:
#             hasil += huruf
#     return hasil
# pesan = input("Masukkan teks: ")
# geser = int(input("Geser berapa huruf: "))
# print("Hasil enkripsi:", caesar_cipher(pesan, geser))

# sistem antrian toko sederhana
# from collections import deque
# antrian = deque()
# while True:
#     print("\n1. Tambah Antrian\n2. Layani Antrian\n3. Lihat Antrian\n4. Keluar")
#     pilih = input("Pilih menu: ")

#     if pilih == "1":
#         nama = input("Masukkan nama pelanggan: ")
#         antrian.append(nama)
#         print(f"{nama} ditambahkan ke antrian.")
#     elif pilih == "2":
#         if antrian:
#             dilayani = antrian.popleft()
#             print(f"{dilayani} telah dilayani.")
#         else:
#             print("Antrian kosong!")
#     elif pilih == "3":
#         print("Daftar antrian saat ini:")
#         for i, nama in enumerate(antrian, 1):
#             print(f"{i}. {nama}")
#     elif pilih == "4":
#         break
#     print("Terima kasih telah menggunakan sistem antrian kami!")

# Sistem daftar produk toko gym
# data_produk = {
#     "Dumbbell": 150000,
#     "Yoga Mat": 100000,
#     "Pull Up Bar": 250000,
#     "Protein Shake": 300000
# }
# print("=== DAFTAR PRODUK TOKO GYM ===")
# for nama, harga in data_produk.items():
#     print(f"{nama:15} : Rp. {harga}")

# Sistem pembelian produk toko gym
# produk = {"Dumbbell": 150000, "Yoga Mat": 100000, "Pull Up Bar": 250000, "Protein Shake": 300000}
# pilihan = input("Pilih produk yang ingin dibeli: ")
# if pilihan in produk:
#     jumlah = int(input("Masukkan jumlah barang: "))
#     total = produk[pilihan] * jumlah
#     print(f"Total harga: Rp{total}")
# else:
#     print("Produk tidak tersedia.")

# sistem pembelian dengan diskon di toko gym
# produk = {"Treadmill": 3000000, "Sepeda Statis": 2500000, "Kettlebell": 200000}
# pilihan = input("Masukkan produk yang dibeli: ")
# jumlah = int(input("Masukkan jumlah: "))
# if pilihan in produk:
#     total = produk[pilihan] * jumlah
#     if total > 1000000:
#         diskon = total * 0.1
#         total -= diskon
#         print(f"Dapat diskon Rp{diskon:.0f}!")
#     print(f"Total bayar: Rp{total:.0f}")
# else:
#     print("Produk tidak ditemukan.")


# # sistem kembalian pembayaran di toko gym
# produk = {"Dumbbell": 150000, "Yoga Mat": 100000, "Pull Up Bar": 250000, "Protein Shake": 300000}
# harga = int(input("Masukkan total harga belanja: "))
# bayar = int(input("Masukkan uang yang dibayarkan: "))
# if bayar < harga:
#     print("⚠️ Uang tidak cukup!")
# else:
#     print(f"Kembalian Anda: Rp{bayar - harga}")
    
    
# sistem member dengan diskon di toko gym
# class member:
#     def __init__(self, nama, level):
#         self.nama = nama
#         self.level = level

#     def get_diskon(self):
#         if self.level == "gold":
#             return 0.2
#         elif self.level == "silver":
#             return 0.1
#         else:
#             return 0
# nama = input("Masukkan nama Anda: ")
# level = input("Masukkan level member (gold/silver/reguler): ").lower()
# member = member(nama, level)
# total = int(input("Masukkan total belanja: "))
# total_bayar = total - (total * member.get_diskon())
# print(f"\nMember {member.nama} ({member.level}) mendapat diskon {member.get_diskon()*100:.0f}%")
# print(f"Total yang harus dibayar: Rp{total_bayar}")

# sistem pembelian produk dengan keranjang di toko gym
# produk = {"Gloves": 75000, "Jump Rope": 50000, "Whey Protein": 350000}
# keranjang = []
# total = 0
# while True:
#     print("\nProduk tersedia:", list(produk.keys()))
#     pilih = input("Pilih produk (atau ketik 'selesai'): ")

#     if pilih == "selesai":
#         break
#     elif pilih in produk:
#         keranjang.append(pilih)
#         total += produk[pilih]
#         print(f"{pilih} ditambahkan ke keranjang.")
#     else:
#         print("Produk tidak tersedia.")
# print("\n🧾 Daftar belanja:", keranjang)
# print(f"Total belanja: Rp{total}")

# sistem hitung volume bola
# import math
# radius = float(input("Masukkan jari-jari bola: "))
# volume = (4/3) * math.pi * radius**3
# print(f"Volume bola dengan jari-jari {radius} adalah {volume}")

# sistem palindrom deteksi
# kata = input("Masukkan kata: ").lower().replace(" ", "")
# if kata == kata[::-1]:
#     print("Kata ini adalah palindrom!")
# else:
#     print("Bukan palindrom")
    
# sistem operasi pecahan dasar
# from fractions import Fraction
# a = Fraction(input("Masukkan pecahan pertama (misal 1/2): "))
# b = Fraction(input("Masukkan pecahan kedua (misal 3/4): "))
# print(f"Jumlah: {a + b}")
# print(f"Selisih: {a - b}")
# print(f"Perkalian: {a * b}")
# print(f"Pembagian: {a / b}")

# sistem enkripsi teks menggunakan metode Caesar Cipher
# def caesar_cipher(teks, shift):
#     hasil = ""
#     for huruf in teks:
#         if huruf.isalpha():
#             ascii_offset = 65 if huruf.isupper() else 97
#             hasil += chr((ord(huruf) - ascii_offset + shift) % 26 + ascii_offset)
#         else:
#             hasil += huruf
#     return hasil
# pesan = input("Masukkan teks: ")
# geser = int(input("Geser berapa huruf: "))
# print("Hasil enkripsi:", caesar_cipher(pesan, geser))

# sistem antrian toko sederhana
# stok = {"Dumbbell": 10, "Yoga Mat": 15, "Pull Up Bar": 5}

# print("=== CEK STOK TOKO GYM ===")
# for barang, jumlah in stok.items():
#     print(f"{barang:15} : {jumlah} unit")

# barang = input("\nMasukkan nama barang yang ingin dibeli: ")
# jumlah = int(input("Masukkan jumlah pembelian: "))

# if barang in stok:
#     if jumlah <= stok[barang]:
#         stok[barang] -= jumlah
#         print(f"Berhasil membeli {jumlah} {barang}. Sisa stok: {stok[barang]}")
#     else:
#         print("⚠️ Stok tidak mencukupi.")
# else:
#     print("Barang tidak ditemukan.")

# sistem keranjang belanja di toko gym
# produk = {"Whey Protein": 350000, "Sarung Tangan": 80000, "Skipping Rope": 60000}
# keranjang = []
# total = 0

# while True:
#     print("\nProduk:", list(produk.keys()))
#     pilih = input("Pilih produk (atau ketik 'selesai'): ")
#     if pilih == "selesai":
#         break
#     elif pilih in produk:
#         keranjang.append(pilih)
#         total += produk[pilih]
#     else:
#         print("Produk tidak tersedia.")

# print("\n=== STRUK PEMBELIAN ===")
# for item in keranjang:
#     print("-", item, "Rp", produk[item])
# print("Total Bayar: Rp", total)
# print("Terima kasih telah berbelanja di GymFit Store 💪")

# sistem cicilan pembelian di toko gym
# harga = int(input("Masukkan harga alat gym: Rp"))
# cicilan = int(input("Ingin dicicil berapa bulan? "))

# bunga = 0.05 * harga
# total = harga + bunga
# per_bulan = total / cicilan

# print(f"\nTotal dengan bunga: Rp{total:.0f}")
# print(f"Bayar per bulan: Rp{per_bulan:.0f}")

# Sistem daftar pelanggan gym
# pelanggan = []

# while True:
#     nama = input("Masukkan nama pelanggan (atau ketik 'selesai'): ")
#     if nama.lower() == "selesai":
#         break
#     pelanggan.append(nama)

# print("\n=== DAFTAR PELANGGAN GYM ===")
# for i, p in enumerate(pelanggan, 1):
#     print(f"{i}. {p}")

# Sistem laporan penjualan harian di toko gym
# penjualan = {
#     "Dumbbell": 5,
#     "Yoga Mat": 3,
#     "Pull Up Bar": 2,
#     "Gloves": 6
# }

# total_item = sum(penjualan.values())
# barang_terlaris = max(penjualan, key=penjualan.get)

# print("=== LAPORAN PENJUALAN HARIAN ===")
# for barang, jumlah in penjualan.items():
#     print(f"{barang:15}: {jumlah} terjual")
# print(f"\nTotal item terjual: {total_item}")
# print(f"Barang terlaris: {barang_terlaris}")

# Sistem pembelian produk dengan pajak dan diskon di toko gym
# produk = {"Treadmill": 3000000, "Bench Press": 2500000, "Elliptical": 2700000}
# pilih = input("Pilih produk: ")

# if pilih in produk:
#     harga = produk[pilih]
#     diskon = 0.1 if harga > 2500000 else 0
#     pajak = 0.05 * harga
#     total = harga - (harga * diskon) + pajak

#     print(f"\nHarga Asli: Rp{harga}")
#     print(f"Diskon: {diskon*100:.0f}%")
#     print(f"Pajak: Rp{pajak}")
#     print(f"Total Bayar: Rp{total}")
# else:
#     print("Produk tidak ditemukan.")

# Sistem pembelian produk dengan kelas di toko gym
# class Produk:
#     def __init__(self, nama, harga, stok):
#         self.nama = nama
#         self.harga = harga
#         self.stok = stok

#     def kurangi_stok(self, jumlah):
#         if jumlah <= self.stok:
#             self.stok -= jumlah
#             return True
#         return False

# class Transaksi:
#     def __init__(self):
#         self.total = 0

#     def beli(self, produk, jumlah):
#         if produk.kurangi_stok(jumlah):
#             subtotal = produk.harga * jumlah
#             self.total += subtotal
#             print(f"{jumlah}x {produk.nama} dibeli. Subtotal: Rp{subtotal}")
#         else:
#             print(f"Stok {produk.nama} tidak mencukupi.")

#     def tampilkan_total(self):
#         print(f"\nTotal Pembayaran: Rp{self.total}")

# # --- Eksekusi Program ---
# dumbbell = Produk("Dumbbell", 150000, 10)
# mat = Produk("Yoga Mat", 100000, 5)

# trx = Transaksi()
# trx.beli(dumbbell, 2)
# trx.beli(mat, 3)
# trx.tampilkan_total()

# Sistem login sederhana dengan username dan password di toko gym
# akun = {"admin": "12345", "kasir": "gymfit"}

# print("=== LOGIN SISTEM TOKO GYM ===")
# user = input("Username: ")
# pw = input("Password: ")

# if user in akun and akun[user] == pw:
#     print(f"✅ Selamat datang, {user}!")
# else:
#     print("❌ Username atau password salah.")

# Sistem pembelian produk dengan keranjang di toko gym
# produk = {"Dumbbell": 200000, "Matras Yoga": 150000, "Sarung Tangan": 80000}
# keranjang = {}
# total = 0

# while True:
#     print("\nProduk tersedia:", list(produk.keys()))
#     pilih = input("Masukkan produk (atau 'selesai'): ")
#     if pilih == "selesai":
#         break
#     elif pilih in produk:
#         qty = int(input("Jumlah: "))
#         keranjang[pilih] = keranjang.get(pilih, 0) + qty
#     else:
#         print("Produk tidak ada.")

# print("\n=== STRUK PEMBELIAN ===")
# for item, jml in keranjang.items():
#     subtotal = produk[item] * jml
#     total += subtotal
#     print(f"{item:15} x{jml} = Rp{subtotal}")
# print("Total Bayar: Rp", total)

# Sistem pendaftaran member gym dengan tipe membership
# nama = input("Masukkan nama member: ")
# tipe = input("Pilih tipe membership (Silver/Gold/Platinum): ").lower()

# biaya = {"silver": 200000, "gold": 350000, "platinum": 500000}
# bonus = {"silver": "Free 1 day pass", "gold": "Free 3 day pass", "platinum": "Free personal trainer 2 sesi"}

# if tipe in biaya:
#     print(f"\nMember {nama} berhasil didaftarkan.")
#     print(f"Biaya bulanan: Rp{biaya[tipe]}")
#     print(f"Bonus: {bonus[tipe]}")
# else:
#     print("Tipe tidak tersedia.")

# Sistem pembayaran dengan saldo di toko gym
# saldo = 1000000
# tagihan = int(input("Masukkan total belanja: Rp"))

# if saldo >= tagihan:
#     saldo -= tagihan
#     print(f"✅ Pembayaran berhasil! Sisa saldo: Rp{saldo}")
# else:
#     print(f"❌ Saldo tidak cukup. Kurang Rp{tagihan - saldo}")

# Sistem laporan penjualan mingguan di toko gym
# penjualan = {
#     "Senin": 5,
#     "Selasa": 8,
#     "Rabu": 3,
#     "Kamis": 7,
#     "Jumat": 6,
#     "Sabtu": 10,
#     "Minggu": 9
# }

# total = sum(penjualan.values())
# rata = total / len(penjualan)
# hari_tertinggi = max(penjualan, key=penjualan.get)

# print("=== LAPORAN PENJUALAN MINGGUAN ===")
# for hari, jml in penjualan.items():
#     print(f"{hari:8} : {jml} transaksi")
# print(f"\nTotal transaksi: {total}")
# print(f"Rata-rata per hari: {rata:.2f}")
# print(f"Hari tertinggi: {hari_tertinggi}")

# Sistem chatbot sederhana untuk toko gym
# data = {
#     "dumbbell": "Alat untuk latihan kekuatan otot lengan dan bahu.",
#     "treadmill": "Mesin untuk latihan kardio dengan berjalan atau berlari.",
#     "protein": "Zat penting untuk pembentukan otot setelah latihan."
# }

# print("🤖 Selamat datang di GymBot!")
# tanya = input("Tanya tentang alat gym apa: ").lower()

# if tanya in data:
#     print("💡", data[tanya])
# else:
#     print("Maaf, data tidak ditemukan.")

# Sistem pembelian produk dengan kelas di toko gym
# class Produk:
#     def __init__(self, nama, harga, stok):
#         self.nama = nama
#         self.harga = harga
#         self.stok = stok

#     def beli(self, jumlah):
#         if jumlah <= self.stok:
#             self.stok -= jumlah
#             return jumlah * self.harga
#         else:
#             print("⚠️ Stok tidak mencukupi!")
#             return 0

# class TokoGym:
#     def __init__(self):
#         self.daftar_produk = [
#             Produk("Dumbbell", 150000, 10),
#             Produk("Yoga Mat", 80000, 5),
#             Produk("Gloves", 50000, 7)
#         ]
#         self.total = 0

#     def tampilkan_produk(self):
#         print("\n=== PRODUK GYM ===")
#         for p in self.daftar_produk:
#             print(f"{p.nama:10} Rp{p.harga} | Stok: {p.stok}")

#     def transaksi(self):
#         while True:
#             self.tampilkan_produk()
#             nama = input("\nMasukkan nama produk ('selesai' untuk keluar): ")
#             if nama.lower() == "selesai":
#                 break
#             for p in self.daftar_produk:
#                 if p.nama.lower() == nama.lower():
#                     qty = int(input("Masukkan jumlah: "))
#                     self.total += p.beli(qty)
#                     break
#             else:
#                 print("Produk tidak ditemukan.")

#         print(f"\n💰 Total Pembayaran: Rp{self.total}")

# # Jalankan Program
# gym = TokoGym()
# gym.transaksi()

# Sistem cek stok produk di toko gym
# stok = {
#     "Dumbbell": 10,
#     "Yoga Mat": 5,
#     "Protein Shake": 8,
#     "Sarung Tangan": 3
# }

# print("=== CEK STOK GYM ===")
# for item, jumlah in stok.items():
#     status = "AMAN" if jumlah > 5 else "PERINGATAN: Stok menipis!"
#     print(f"{item:15}: {jumlah} unit ({status})")

# Sistem pembelian dengan diskon berdasarkan total belanja di toko gym
# total = int(input("Masukkan total belanja: Rp "))
# diskon = 0

# if total >= 500000:
#     diskon = 0.2
# elif total >= 300000:
#     diskon = 0.1
# elif total >= 100000:
#     diskon = 0.05

# bayar = total - (total * diskon)
# print(f"Diskon: {diskon*100:.0f}%")
# print(f"Total bayar: Rp{bayar:.0f}")

# Sistem pembelian produk dengan kelas di toko gym
# class Produk:
#     def __init__(self, nama, harga, stok):
#         self.nama = nama
#         self.harga = harga
#         self.stok = stok

#     def jual(self, jumlah):
#         if jumlah <= self.stok:
#             self.stok -= jumlah
#             return self.harga * jumlah
#         else:
#             print(f"❌ Stok {self.nama} tidak cukup.")
#             return 0

# class Transaksi:
#     def __init__(self):
#         self.total = 0

#     def beli(self, produk, jumlah):
#         subtotal = produk.jual(jumlah)
#         self.total += subtotal
#         print(f"{produk.nama} x{jumlah} = Rp{subtotal}")

#     def tampilkan_total(self):
#         print(f"\n💰 Total Pembayaran: Rp{self.total}")

# # Main program
# p1 = Produk("Dumbbell", 200000, 5)
# p2 = Produk("Treadmill", 1500000, 2)

# t = Transaksi()
# t.beli(p1, 2)
# t.beli(p2, 1)
# t.tampilkan_total()

# Sistem laporan keuangan bulanan di toko gym
# pemasukan = [500000, 750000, 300000, 400000, 1000000]
# pengeluaran = [200000, 150000, 250000, 100000, 300000]

# total_masuk = sum(pemasukan)
# total_keluar = sum(pengeluaran)
# saldo = total_masuk - total_keluar

# print("=== LAPORAN KEUANGAN TOKO GYM ===")
# print(f"Total Pemasukan: Rp{total_masuk}")
# print(f"Total Pengeluaran: Rp{total_keluar}")
# print(f"Saldo Akhir: Rp{saldo}")

# Sistem chatbot sederhana untuk toko gym dengan topik latihan, makan, dan istirahat
# import random

# respon = {
#     "latihan": ["Lakukan pemanasan 10 menit sebelum latihan!", "Fokus pada teknik, bukan beratnya."],
#     "makan": ["Konsumsi protein setelah latihan.", "Jaga hidrasi, minum air cukup!"],
#     "istirahat": ["Tidur minimal 7 jam agar otot pulih.", "Istirahat adalah bagian dari progres."]
# }

# while True:
#     tanya = input("\nTanya seputar (latihan/makan/istirahat) atau 'exit': ").lower()
#     if tanya == "exit":
#         print("🤖 Terima kasih sudah berbicara dengan GymBot!")
#         break
#     elif tanya in respon:
#         print("💡", random.choice(respon[tanya]))
#     else:
#         print("Maaf, topik tidak tersedia.")

# Sistem restock produk di toko gym
# produk = {"Treadmill": 0, "Dumbbell": 2, "Protein": 5}

# for item, stok in produk.items():
#     if stok == 0:
#         produk[item] = 10
#         print(f"🔁 Produk {item} di-restock menjadi 10 unit.")
#     else:
#         print(f"{item} masih tersedia {stok} unit.")

# Sistem pendaftaran kelas gym dengan kuota terbatas
# kelas = {
#     "Yoga": 10,
#     "Zumba": 8,
#     "Weight Training": 12
# }

# nama = input("Masukkan nama Anda: ")
# pilih = input("Pilih kelas (Yoga/Zumba/Weight Training): ")

# if pilih in kelas:
#     if kelas[pilih] > 0:
#         kelas[pilih] -= 1
#         print(f"✅ {nama} berhasil mendaftar kelas {pilih}.")
#     else:
#         print("❌ Kelas sudah penuh.")
# else:
#     print("Kelas tidak tersedia.")

# Sistem pengingat jadwal latihan gym
# jadwal = {
#     "Senin": "Cardio dan Abs",
#     "Rabu": "Upper Body Strength",
#     "Jumat": "Lower Body Strength"
# }
# hari = input("Masukkan hari (Senin/Rabu/Jumat): ")
# if hari in jadwal:
#     print(f"🏋️ Jadwal latihan hari {hari}: {jadwal[hari]}")
# else:
#     print("Tidak ada jadwal latihan pada hari tersebut.")

# Sistem pembelian produk dengan metode pembayaran di toko gym
# produk = {"Dumbbell": 200000, "Yoga Mat": 150000, "Gloves": 80000}
# pilih = input("Pilih produk yang ingin dibeli: ")
# if pilih in produk:
#     jumlah = int(input("Masukkan jumlah: "))
#     total = produk[pilih] * jumlah
#     print(f"\nTotal harga: Rp{total}")

#     metode = input("Pilih metode pembayaran (cash/kartu): ").lower()
#     if metode == "cash":
#         bayar = int(input("Masukkan jumlah uang yang dibayarkan: Rp"))
#         if bayar >= total:
#             print(f"✅ Pembayaran berhasil! Kembalian: Rp{bayar - total}")
#         else:
#             print("❌ Uang tidak cukup.")
#     elif metode == "kartu":
#         print("✅ Pembayaran dengan kartu berhasil!")
#     else:
#         print("Metode pembayaran tidak dikenali.")
# else:
#     print("Produk tidak tersedia.")

# Sistem pengingat jadwal latihan gym dengan notifikasi sederhana
# import time
# jadwal = {
#     "07:00": "Waktu untuk latihan pagi! Jangan lupa pemanasan.",
#     "12:00": "Saatnya istirahat dan makan siang sehat.",
#     "18:00": "Waktunya latihan sore! Fokus pada teknik."
# }
# while True:
#     sekarang = time.strftime("%H:%M")
#     if sekarang in jadwal:
#         print(f"🔔 Pemberitahuan: {jadwal[sekarang]}")
#         time.sleep(60)  # Tunggu 1 menit untuk menghindari notifikasi berulang
#     time.sleep(10)  # Cek setiap 10 detik
#     print("Program berjalan... Tekan Ctrl+C untuk berhenti.")

# Sistem pendaftaran member gym dengan validasi usia
# nama = input("Masukkan nama Anda: ")
# usia = int(input("Masukkan usia Anda: "))

# if usia >= 18:
#     print(f"✅ {nama}, Anda berhasil mendaftar sebagai member gym.")
# else:
#     print("❌ Maaf, usia Anda belum memenuhi syarat untuk mendaftar.")
    
    
# Sistem laporan keuangan bulanan di toko gym
# pemasukan = [500000, 750000, 300000, 400000, 1000000]
# pengeluaran = [200000, 150000, 250000, 100000, 300000]
# total_masuk = sum(pemasukan)
# total_keluar = sum(pengeluaran)
# saldo = total_masuk - total_keluar
# print("=== LAPORAN KEUANGAN TOKO GYM ===")
# print(f"Total Pemasukan: Rp{total_masuk}")
# print(f"Total Pengeluaran: Rp{total_keluar}")
# print(f"Saldo Akhir: Rp{saldo}")


# sistem rekap masa otot gym
# import datetime
# class MemberGym:
#     def __init__(self, nama, tanggal_lahir):
#         self.nama = nama
#         self.tanggal_lahir = datetime.datetime.strptime(tanggal_lahir, "%d-%m-%Y")

#     def hitung_usia(self):
#         hari_ini = datetime.datetime.now()
#         usia = hari_ini.year - self.tanggal_lahir.year
#         if (hari_ini.month, hari_ini.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day):
#             usia -= 1
#         return usia

#     def rekap_masa_otot(self):
#         usia = self.hitung_usia()
#         if usia < 25:
#             return "Masa otot optimal untuk latihan intensif."
#         elif 25 <= usia < 40:
#             return "Masa otot stabil, pertahankan latihan rutin."
#         else:
#             return "Perlunya perhatian ekstra pada pemulihan otot."
# nama = input("Masukkan nama member: ")
# tanggal_lahir = input("Masukkan tanggal lahir (dd-mm-yyyy): ")
# member = MemberGym(nama, tanggal_lahir)
# print(f"Usia {member.nama}: {member.hitung_usia()} tahun")
# print(member.rekap_masa_otot())


# sistem chatbot sederhana untuk toko gym dengan topik latihan, makan, dan istirahat
# import random
# respon = {
#     "latihan": ["Lakukan pemanasan 10 menit sebelum latihan!", "Fokus pada teknik, bukan beratnya."],
#     "makan": ["Konsumsi protein setelah latihan.", "Jaga hidrasi, minum air cukup!"],
#     "istirahat": ["Tidur minimal 7 jam agar otot pulih.", "Istirahat adalah bagian dari progres."]
# }
# while True:
#     tanya = input("\nTanya seputar (latihan/makan/istirahat) atau 'exit': ").lower()
#     if tanya == "exit":
#         print("🤖 Terima kasih sudah berbicara dengan GymBot!")
#         break
#     elif tanya in respon:
#         print("💡", random.choice(respon[tanya]))
#     else:
#         print("Maaf, topik tidak tersedia.")
        
# Sistem pembelian produk dengan keranjang di toko gym        
# def hitung_total(keranjang):
#     total = 0
#     for item, harga in keranjang.items():
#         total += harga
#     return total

# keranjang = {
#     "Treadmill": 1500000,
#     "Dumbbell": 250000,
#     "Matras Yoga": 120000
# }

# total = hitung_total(keranjang)
# print("=== STRUK PEMBELIAN ===")
# for k, v in keranjang.items():
#     print(f"{k:15} : Rp{v}")
# print(f"Total Bayar : Rp{total}")

# Sistem reward poin untuk pembelian di toko gym
# def hitung_poin(pembelian):
#     if pembelian >= 1000000:
#         return 100
#     elif pembelian >= 500000:
#         return 50
#     else:
#         return 10

# nama = input("Masukkan nama member: ")
# belanja = int(input("Masukkan total pembelian: Rp"))

# poin = hitung_poin(belanja)
# print(f"🎉 Selamat {nama}, Anda mendapat {poin} poin reward!")

# Sistem pendaftaran member gym dengan validasi usia
# anggota = []

# while True:
#     nama = input("Nama anggota (ketik 'stop' untuk berhenti): ")
#     if nama.lower() == "stop":
#         break
#     umur = int(input("Umur: "))
#     if umur < 17:
#         print("❌ Minimal umur 17 tahun untuk mendaftar gym.")
#     else:
#         anggota.append(nama)
#         print(f"✅ {nama} berhasil didaftarkan.")

# print("\nDaftar Anggota Terdaftar:")
# for a in anggota:
#     print("-", a)

# Sistem chatbot motivasi latihan di toko gym
# import random

# motivasi = [
#     "Latihan hari ini adalah kemenangan besok!",
#     "Kekuatan datang dari kebiasaan, bukan niat.",
#     "Kamu tidak perlu cepat, cukup konsisten!",
#     "Istirahat juga bagian dari progres 💪"
# ]

# print("=== GymBot Motivasi ===")
# while True:
#     tanya = input("Ketik 'motivasi' untuk mendapatkan semangat atau 'exit': ").lower()
#     if tanya == "exit":
#         print("Sampai jumpa di sesi berikutnya!")
#         break
#     elif tanya == "motivasi":
#         print(random.choice(motivasi))

# Sistem cek dan tambah stok produk di toko gym
# stok = {}

# while True:
#     print("\n1. Tambah Produk\n2. Lihat Stok\n3. Keluar")
#     menu = input("Pilih menu: ")

#     if menu == "1":
#         nama = input("Nama produk: ")
#         jumlah = int(input("Jumlah stok: "))
#         stok[nama] = stok.get(nama, 0) + jumlah
#         print(f"✅ {nama} ditambahkan ke inventori.")
#     elif menu == "2":
#         print("=== DATA STOK GYM ===")
#         for p, j in stok.items():
#             print(f"{p:15} : {j} unit")
#     elif menu == "3":
#         break
#     else:
#         print("Pilihan tidak valid.")

# Sistem penyimpanan transaksi pembelian di toko gym ke file teks
# with open("transaksi_gym.txt", "a") as file:
#     nama = input("Nama pelanggan: ")
#     total = input("Total belanja: Rp")
#     file.write(f"{nama} - Rp{total}\n")
#     print("🧾 Transaksi berhasil disimpan ke file 'transaksi_gym.txt'")

# Sistem pembelian produk dengan kelas di toko gym
# class Produk:
#     def __init__(self, nama, harga, stok):
#         self.nama = nama
#         self.harga = harga
#         self.stok = stok

#     def jual(self, jumlah):
#         if jumlah <= self.stok:
#             self.stok -= jumlah
#             return jumlah * self.harga
#         else:
#             print(f"❌ Stok {self.nama} tidak cukup.")
#             return 0

# class TokoGym:
#     def __init__(self):
#         self.produk = [
#             Produk("Dumbbell", 200000, 5),
#             Produk("Matras Yoga", 100000, 10),
#             Produk("Protein Shake", 50000, 15)
#         ]
#         self.total = 0

#     def tampilkan(self):
#         print("\n=== PRODUK TOKO GYM ===")
#         for p in self.produk:
#             print(f"{p.nama:15} Rp{p.harga} | Stok: {p.stok}")

#     def beli(self):
#         while True:
#             self.tampilkan()
#             nama = input("\nMasukkan nama produk ('selesai' untuk keluar): ")
#             if nama.lower() == "selesai":
#                 break
#             for p in self.produk:
#                 if p.nama.lower() == nama.lower():
#                     qty = int(input("Masukkan jumlah: "))
#                     self.total += p.jual(qty)
#                     break
#             else:
#                 print("Produk tidak ditemukan.")
#         print(f"\n💰 Total Bayar: Rp{self.total}")

# # Jalankan
# toko = TokoGym()
# toko.beli()

# Sistem enkripsi teks menggunakan metode Caesar Cipher
# def caesar_cipher(teks, shift):
#     hasil = ""
#     for huruf in teks:
#         if huruf.isalpha():
#             ascii_offset = 65 if huruf.isupper() else 97
#             hasil += chr((ord(huruf) - ascii_offset + shift) % 26 + ascii_offset)
#         else:
#             hasil += huruf
#     return hasil
# pesan = input("Masukkan teks: ")
# geser = int(input("Geser berapa huruf: "))
# print("Teks terenkripsi:", caesar_cipher(pesan, geser))
# print("Teks terdekripsi:", caesar_cipher(caesar_cipher(pesan, geser), -geser))


# Sistem antrian pelanggan di toko gym
# from collections import deque
# antrian = deque()
# while True:
#     print("\n=== SISTEM ANTRIAN GYM ===")
#     print("1. Tambah Pelanggan")
#     print("2. Layani Pelanggan")
#     print("3. Lihat Antrian")
#     print("4. Keluar")
#     pilih = input("Pilih menu: ")
#     if pilih == "1":
#         nama = input("Masukkan nama pelanggan: ")
#         antrian.append(nama)
#         print(f"{nama} ditambahkan ke antrian.")
#     elif pilih == "2":
#         if antrian:
#             dilayani = antrian.popleft()
#             print(f"{dilayani} sedang dilayani.")
#         else:
#             print("Antrian kosong.")
#     elif pilih == "3":
#         print("Antrian saat ini:", list(antrian))
#     elif pilih == "4":
#         break
#     else:
#         print("Pilihan tidak valid.")
        
        
# Sistem hitung volume bola
# import math
# radius = float(input("Masukkan jari-jari bola: "))
# volume = (4/3) * math.pi * radius**3
# print(f"Volume bola dengan jari-jari {radius} adalah {volume:.2f}")


# Sistem operasi pecahan dasar
# from fractions import Fraction  
# a = Fraction(input("Masukkan pecahan pertama (misal 1/2): "))
# b = Fraction(input("Masukkan pecahan kedua (misal 3/4): "))
# print(f"Jumlah: {a + b}")
# print(f"Selisih: {a - b}")
# print(f"Perkalian: {a * b}")
# print(f"Pembagian: {a / b}")
# print(f"Pecahan pertama dalam desimal: {float(a)}")
# print(f"Pecahan kedua dalam desimal: {float(b)}")
# print(f"Pecahan pertama dalam persen: {float(a) * 100}%")
# print(f"Pecahan kedua dalam persen: {float(b) * 100}%")


# Sistem pembelian produk dengan diskon di toko gym
# produk = {"Dumbbell": 200000, "Yoga Mat": 150000, "Gloves": 80000}
# pilih = input("Pilih produk yang ingin dibeli: ")
# if pilih in produk:
#     jumlah = int(input("Masukkan jumlah: "))
#     total = produk[pilih] * jumlah

#     if total >= 500000:
#         diskon = 0.2
#     elif total >= 300000:
#         diskon = 0.1
#     elif total >= 100000:
#         diskon = 0.05
#     else:
#         diskon = 0

#     total -= total * diskon
#     print(f"\nDiskon: {diskon*100:.0f}%")
#     print(f"Total yang harus dibayar: Rp{total:.0f}")
# else:
#     print("Produk tidak tersedia.")
  
  
# Sistem pembelian produk dengan kelas Member di toko gym
# class Member:
#     def __init__(self, nama, level):
#         self.nama = nama  
#         self.level = level
#     def get_diskon(self):
#         if self.level == "gold":
#             return 0.2
#         elif self.level == "silver":
#             return 0.1
#         else:
#             return 0.05
# nama = input("Masukkan nama member: ")
# level = input("Masukkan level member (gold/silver/reguler): ").lower()
# member = Member(nama, level)
# print(f"Diskon untuk {member.nama} dengan level {member.level} adalah {member.get_diskon()*100}%")


# Sistem pendaftaran kelas gym dengan kuota terbatas
# kelas = {
#     "Yoga": 10,
#     "Zumba": 8,
#     "Weight Training": 12
# }
# nama = input("Masukkan nama Anda: ")
# pilih = input("Pilih kelas (Yoga/Zumba/Weight Training): ")
# if pilih in kelas:
#     if kelas[pilih] > 0:
#         kelas[pilih] -= 1
#         print(f"✅ {nama} berhasil mendaftar kelas {pilih}.")
#     else:
#         print("❌ Kelas sudah penuh.")
# else:
#     print("Kelas tidak tersedia.")

# Sistem Cek Harga Otomatis (Dictionary Lookup)
# produk = {
#     "Dumbbell 10kg": 250000,
#     "Rope Skipping": 45000,
#     "Gloves Gym": 60000,
#     "Whey Protein": 350000
# }

# item = input("Masukkan nama produk: ")

# if item in produk:
#     print(f"Harga {item} adalah Rp{produk[item]}")
# else:
#     print("Produk tidak ditemukan.")

# Sistem pembelian produk dengan diskon berdasarkan jenis member di toko gym
# harga = int(input("Total harga pembelian: Rp"))
# member = input("Jenis member (silver/gold/non): ").lower()

# if member == "gold":
#     diskon = harga * 0.20
# elif member == "silver":
#     diskon = harga * 0.10
# else:
#     diskon = 0

# bayar = harga - diskon

# print(f"Diskon: Rp{int(diskon)}")
# print(f"Total bayar: Rp{int(bayar)}")

# Sistem struk pembelian di toko gym
nama = input("Nama pembeli: ")
barang = input("Barang dibeli: ")
harga = int(input("Harga barang: Rp"))

print("\n===== STRUK PEMBELIAN GYM =====")
print(f"Pembeli : {nama}")
print(f"Barang  : {barang}")
print(f"Harga   : Rp{harga}")
print("================================")
print("Terima kasih telah berbelanja 💪")
