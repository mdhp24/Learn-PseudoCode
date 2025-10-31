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
angka = int(input("Masukkan angka: "))
reversed_num = 0

while angka > 0:
    sisa = angka % 10
    reversed_num = reversed_num * 10 + sisa
    angka //= 10

print("Angka terbalik:", reversed_num)