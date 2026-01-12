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
# nama = input("Nama pembeli: ")
# barang = input("Barang dibeli: ")
# harga = int(input("Harga barang: Rp"))

# print("\n===== STRUK PEMBELIAN GYM =====")
# print(f"Pembeli : {nama}")
# print(f"Barang  : {barang}")
# print(f"Harga   : Rp{harga}")
# print("================================")
# print("Terima kasih telah berbelanja 💪")

# Sistem total pembelian produk di toko gym
# total = 0

# jumlah = int(input("Berapa jenis produk yang ingin dibeli? "))

# for i in range(jumlah):
#     nama = input(f"Nama produk ke-{i+1}: ")
#     harga = int(input("Harga produk: Rp"))
#     total += harga

# print(f"\nTotal seluruh pembelian: Rp{total}")

# Sistem cicilan pembayaran di toko gym
# tagihan = int(input("Total tagihan: Rp"))
# bayar = 0

# while bayar < tagihan:
#     cicil = int(input("Masukkan pembayaran: Rp"))
#     bayar += cicil
#     print(f"Total terbayar: Rp{bayar}")

# print("🎉 Tagihan lunas!")

# Sistem cek stok produk di toko gym
# stok = {
#     "Barbell": 10,
#     "Kettlebell": 7,
#     "Treadmill": 2,
#     "Resistance Band": 15
# }

# barang = input("Cek stok apa: ")

# if barang in stok:
#     print(f"Stok {barang}: {stok[barang]} unit")
# else:
#     print("Barang tidak tersedia.")

# sistem keranjang belanja di toko gym
# keranjang = []

# while True:
#     barang = input("Tambahkan barang (ketik 'selesai'): ")
#     if barang == "selesai":
#         break
#     keranjang.append(barang)

# print("\n=== KERANJANG ANDA ===")
# for item in keranjang:
#     print("-", item)

# Sistem promo acak di toko gym
# import random

# promo = [
#     "Diskon 10% untuk semua Dumbbell",
#     "Cashback Rp20.000 untuk pembelian Whey Protein",
#     "Buy 1 Get 1 Resistance Band",
#     "Diskon 15% untuk Member Gold",
#     "Gratis Shaker untuk belanja di atas Rp150.000"
# ]

# print("🎯 Promo hari ini:", random.choice(promo))

# Sistem pembelian bundling produk di toko gym
# paket = {
#     1: ("Paket Pemula", 150000),
#     2: ("Paket Intermediate", 300000),
#     3: ("Paket Pro", 500000)
# }

# print("=== DAFTAR BUNDLING ===")
# for k, v in paket.items():
#     print(k, "-", v[0], "Rp", v[1])

# pilihan = int(input("\nPilih paket : "))

# if pilihan in paket:
#     nama, harga = paket[pilihan]
#     print(f"Anda membeli {nama} seharga Rp{harga}")
# else:
#     print("Paket tidak tersedia.")

# Sistem reward poin untuk pembelian di toko gym
# total = int(input("Total pembelian: Rp"))
# poin = total // 10000 * 2  # setiap 10k = 2 poin

# print(f"Anda mendapatkan {poin} poin reward!")

# Sistem cek kategori produk di toko gym
# kategori = {
#     "alat": ["Dumbbell", "Barbell", "Kettlebell", "Rope"],
#     "suplement": ["Whey", "Creatine", "BCAA"],
#     "accessories": ["Gloves", "Matras", "Strap"]
# }

# pilih = input("Cek kategori (alat/suplement/accessories): ")

# if pilih in kategori:
#     print("\nBarang tersedia:")
#     for b in kategori[pilih]:
#         print("-", b)
# else:
#     print("Kategori tidak ditemukan.")

# Sistem total pembelian produk di toko gym
# total = 0

# print("=== Masukkan Pembelian (ketik 0 untuk selesai) ===")
# while True:
#     harga = int(input("Harga item: Rp"))
#     if harga == 0:
#         break
#     total += harga

# print(f"\nTOTAL AKHIR: Rp{total}")

# Sistem kupon diskon di toko gym
# kode = input("Masukkan kode kupon: ").upper()

# if kode == "GYM10":
#     print("Diskon 10% diterapkan!")
# elif kode == "WHEY50":
#     print("Diskon Rp50.000 untuk Whey Protein!")
# elif kode == "FREEBAND":
#     print("Bonus Resistance Band!")
# else:
#     print("Kode kupon tidak valid.")

# Sistem ongkir berdasarkan berat di toko gym
# berat = float(input("Total berat barang (kg): "))
# ongkir = 18000 + (berat * 3000)

# print(f"Total ongkir: Rp{int(ongkir)}")

# Sistem total pembelian produk di toko gym
# total = 0

# print("=== Masukkan Pembelian (ketik 0 untuk selesai) ===")
# while True:
#     harga = int(input("Harga item: Rp"))
#     if harga == 0:
#         break
#     total += harga

# print(f"\nTOTAL AKHIR: Rp{total}")

# Sistem cek stok iPhone di pras_phone.id
# iphone_stock = {
#     "iPhone 12": 3,
#     "iPhone 13": 5,
#     "iPhone 14": 2,
#     "iPhone 15 Pro": 1
# }

# model = input("Cek stok iPhone apa? ")

# if model in iphone_stock:
#     print(f"Stok {model}: {iphone_stock[model]} unit")
# else:
#     print("Model tidak tersedia di pras_phone.id")

# Sistem sewa iPhone di pras_phone.id
# harga_sewa = {
#     "iPhone 11": 50000,
#     "iPhone 12": 70000,
#     "iPhone 13": 90000,
#     "iPhone 14 Pro": 120000
# }

# tipe = input("Pilih iPhone untuk disewa: ")
# hari = int(input("Berapa hari disewa? "))

# if tipe in harga_sewa:
#     total = harga_sewa[tipe] * hari
#     print(f"Total biaya sewa {tipe} selama {hari} hari: Rp{total}")
# else:
#     print("Tipe tidak tersedia.")

# Sistem promo acak di pras_phone.id
# import random

# promo = [
#     "Gratis antigores premium",
#     "Bonus casing transparan",
#     "Cashback Rp50.000",
#     "Diskon 5%",
#     "Voucher sewa iPhone 1 hari"
# ]

# print("🎉 Promo pembelian hari ini di pras_phone.id:")
# print(random.choice(promo))

# sistem kalkukator cicilan iphone
# harga = int(input("Masukkan harga iPhone: Rp"))
# bulan = int(input("Tenor cicilan (bulan): "))

# bunga = 0.015  # 1.5% per bulan
# angsuran = (harga / bulan) + (harga * bunga)

# print(f"Cicilan per bulan: Rp{int(angsuran)}")

# Sistem cek validasi IMEI iPhone di pras_phone.id
# imei = input("Masukkan IMEI iPhone: ")

# if len(imei) == 15 and imei.isdigit():
#     print("IMEI valid. iPhone dapat dijual/sewa di pras_phone.id")
# else:
#     print("IMEI tidak valid!")

# kalkulator trade-in iphone
# harga_baru = {
#     "iPhone 12": 6000000,
#     "iPhone 13": 8000000,
#     "iPhone 14": 10000000
# }

# tipe = input("Trade-in ke model apa? ")

# if tipe in harga_baru:
#     kondisi = input("Kondisi HP lama (mulus/sedang/rusak): ").lower()

#     if kondisi == "mulus":
#         potongan = 2500000
#     elif kondisi == "sedang":
#         potongan = 1500000
#     else:
#         potongan = 500000

#     total = harga_baru[tipe] - potongan
#     print(f"Harga setelah trade-in: Rp{total}")
# else:
#     print("Model tidak tersedia.")

# sistem booking sewa iphone
# import random

# nama = input("Nama penyewa: ")
# tipe = input("iPhone yang disewa: ")
# durasi = int(input("Durasi sewa (hari): "))

# order_id = "PRS-" + str(random.randint(10000, 99999))

# print("\n=== DETAIL BOOKING ===")
# print("Nama:", nama)
# print("Tipe iPhone:", tipe)
# print("Durasi:", durasi, "hari")
# print("Order ID:", order_id)

# sistem cek garansi iphone di pras_phone.id
# imei = input("Masukkan IMEI iPhone: ")
# if len(imei) == 15 and imei.isdigit():
#     print("Garansi iPhone masih berlaku hingga 1 tahun dari tanggal pembelian.")
# else:
#     print("IMEI tidak valid!")
  
# Sistem laporan transaksi bulanan di pras_phone.id 
# transaksi = [1500000, 2500000, 3000000, 2000000, 4000000]
# bulanan = sum(transaksi)
# print(f"Total transaksi bulanan: Rp{bulanan}")

# Sistem pembelian produk dengan kelas di pras_phone.id
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
# class TokoPrasPhone:
#     def __init__(self):
#         self.produk = [
#             Produk("iPhone 12", 8000000, 5),
#             Produk("iPhone 13", 10000000, 3),
#             Produk("iPhone 14 Pro", 15000000, 2)
#         ]
#         self.total = 0

#     def tampilkan(self):
#         print("\n=== PRODUK PRAS_PHONE.ID ===")
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
        
# print("=== SELAMAT DATANG DI PRAS_PHONE.ID ===")
# toko = TokoPrasPhone()
# toko.beli()

# Sistem transaksi pembelian produk di pras_phone.id
# stok = {
#     "iPhone 12": 3,
#     "iPhone 13": 5,
#     "iPhone 14": 2,
# }
# harga = {
#     "iPhone 12": 8000000,
#     "iPhone 13": 10000000,
#     "iPhone 14": 12000000,
# }
# total_belanja = 0
# while True:
#     model = input("Masukkan model iPhone yang ingin dibeli (ketik 'selesai' untuk keluar): ")
#     if model.lower() == "selesai":
#         break
#     if model in stok:
#         jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
#         if jumlah <= stok[model]:
#             total_harga = harga[model] * jumlah
#             total_belanja += total_harga
#             stok[model] -= jumlah
#             print(f"✅ {jumlah} unit {model} berhasil dibeli seharga Rp{total_harga}")
#         else:
#             print("❌ Stok tidak cukup.")
#     else:
#         print("❌ Model tidak tersedia.")
# print(f"\nTotal belanja: Rp{total_belanja}")

# Sistem promo diskon di pras_phone.id
# total = int(input("Masukkan total pembelian: Rp"))
# if total >= 5000000:
#     diskon = 0.15
# elif total >= 3000000:
#     diskon = 0.10
# elif total >= 1000000:
#     diskon = 0.05
# else:
#     diskon = 0

# total_bayar = total - (total * diskon)
# print(f"Total bayar setelah diskon: Rp{total_bayar}")

# Sistem jadwal pengiriman di pras_phone.id
# hari = input("Masukkan hari pemesanan (Senin-Sabtu): ").lower()
# if hari in ["senin", "selasa", "rabu", "kamis", "jumat"]:
#     print("📦 Pesanan akan dikirim dalam 2 hari kerja.")
# elif hari == "sabtu":
#     print("📦 Pesanan akan dikirim pada hari Senin.")
# else:
#     print("❌ Hari tidak valid. Pemesanan hanya bisa dilakukan dari Senin hingga Sabtu.")
    
    
# sistem borongan iphone di pras_phone.id
# harha_borongan = {
#     5: 7500000,
#     10: 7000000,
#     20: 6500000
# }
# jumlah = int(input("Masukkan jumlah iPhone yang dibeli: "))
# if jumlah in harha_borongan:
#     harga_per_unit = harha_borongan[jumlah]
#     total_harga = harga_per_unit * jumlah
#     print(f"Total harga untuk {jumlah} iPhone: Rp{total_harga}")
# else:
#     print("Jumlah tidak memenuhi syarat borongan.")

# sistem antrian service iphone pras_phone.id
# queue = []

# while True:
#     print("\n1. Tambah Antrian")
#     print("2. Panggil Antrian")
#     print("3. Lihat Antrian")
#     print("4. Keluar")

#     pilihan = input("Pilih menu: ")

#     if pilihan == "1":
#         nama = input("Masukkan nama pelanggan: ")
#         queue.append(nama)
#         print(f"{nama} ditambahkan ke dalam antrian servis.")

#     elif pilihan == "2":
#         if queue:
#             pelanggan = queue.pop(0)
#             print(f"Memanggil: {pelanggan}")
#         else:
#             print("Antrian kosong.")

#     elif pilihan == "3":
#         print("Antrian:", queue)

#     elif pilihan == "4":
#         break

# selisih harga iphone di pras_phone.id dan online shop
# harga_pras = 10200000
# harga_online = 10400000

# selisih = harga_online - harga_pras

# print("Harga di pras_phone.id lebih murah Rp", selisih)

# Sistem upgrade storage iPhone di pras_phone.id
# upgrade_cost = {
#     "128GB -> 256GB": 1200000,
#     "256GB -> 512GB": 1800000
# }

# print("Pilihan upgrade storage:")
# for key in upgrade_cost:
#     print("-", key)

# pilihan = input("Pilih upgrade: ")

# if pilihan in upgrade_cost:
#     print(f"Biaya upgrade: Rp{upgrade_cost[pilihan]}")
# else:
#     print("Pilihan tidak tersedia")

# Sistem metode pembayaran di pras_phone.id
# total = int(input("Total belanja: Rp"))
# print("Metode pembayaran: cash / qris / transfer")
# metode = input("Pilih: ")

# if metode.lower() in ["cash", "qris", "transfer"]:
#     print(f"Pembayaran dengan {metode} berhasil!")
# else:
#     print("Metode tidak dikenali.")

# Sistem cek garansi iPhone di pras_phone.id
# import datetime

# pembelian = input("Tanggal pembelian (YYYY-MM-DD): ")
# pembelian_date = datetime.datetime.strptime(pembelian, "%Y-%m-%d")
# garansi = pembelian_date + datetime.timedelta(days=365)

# print("Garansi berlaku sampai:", garansi.date())

# Sistem rekomendasi iPhone berdasarkan budget di pras_phone.id
# iphone = {
#     "iPhone X": 3000000,
#     "iPhone 11": 4500000,
#     "iPhone 12": 6000000,
#     "iPhone 13": 7600000,
#     "iPhone 14 Pro": 14000000
# }

# budget = int(input("Budget kamu: Rp"))

# print("\nRekomendasi iPhone di bawah budget:")
# for model, harga in iphone.items():
#     if harga <= budget:
#         print(f"- {model} (Rp{harga})")

# Sistem flash sale di pras_phone.id
# import random
# import time

# harga_normal = 8000000
# diskon = random.randint(5, 40)  # persen diskon acak
# harga_diskon = harga_normal - (harga_normal * diskon / 100)

# print("🔥 FLASH SALE pras_phone.id! 🔥")
# for i in range(3, 0, -1):
#     print("Mulai dalam", i)
#     time.sleep(1)

# print(f"Harga normal: Rp{harga_normal}")
# print(f"Diskon {diskon}%!")
# print(f"Harga flash sale: Rp{int(harga_diskon)}")

# Sistem cek stok iPhone di pras_phone.id
# inventory = {
#     "iPhone 12": 2,
#     "iPhone 13": 0,
#     "iPhone 14": 1,
#     "iPhone 15 Pro": 5
# }

# for model, stock in inventory.items():
#     if stock <= 1:
#         print(f"⚠️ WARNING: {model} needs restock! Only {stock} left.")

# Sistem rating pelanggan di pras_phone.id
# ratings = []
# print("Rate your experience at pras_phone.id (1–5)")

# for i in range(3):
#     rating = int(input(f"Customer {i+1} rating: "))
#     ratings.append(rating)

# avg = sum(ratings)/len(ratings)
# print("Average rating:", round(avg, 2))

# Sistem estimasi harga jual kembali iPhone di pras_phone.id
# iphone_price = 12000000
# age = int(input("Years used: "))

# depreciation = 0.15  # 15% loss per year
# resell_value = iphone_price * ((1 - depreciation) ** age)

# print("Estimated resell value: Rp", int(resell_value))

# Sistem rekomendasi iPhone berdasarkan fitur di pras_phone.id
# user = input("What feature do you need? (camera/battery/performance): ")

# if user == "camera":
#     print("Recommended: iPhone 15 Pro Max")
# elif user == "battery":
#     print("Recommended: iPhone 13 or 14 Plus")
# elif user == "performance":
#     print("Recommended: iPhone 15 Pro")
# else:
#     print("No recommendation available.")

# Sistem pemilihan supplier terbaik di pras_phone.id
# supplier = {
#     "Supplier A": 9500000,
#     "Supplier B": 9700000,
#     "Supplier C": 9400000
# }

# best_supplier = min(supplier, key=supplier.get)

# print("Best supplier for stock purchase:", best_supplier)
# print("Price:", supplier[best_supplier])

# Sistem reward poin untuk pembelian di pras_phone.id
# purchase = int(input("Enter purchase amount: Rp"))
# points = purchase // 50000  # 1 point per 50k spending

# print("You earned", points, "loyalty points!")

# Sistem pembelian produk dengan diskon berdasarkan jumlah di pras_phone.id
# harga = 7500000
# qty = int(input("How many units to order? "))

# if qty >= 10:
#     diskon = 0.07
# elif qty >= 5:
#     diskon = 0.05
# else:
#     diskon = 0.02

# total = harga * qty * (1 - diskon)

# print(f"Total price after discount: Rp{int(total)}")

# Sistem pajak berdasarkan provinsi di pras_phone.id
# harga = int(input("Harga iPhone: Rp"))
# provinsi = input("Provinsi (Jawa/Bali/Sumatra): ").lower()

# pajak = {
#     "jawa": 0.11,
#     "bali": 0.10,
#     "sumatra": 0.12
# }

# if provinsi in pajak:
#     total = harga + (harga * pajak[provinsi])
#     print(f"Total setelah pajak: Rp{int(total)}")
# else:
#     print("Provinsi tidak terdaftar.")

# Sistem denda keterlambatan pengembalian iPhone di pras_phone.id
# hari_sewa = int(input("Hari seharusnya dikembalikan: "))
# hari_kembali = int(input("Hari aktual dikembalikan: "))

# late = hari_kembali - hari_sewa

# if late <= 0:
#     print("Tidak ada denda")
# else:
#     denda = late * 30000
#     print(f"Denda keterlambatan: Rp{denda}")

# Sistem cek status garansi iPhone di pras_phone.id
# bulan = int(input("Berapa bulan sejak pembelian? "))

# if bulan <= 3:
#     kategori = "Full Warranty"
# elif bulan <= 6:
#     kategori = "Limited Warranty"
# elif bulan <= 12:
#     kategori = "Service-Only Warranty"
# else:
#     kategori = "Warranty Expired"

# print("Status garansi:", kategori)

# Sistem kategori kondisi iPhone di pras_phone.id
# screen = int(input("Skor layar (1–10): "))
# battery = int(input("Skor baterai (1–10): "))
# body = int(input("Skor body (1–10): "))

# avg = (screen + battery + body) / 3

# if avg >= 9:
#     kondisi = "Super Mint"
# elif avg >= 7:
#     kondisi = "Mint"
# elif avg >= 5:
#     kondisi = "Normal"
# else:
#     kondisi = "Below Average"

# print("Kategori kondisi iPhone:", kondisi)


## Sistem tawar-menawar harga iPhone di pras_phone.id
# import random

# price = int(input("Your offer: Rp"))

# responses = [
#     "Deal!",
#     "Boleh, tapi harga pas ya.",
#     "Tidak bisa, terlalu rendah.",
#     "Tambah dikit lagi boleh.",
#     "Saya cek dulu stok dan kondisi unit."
# ]

# print("Seller:", random.choice(responses))

# Sistem invoice pembelian iPhone di pras_phone.id
# import random

# nama = input("Nama pelanggan: ")
# barang = input("Model iPhone: ")
# harga = int(input("Harga: Rp"))

# invoice_id = "INV-" + str(random.randint(1000, 9999))

# print("\n===== INVOICE =====")
# print("ID:", invoice_id)
# print("Nama:", nama)
# print("Barang:", barang)
# print("Total: Rp", harga)
# print("===================")

# Sistem hitung profit jual dan sewa iPhone di pras_phone.id
# harga_beli = int(input("Modal beli iPhone: Rp"))
# harga_jual = int(input("Harga jual final: Rp"))
# sewa_income = int(input("Total pemasukan dari sewa: Rp"))

# profit = (harga_jual + sewa_income) - harga_beli

# print("Total profit keseluruhan: Rp", profit)


# Sistem pengingat servis iPhone di pras_phone.id
# import datetime
# last_service = input("Tanggal servis terakhir (YYYY-MM-DD): ")
# last_service_date = datetime.datetime.strptime(last_service, "%Y-%m-%d")
# next_service_date = last_service_date + datetime.timedelta(days=180)

# print("Tanggal servis berikutnya:", next_service_date.strftime("%Y-%m-%d"))

# Sistem hitung volume bola
# import math
# radius = float(input("Masukkan jari-jari bola: "))
# volume = (4/3) * math.pi * radius**3
# print(f"Volume bola dengan jari-jari {radius} adalah {volume:.2f}")

# Sistem operasi pecahan dasar
# from fractions import Fraction  
# a = Fraction(input("Masukkan pecahan pertama (misal 1/2): "))
# b = Fraction(input("Masukkan pecahan kedua (misal 3/4): "))

# print("Penjumlahan:", a + b)
# print("Pengurangan:", a - b)
# print("Perkalian:", a * b)
# print("Pembagian:", a / b)
# print("Pecahan pertama dalam desimal:", float(a))
# print("Pecahan kedua dalam desimal:", float(b))
# print("Pecahan pertama dalam persen:", float(a) * 100, "%")
# print("Pecahan kedua dalam persen:", float(b) * 100, "%")

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
#             Produk("Dumbbell", 200000, 10),
#             Produk("Yoga Mat", 150000, 8),
#             Produk("Gloves", 80000, 20),]
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
#                 print("❌ Produk tidak ditemukan.")
#         print(f"\n💰 Total Bayar: Rp{self.total}")
# print("=== SELAMAT DATANG DI TOKO GYM ===")
# toko = TokoGym()
# toko.beli()


# sistem pembuatan password kuat
# import random
# import string
# def generate_password(length):
#     if length < 8:
#         return "Panjang password minimal 8 karakter."
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password
# panjang = int(input("Masukkan panjang password yang diinginkan: "))
# print("Password kuat yang dihasilkan:", generate_password(panjang))

# Sistem validasi password
# import string


# def validate_password(password):
#     if len(password) < 8:
#         return "Password harus memiliki minimal 8 karakter."
#     if not any(char.isupper() for char in password):
#         return "Password harus mengandung setidaknya satu huruf kapital."
#     if not any(char.islower() for char in password):
#         return "Password harus mengandung setidaknya satu huruf kecil."
#     if not any(char.isdigit() for char in password):
#         return "Password harus mengandung setidaknya satu angka."
#     if not any(char in string.punctuation for char in password):
#         return "Password harus mengandung setidaknya satu karakter khusus."
#     return "Password valid dan kuat."
# password_input = input("Masukkan password untuk divalidasi: ")
# print(validate_password(password_input))

# sistem cek diskon pembelian di toko gym
# harga = float(input("Masukkan harga barang: "))
# diskon = float(input("Masukkan diskon (%): "))

# potongan = harga * (diskon / 100)
# total = harga - potongan

# print(f"Total setelah diskon: Rp{total}")

# Sistem hitung kalori makanan di toko gym
# makanan = {
#     "nasi": 200,
#     "ayam": 250,
#     "telur": 78,
#     "roti": 120
# }

# total = 0

# while True:
#     pilih = input("Masukkan makanan (ketik 'stop' untuk selesai): ")
#     if pilih == "stop":
#         break
#     if pilih in makanan:
#         total += makanan[pilih]
#     else:
#         print("Makanan tidak ditemukan.")

# print("Total kalori:", total)

# Sistem cek angka genap atau ganjil
# angka = int(input("Masukkan angka: "))

# if angka % 2 == 0:
#     print("Angka genap")
# else:
#     print("Angka ganjil")

# Sistem login sederhana    
# username = "admin"
# password = "12345"

# u = input("Username: ")
# p = input("Password: ")

# if u == username and p == password:
#     print("Login berhasil!")
# else:
#     print("Login gagal!")

# # Sistem konversi suhu Celsius ke Fahrenheit
# c = float(input("Masukkan suhu Celsius: "))
# f = (c * 9/5) + 32

# print("Hasil dalam Fahrenheit:", f)

# Sistem rekomendasi motivasi harian
# import random

# motivasi = [
#     "Tetap semangat!",
#     "Kamu pasti bisa!",
#     "Jangan menyerah!",
#     "Fokus dan terus maju!",
#     "Proses tidak akan mengkhianati hasil."
# ]

# print("Motivasi hari ini:", random.choice(motivasi))

# Sistem hitung ongkos kirim berdasarkan berat paket
# berat = float(input("Masukkan berat paket (kg): "))
# tarif = 12000 + (berat * 4000)

# total = berat * tarif

# print(f"Total ongkos kirim: Rp{total}")


# sistem cek kesehatan suhu badan
# suhu = float(input("Masukkan suhu badan (°C): "))
# if suhu < 36.5:
#     status = "Suhu badan rendah (hipotermia)"
# elif 36.5 <= suhu <= 37.5:
#     status = "Suhu badan normal"
# else:
#     status = "Suhu badan tinggi (demam)"
# print("Status kesehatan:", status)


# sistem kalkulator BMI
# berat = float(input("Masukkan berat badan (kg): "))
# tinggi = float(input("Masukkan tinggi badan (m): "))
# bmi = berat / (tinggi ** 2)
# print(f"Indeks Massa Tubuh (BMI): {bmi:.2f}")
# if bmi < 18.5:
#     kategori = "Kurus"
# elif 18.5 <= bmi < 24.9:
#     kategori = "Normal"
# elif 25 <= bmi < 29.9:
#     kategori = "Kelebihan berat badan"
# else:
#     kategori = "Obesitas"
# print("Kategori BMI:", kategori)

# Sistem pendaftaran kelas gym dengan stok terbatas
# kelas = {
#     "Yoga": 5,
#     "Pilates": 3,
#     "Zumba": 4
# }
# pilih = input("Pilih kelas yang ingin didaftarkan (Yoga/Pilates/Zumba): ")
# if pilih in kelas:
#     if kelas[pilih] > 0:
#         kelas[pilih] -= 1
#         print(f"Pendaftaran kelas {pilih} berhasil! Sisa kuota: {kelas[pilih]}")
#     else:
#         print(f"Maaf, kelas {pilih} sudah penuh.")
# else:
#     print("Kelas tidak tersedia.")
    
# Sistem cek kesehatan jantung
# detak = int(input("Masukkan detak jantung per menit: "))
# if detak < 60:
#     status = "Bradikardia (detak jantung rendah)"
# elif 60 <= detak <= 100:
#     status = "Normal"
# else:
#     status = "Tachikardia (detak jantung tinggi)"
# print("Status kesehatan jantung:", status)

# Sistem cek kebutuhan air harian
# berat = float(input("Masukkan berat badan (kg): "))
# kebutuhan_air = berat * 35  # ml per kg
# print(f"Kebutuhan air harian Anda: {int(kebutuhan_air)} ml")

# Sistem hitung kalori terbakar saat olahraga
# durasi = float(input("Masukkan durasi olahraga (menit): "))
# met = float(input("Masukkan MET aktivitas: "))
# berat = float(input("Masukkan berat badan (kg): "))
# kalori = (met * 3.5 * berat / 200) * durasi
# print(f"Kalori terbakar: {int(kalori)} kkal")

# Sistem cek tingkat stres
# skor = int(input("Masukkan skor stres Anda (1-10): "))
# if skor <= 3:
#     tingkat = "Rendah"
# elif 4 <= skor <= 7:
#     tingkat = "Sedang"
# else:
#     tingkat = "Tinggi"
# print("Tingkat stres Anda:", tingkat)

# Sistem hitung tarif parkir di toko gym
# jam = int(input("Masukkan durasi parkir (jam): "))
# tarif = 3000

# total = jam * tarif
# print(f"Total bayar parkir: Rp{total}")

# Sistem hitung luas segitiga
# alas = float(input("Masukkan alas: "))
# tinggi = float(input("Masukkan tinggi: "))

# luas = 0.5 * alas * tinggi
# print("Luas segitiga:", luas)

# Sistem daftar belanja di toko gym
# belanja = []

# while True:
#     item = input("Tambah item (ketik 'selesai'): ")
#     if item == "selesai":
#         break
#     belanja.append(item)

# print("Daftar belanja kamu:", belanja)

# Sistem penilaian siswa
# nilai = int(input("Masukkan nilai: "))

# if nilai >= 80:
#     print("Grade A")
# elif nilai >= 70:
#     print("Grade B")
# elif nilai >= 60:
#     print("Grade C")
# else:
#     print("Grade D")

# Sistem kalkulator BMI
# berat = float(input("Masukkan berat (kg): "))
# tinggi = float(input("Masukkan tinggi (m): "))

# bmi = berat / (tinggi ** 2)
# print("BMI:", round(bmi, 2))

# if bmi < 18.5:
#     print("Kurus")
# elif bmi < 25:
#     print("Normal")
# else:
#     print("Overweight")

# Sistem penjumlahan angka
# jumlah = int(input("Berapa angka yang ingin dijumlahkan? "))
# total = 0

# for i in range(jumlah):
#     angka = float(input(f"Angka ke-{i+1}: "))
#     total += angka

# print("Total:", total)

# Sistem pemesanan tiket nonton film
# film = ["Avatar", "Naruto", "One Piece", "Joker 2"]

# print("Daftar Film:")
# for i, f in enumerate(film):
#     print(f"{i+1}. {f}")

# pilih = int(input("Pilih film (1-4): "))
# tiket = int(input("Jumlah tiket: "))

# harga = 35000
# total = harga * tiket

# print(f"Kamu memilih film {film[pilih-1]}")
# print(f"Total bayar: Rp{total}")

# Sistem cek kelayakan kredit berdasarkan rasio hutang
# penghasilan = int(input("Masukkan penghasilan bulanan: "))
# hutang = int(input("Masukkan total hutang bulanan: "))

# rasio = hutang / penghasilan

# print("Rasio hutang:", round(rasio, 2))

# if rasio < 0.3:
#     print("Status: Sangat Layak Kredit")
# elif rasio < 0.5:
#     print("Status: Layak Kredit")
# else:
#     print("Status: Tidak Layak Kredit")

# Sistem pembelian buku di toko online
# buku = {
#     "Python Dasar": 85000,
#     "Java OOP": 92000,
#     "AI for Beginner": 120000
# }

# print("Daftar Buku:")
# for b, h in buku.items():
#     print(b, "- Rp", h)

# pilih = input("Pilih judul buku: ")
# jumlah = int(input("Jumlah beli: "))

# total = buku.get(pilih, 0) * jumlah
# print("Total pembayaran: Rp", total)

# Sistem diskon pembelian di toko gym
# harga = float(input("Masukkan total belanja: "))

# if harga >= 500000:
#     diskon = 0.25
# elif harga >= 250000:
#     diskon = 0.15
# else:
#     diskon = 0.05

# total = harga - (harga * diskon)

# print(f"Diskon: {diskon*100}%")
# print(f"Total bayar: Rp{total}")

# Sistem rekap absen mahasiswa
# absen = {}

# for i in range(3):
#     nama = input("Nama mahasiswa: ")
#     status = input("Status (Hadir/Tidak): ")
#     absen[nama] = status

# print("Rekap Absen:")
# for n, s in absen.items():
#     print(n, "-", s)

# Sistem cek angka genap atau ganjil
# angka = int(input("Masukkan angka: "))

# if angka % 2 == 0:
#     print("Angka ini GENAP")
# else:
#     print("Angka ini GANJIL")

# Sistem hitung ongkos kirim paket di pras_phone.id
# berat = float(input("Masukkan berat paket (kg): "))
# jarak = float(input("Masukkan jarak (km): "))

# ongkir = (berat * 5000) + (jarak * 1500)

# print("Total ongkir: Rp", ongkir)

# Sistem kategori usia di pras_phone.id
# usia = int(input("Masukkan usia: "))

# if usia <= 12:
#     print("Kategori: Anak-anak")
# elif usia <= 17:
#     print("Kategori: Remaja")
# elif usia <= 59:
#     print("Kategori: Dewasa")
# else:
#     print("Kategori: Lansia")

# Sistem pembelian minuman di toko gym
# menu = {
#     "Es Teh": 5000,
#     "Es Jeruk": 7000,
#     "Kopi Hitam": 8000,
#     "Cappuccino": 12000
# }

# print("=== MENU MINUMAN ===")
# for m, h in menu.items():
#     print(f"{m} - Rp{h}")

# pesan = input("Pilih minuman: ")
# jumlah = int(input("Jumlah: "))

# total = menu.get(pesan, 0) * jumlah
# print("Total bayar: Rp", total)

# Sistem penilaian akhir siswa
# nilai = int(input("Masukkan nilai akhir: "))

# if nilai >= 90:
#     print("Grade: A")
# elif nilai >= 75:
#     print("Grade: B")
# elif nilai >= 60:
#     print("Grade: C")
# else:
#     print("Grade: D - Harus Remedial")

# username = "admin"
# password = "12345"

# u = input("Masukkan username: ")
# p = input("Masukkan password: ")

# if u == username and p == password:
#     print("Login Berhasil!")
# else:
#     print("Login Gagal!")

# Sistem hitung pajak penghasilan sederhana
# gaji = float(input("Masukkan gaji bulanan: "))

# if gaji <= 4000000:
#     pajak = 0.05
# elif gaji <= 8000000:
#     pajak = 0.10
# else:
#     pajak = 0.15

# total_pajak = gaji * pajak
# print("Pajak yang harus dibayar: Rp", total_pajak)

# Sistem pembuatan username dari nama lengkap
# nama = input("Masukkan nama lengkap: ")

# username = nama.lower().replace(" ", "_")
# print("Username Anda:", username)


# Sistem cek bilangan prima
# n = int(input("Masukkan angka: "))

# prima = True

# if n < 2:
#     prima = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             prima = False
#             break

# if prima:
#     print(n, "adalah bilangan prima")
# else:
#     print(n, "bukan bilangan prima")


# Sistem kalkulator BMI
# berat = float(input("Masukkan berat (kg): "))
# tinggi = float(input("Masukkan tinggi (m): "))

# bmi = berat / (tinggi ** 2)
# print("BMI:", round(bmi, 2))

# if bmi < 18.5:
#     print("Status: Kurang berat badan")
# elif bmi < 25:
#     print("Status: Normal")
# elif bmi < 30:
#     print("Status: Kelebihan berat badan")
# else:
#     print("Status: Obesitas")


# Sistem hitung durasi sewa iPhone di pras_phone.id
# hari = int(input("Masukkan durasi sewa (hari): "))
# tarif_harian = 150000
# total_bayar = hari * tarif_harian
# print("Total bayar: Rp", total_bayar)
# if hari >= 7:
#     diskon = 0.10
#     total_bayar -= total_bayar * diskon
#     print(f"Diskon 10% diterapkan! Total bayar setelah diskon: Rp{int(total_bayar)}")

# Sistem hitung gaji karyawan toko gym
# jam_kerja = int(input("Masukkan jam kerja dalam seminggu: "))
# tarif_per_jam = 50000
# if jam_kerja <= 40:
#     gaji = jam_kerja * tarif_per_jam
# else:
#     lembur = jam_kerja - 40
#     gaji = (40 * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
# print("Total gaji: Rp", int(gaji))


# # Sistem pembelian produk dengan kelas di pras_phone.id
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
# class TokoPrasPhone:
#     def __init__(self):
#         self.produk = [
#             Produk("iPhone 12", 8000000, 3),
#             Produk("iPhone 13", 10000000, 5),
#             Produk("iPhone 14", 12000000, 2),]
#         self.total = 0
#     def tampilkan(self):
#         print("\n=== PRODUK PRAS_PHONE.ID ===")
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
#                 print("❌ Produk tidak ditemukan.")
#         print(f"\n💰 Total Bayar: Rp{self.total}")
# print("=== SELAMAT DATANG DI PRAS_PHONE.ID ===")
# toko = TokoPrasPhone()
# toko.beli()
# toko.jual(2)

# Sistem pemesanan tiket nonton film di pras_phone.id
# film = {
#     "Avengers": 45000,
#     "Naruto The Movie": 35000,
#     "Transformers": 50000
# }

# print("=== DAFTAR FILM ===")
# for f, h in film.items():
#     print(f"{f} - Rp{h}")

# pilih = input("Pilih film: ")
# jumlah = int(input("Jumlah tiket: "))

# total = film.get(pilih, 0) * jumlah
# print("Total bayar: Rp", total)

# Sistem konversi waktu dari detik ke jam, menit, dan detik
# detik = int(input("Masukkan total detik: "))

# jam = detik // 3600
# detik %= 3600
# menit = detik // 60
# detik %= 60

# print(f"Hasil: {jam} jam, {menit} menit, {detik} detik")

# Sistem pembuatan password acak
# import random
# import string

# panjang = int(input("Masukkan panjang password: "))

# karakter = string.ascii_letters + string.digits
# password = "".join(random.choice(karakter) for _ in range(panjang))

# print("Password Anda:", password)

# Sistem voting sederhana
# votes = {"Andi": 0, "Budi": 0, "Cici": 0}

# for i in range(5):
#     pilih = input("Pilih kandidat (Andi/Budi/Cici): ")
#     if pilih in votes:
#         votes[pilih] += 1

# print("Hasil voting:", votes)

# Sistem hitung ongkos kirim berdasarkan jarak di pras_phone.id
# jarak = float(input("Masukkan jarak pengiriman (km): "))

# if jarak <= 5:
#     ongkir = 10000
# elif jarak <= 15:
#     ongkir = 20000
# else:
#     ongkir = 30000

# print("Total ongkir: Rp", ongkir)

# Sistem cek kesehatan berdasarkan suhu tubuh
# suhu = float(input("Masukkan suhu tubuh: "))

# if suhu < 36:
#     print("Status: Suhu rendah")
# elif suhu <= 37.5:
#     print("Status: Normal")
# else:
#     print("Status: Demam")

# sistem hitung biaya parkir di toko gym
# jam = int(input("Berapa jam parkir? "))

# biaya = 5000 + (jam - 1) * 3000 if jam > 1 else 5000
# print("Biaya parkir: Rp", biaya)

#
# nama = input("Masukkan nama lengkap: ")

# bagian = nama.split()
# print("Nama depan:", bagian[0])
# print("Nama belakang:", bagian[-1])

# sistem hitung jumlah kata dalam kalimat
# kalimat = input("Masukkan kalimat: ")

# jumlah = len(kalimat.split())
# print("Jumlah kata:", jumlah)

# Sistem konversi kecepatan dari km/h ke m/s
# kmh = float(input("Masukkan kecepatan (km/h): "))

# ms = kmh / 3.6
# print("Kecepatan dalam m/s:", round(ms, 2))

# Sistem pemilihan pemenang giveaway di pras_phone.id
# import random

# peserta = ["Andi", "Budi", "Citra", "Doni", "Eka", "Farhan"]

# pemenang = random.choice(peserta)
# print("Pemenang giveaway adalah:", pemenang)

# Sistem cek promo pembelian di toko gym
# harga = float(input("Masukkan harga barang: Rp "))

# if harga >= 2000000:
#     promo = "Gratis Keyboard + Mouse"
# elif harga >= 1000000:
#     promo = "Gratis Mouse"
# else:
#     promo = "Tidak ada promo"

# print("Promo yang didapat:", promo)

# Sistem konversi waktu dari jam ke hari dan jam
# jam = int(input("Masukkan jumlah jam: "))

# hari = jam // 24
# sisa_jam = jam % 24

# print(f"Hasil: {hari} hari {sisa_jam} jam")

# Sistem rating pelanggan di pras_phone.id
# rating = int(input("Masukkan rating (1-5): "))

# if rating == 5:
#     print("Rating: Sangat Bagus ⭐⭐⭐⭐⭐")
# elif rating == 4:
#     print("Rating: Bagus ⭐⭐⭐⭐")
# elif rating == 3:
#     print("Rating: Cukup ⭐⭐⭐")
# elif rating == 2:
#     print("Rating: Buruk ⭐⭐")
# else:
#     print("Rating: Sangat Buruk ⭐")

# Sistem cek tahun kabisat
# tahun = int(input("Masukkan tahun: "))

# if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     print("Tahun kabisat")
# else:
#     print("Bukan tahun kabisat")

# Sistem tebak warna
# import random

# warna = ["merah", "biru", "hijau", "kuning"]
# jawaban = random.choice(warna)

# tebakan = input("Tebak warna (merah/biru/hijau/kuning): ")

# if tebakan == jawaban:
#     print("Benar!")
# else:
#     print("Salah, warna yang benar adalah:", jawaban)

# sistem kategori umur di pras_phone.id
# umur = int(input("Masukkan umur: "))

# if umur < 12:
#     print("Kategori: Anak-anak")
# elif umur < 18:
#     print("Kategori: Remaja")
# elif umur < 60:
#     print("Kategori: Dewasa")
# else:
#     print("Kategori: Lansia")

# sistem konversi mata uang dari rupiah ke USD
# rupiah = float(input("Masukkan jumlah rupiah: Rp "))
# kurs_usd = 15500

# usd = rupiah / kurs_usd
# print("Hasil dalam USD: $", round(usd, 2))

# sistem pembelian paket data di pras_phone.id
# paket = {
#     "1GB": 15000,
#     "5GB": 45000,
#     "10GB": 80000
# }

# print("=== PAKET DATA ===")
# for p, h in paket.items():
#     print(f"{p} - Rp{h}")

# pilih = input("Pilih paket: ")
# total = paket.get(pilih, 0)

# print("Total bayar: Rp", total)


# # Sistem hitung luas permukaan kubus
# sisi = float(input("Masukkan panjang sisi kubus: "))

# luas = 6 * (sisi ** 2)
# print("Luas permukaan kubus:", luas)

# Sistem validasi email sederhana
# email = input("Masukkan email: ")

# if "@" in email and "." in email:
#     print("Email valid")
# else:
#     print("Email tidak valid")

# Sistem validasi golongan darah
# gol = input("Masukkan golongan darah (A/B/AB/O): ").upper()

# valid = ["A", "B", "AB", "O"]

# if gol in valid:
#     print("Golongan darah valid:", gol)
# else:
#     print("Input tidak dikenal")

# Sistem tarik tunai sederhana
# saldo = 1200000

# print("Saldo Anda:", saldo)
# tarik = int(input("Masukkan jumlah penarikan: "))

# if tarik <= saldo:
#     saldo -= tarik
#     print("Penarikan berhasil! Sisa saldo:", saldo)
# else:
#     print("Saldo tidak cukup!")

# Sistem hitung waktu tempuh berdasarkan jarak dan kecepatan
# jarak = float(input("Masukkan jarak tempuh (km): "))
# kecepatan = float(input("Masukkan kecepatan (km/jam): "))

# waktu = jarak / kecepatan
# print("Waktu tempuh:", round(waktu, 2), "jam")

# Sistem hitung rata-rata nilai siswa
# nilai = []
# jumlah = int(input("Berapa jumlah siswa? "))

# for i in range(jumlah):
#     n = float(input(f"Nilai siswa ke-{i+1}: "))
#     nilai.append(n)

# rata = sum(nilai) / len(nilai)
# print("Rata-rata nilai kelas:", round(rata, 2))


# Sistem hitung total belanja dengan pajak
# total = 0
# while True:
#     harga = float(input("Masukkan harga barang (0 untuk selesai): Rp "))
#     if harga == 0:
#         break
#     total += harga
# pajak = total * 0.1
# grand_total = total + pajak
# print(f"Total belanja: Rp{int(total)}")
# print(f"Pajak (10%): Rp{int(pajak)}")
# print(f"Grand Total: Rp{int(grand_total)}")

# Sistem hitung total belanja dengan diskon member
# member = input("Apakah Anda punya kartu member? (y/n): ")

# belanja = float(input("Total belanja: Rp "))

# if member.lower() == "y":
#     total = belanja * 0.90  # diskon 10%
# else:
#     total = belanja

# print("Total bayar: Rp", total)

# Sistem cari nilai terbesar dari 5 angka
# angka = []

# for i in range(5):
#     x = int(input(f"Masukkan angka ke-{i+1}: "))
#     angka.append(x)

# print("Nilai terbesar adalah:", max(angka))


# sistem konversi suhu dari Celcius ke Fahrenheit dan Kelvin
# c = float(input("Masukkan suhu dalam Celcius: "))

# f = (c * 9/5) + 32
# k = c + 273.15

# print("Fahrenheit:", round(f, 2))
# print("Kelvin:", round(k, 2))


# # Sistem undian nomor di pras_phone.id
# import random

# print("Mengundi nomor...")

# nomor = random.randint(1000, 9999)
# print("Nomor undian Anda:", nomor)

# Sistem cek kelulusan siswa
# nilai = float(input("Masukkan nilai akhir: "))

# if nilai >= 75:
#     print("Status: Lulus")
# else:
#     print("Status: Tidak Lulus")

# Sistem login sederhana di pras_phone.id
# username = "admin"
# password = "12345"

# u = input("Masukkan username: ")
# p = input("Masukkan password: ")

# if u == username and p == password:
#     print("Login berhasil!")
# else:
#     print("Login gagal!")

# Sistem cek stok iPhone di pras_phone.id
# iphones = {
#     "iPhone 11": 5,
#     "iPhone 12": 3,
#     "iPhone 13": 0,
#     "iPhone 14 Pro": 2
# }

# def cek_stok(model):
#     return f"Stok {model}: {'Tersedia' if iphones.get(model,0) > 0 else 'Habis'}"

# print(cek_stok("iPhone 13"))
# print(cek_stok("iPhone 12"))

# Sistem hitung biaya sewa iPhone di pras_phone.id
# harga_sewa = {
#     "iPhone 11": 45000,
#     "iPhone 12": 60000,
#     "iPhone 13": 75000,
#     "iPhone 14": 90000
# }

# def hitung_sewa(model, hari):
#     return hari * harga_sewa.get(model, 0)

# print("Total biaya:", hitung_sewa("iPhone 14", 5))

# Sistem checkout pembelian di pras_phone.id
# def checkout(nama, model, harga):
#     return f"Pesanan atas nama {nama} untuk {model} berhasil! Total pembayaran: Rp{harga:,}"

# print(checkout("Dicky", "iPhone 12 128GB", 7999000))

# Sistem hitung diskon pembelian di pras_phone.id
# def hitung_diskon(harga):
#     diskon = 0.10  # 10%
#     final = harga - (harga * diskon)
#     return final

# print("Harga setelah diskon:", hitung_diskon(10500000))

# Sistem cek garansi iPhone di pras_phone.id
# import random

# def cek_garansi(imei):
#     status = ["Aktif", "Kadaluarsa"]
#     return f"IMEI {imei}: Garansi {random.choice(status)}"

# print(cek_garansi("356789105432100"))

# Sistem kategori pembelian iPhone di pras_phone.id
# def kategori(model):
#     data = {
#         "iPhone 11": "Bekas",
#         "iPhone 12": "Bekas",
#         "iPhone 13": "Baru",
#         "iPhone 14 Pro": "Sewa & Jual"
#     }
#     return f"{model} tersedia untuk kategori: {data.get(model, 'Tidak ditemukan')}"

# print(kategori("iPhone 14 Pro"))

# Sistem negosiasi harga iPhone di pras_phone.id
# def nego(harga_awal, tawaran):
#     if tawaran >= harga_awal * 0.9:
#         return f"Deal! Harga disetujui: Rp{tawaran:,}"
#     else:
#         return "Maaf, tawaran terlalu rendah."

# print(nego(8500000, 8000000))

# Sistem cek kondisi iPhone di pras_phone.id
# def cek_kondisi(baterai, fisik, lcd):
#     nilai = (baterai + fisik + lcd) / 3
#     if nilai >= 90:
#         return "Kondisi: Excellent"
#     elif nilai >= 75:
#         return "Kondisi: Good"
#     else:
#         return "Kondisi: Fair"

# print(cek_kondisi(88, 92, 85))

# Sistem hitung poin pembelian di pras_phone.id
# def hitung_poin(total_belanja):
#     poin = total_belanja // 50000
#     return f"Poin yang didapat: {poin}"

# print(hitung_poin(1250000))

# Sistem chat sederhana dengan pembeli di pras_phone.id
# def chat_pembeli(pesan):
#     if "harga" in pesan.lower():
#         return "Harga mulai dari Rp 5.500.000 – Rp 25.000.000 tergantung model."
#     elif "stok" in pesan.lower():
#         return "Stok masih tersedia, silakan pilih model."
#     else:
#         return "Baik, ada yang bisa dibantu terkait iPhone?"

# print(chat_pembeli("Bang berapa harga iPhone 12?"))

# Sistem validasi transfer pembayaran di pras_phone.id
# import random

# def validasi_transfer(nama, jumlah):
#     if random.choice([True, False]):
#         return f"Pembayaran oleh {nama} sebesar Rp{jumlah:,} telah diterima."
#     else:
#         return "Pembayaran belum terverifikasi, coba cek kembali bukti transfer."

# print(validasi_transfer("Dicky", 6500000))

# Sistem estimasi depresiasi nilai iPhone di pras_phone.id
# def depresiasi(harga_awal, tahun):
#     return harga_awal * (0.80 ** tahun)

# print("Estimasi nilai:", depresiasi(12000000, 2))

# Sistem antrian pembeli di pras_phone.id
# antrian = []

# def tambah_antrian(nama):
#     antrian.append(nama)
#     return f"{nama} masuk antrian. Nomor antrian: {len(antrian)}"

# print(tambah_antrian("Dicky"))
# print(tambah_antrian("Andi"))
# print("Total antrian:", antrian)

# Sistem buat order ID unik di pras_phone.id
# import random
# import datetime

# def buat_order_id():
#     now = datetime.datetime.now().strftime("%Y%m%d%H%M")
#     rand = random.randint(100, 999)
#     return f"PRS-{now}-{rand}"

# print("Order ID:", buat_order_id())

# Sistem konversi nilai angka ke huruf
# def nilai_huruf(nilai):
#     if nilai >= 85:
#         return "A"
#     elif nilai >= 70:
#         return "B"
#     elif nilai >= 55:
#         return "C"
#     else:
#         return "D"

# print(nilai_huruf(78))

# Sistem hitung IPK dari daftar nilai
# def hitung_ipk(nilai):
#     total = sum(nilai)
#     return round(total / len(nilai), 2)

# print(hitung_ipk([3.5, 3.7, 3.2, 3.8]))

# Sistem cari kata terpanjang dalam kalimat
# def kata_terpanjang(kalimat):
#     return max(kalimat.split(), key=len)

# print(kata_terpanjang("belajar python untuk skripsi"))

# Sistem login sederhana di pras_phone.id
# def login(username, password):
#     if username == "admin" and password == "1234":
#         return "Login berhasil"
#     return "Login gagal"

# print(login("admin", "1234"))

# Sistem filter angka genap dari daftar
# def filter_genap(data):
#     return [x for x in data if x % 2 == 0]

# print(filter_genap([1,2,3,4,5,6,7,8]))

# Sistem hitung frekuensi kemunculan huruf dalam teks
# def frekuensi(teks):
#     hasil = {}
#     for huruf in teks:
#         hasil[huruf] = hasil.get(huruf, 0) + 1
#     return hasil

# print(frekuensi("pseudocode"))

# Sistem menu pilihan sederhana
# def menu(pilihan):
#     opsi = {
#         1: "Lihat data",
#         2: "Tambah data",
#         3: "Keluar"
#     }
#     return opsi.get(pilihan, "Pilihan tidak valid")

# print(menu(2))

# Sistem hitung total belanja dengan pajak di pras_phone.id
# def total_belanja(harga_list, pajak=0.1):
#     subtotal = sum(harga_list)
#     return subtotal + (subtotal * pajak)

# print(total_belanja([50000, 75000, 120000]))

# Sistem cek umur dewasa atau belum
# def cek_umur(umur):
#     return "Dewasa" if umur >= 18 else "Belum Dewasa"

# print(cek_umur(17))

# Sistem cari angka terbesar dalam daftar
# def angka_terbesar(data):
#     return max(data)

# print(angka_terbesar([10, 45, 23, 89, 12]))

# Sistem hitung jumlah kata dalam teks
# def jumlah_kata(teks):
#     return len(teks.split())

# print(jumlah_kata("belajar python setiap hari"))

# Sistem konversi menit ke jam dan menit
# def menit_ke_jam(menit):
#     jam = menit // 60
#     sisa = menit % 60
#     return f"{jam} jam {sisa} menit"

# print(menit_ke_jam(135))

# Sistem validasi password minimal 8 karakter
# def valid_password(password):
#     return len(password) >= 8

# print(valid_password("belajar123"))

# Sistem cek status kelulusan berdasarkan rata-rata nilai
# def status_lulus(nilai):
#     rata = sum(nilai) / len(nilai)
#     return "Lulus" if rata >= 70 else "Tidak Lulus"

# print(status_lulus([80, 75, 60, 90]))

# Sistem cek tahun kabisat
# def tahun_kabisat(tahun):
#     return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

# print(tahun_kabisat(2024))

# Sistem urutkan daftar nilai siswa
# def urutkan_nilai(nilai):
#     return sorted(nilai)

# print(urutkan_nilai([78, 90, 65, 88, 70]))

# Sistem hitung jumlah vokal dalam teks
# def hitung_vokal(teks):
#     vokal = "aiueo"
#     return sum(1 for huruf in teks.lower() if huruf in vokal)

# print(hitung_vokal("Belajar Python"))

# Sistem hitung saldo akhir setelah transaksi
# def saldo_akhir(saldo, transaksi):
#     for t in transaksi:
#         saldo += t
#     return saldo

# print(saldo_akhir(100000, [-20000, 50000, -15000]))

# Sistem cari angka hilang dalam deret
# def angka_hilang(data):
#     n = len(data) + 1
#     return (n * (n + 1)) // 2 - sum(data)

# print(angka_hilang([1, 2, 3, 5]))

# Sistem hitung total jam dari daftar durasi
# def total_jam(data_jam):
#     return sum(data_jam)

# print(total_jam([2, 3, 1.5, 2.5]))

# Sistem validasi email sederhana
# def valid_email(email):
#     return "@" in email and "." in email

# print(valid_email("user@gmail.com"))

# Sistem hitung rata-rata nilai tanpa nilai terendah
# def rata_tanpa_terendah(nilai):
#     nilai.remove(min(nilai))
#     return sum(nilai) / len(nilai)

# print(rata_tanpa_terendah([60, 75, 80, 90]))

# Sistem hitung diskon berdasarkan total belanja di pras_phone.id
# def diskon(total):
#     if total > 1000000:
#         return total * 0.8
#     elif total > 500000:
#         return total * 0.9
#     return total

# print(diskon(750000))

# Sistem cek palindrome
# def palindrome(kata):
#     return kata == kata[::-1]

# print(palindrome("katak"))

# Sistem antrian pembeli di pras_phone.id
# antrian = []

# def masuk(nama):
#     antrian.append(nama)
#     return antrian

# def keluar():
#     return antrian.pop(0) if antrian else "Antrian kosong"

# masuk("Dicky")
# masuk("Andi")
# print(keluar())


# Sistem konversi nilai ke skala 4.0
# def skala_empat(nilai):
#     if nilai >= 85:
#         return 4.0
#     elif nilai >= 75:
#         return 3.5
#     elif nilai >= 65:
#         return 3.0
#     else:
#         return 2.0

# print(skala_empat(78))

# Sistem filter kata yang mengandung huruf tertentu
# def filter_kata(kata_list, huruf):
#     return [k for k in kata_list if huruf.lower() in k.lower()]

# print(filter_kata(["python", "java", "pseudocode"], "o"))

# Sistem hitung persentase kehadiran siswa
# def persentase_hadir(hadir, total):
#     return round((hadir / total) * 100, 2)

# print(persentase_hadir(12, 14))

# Sistem konversi detik ke jam, menit, dan detik
# def konversi_detik(detik):
#     jam = detik // 3600
#     detik %= 3600
#     menit = detik // 60
#     detik %= 60
#     return f"{jam} jam {menit} menit {detik} detik"

# print(konversi_detik(3671))

# Sistem cek bilangan prima
# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(prima(29))

# Sistem hitung total setelah cashback di pras_phone.id
# def total_setelah_cashback(total):
#     cashback = 50000 if total >= 500000 else 0
#     return total - cashback

# print(total_setelah_cashback(650000))

# Sistem ambil angka ganjil dari daftar
# def ambil_ganjil(data):
#     return [x for x in data if x % 2 != 0]

# print(ambil_ganjil([1,2,3,4,5,6,7]))

# Sistem cek kata unik dalam kalimat
# def kata_unik(teks):
#     kata = teks.split()
#     return len(kata) == len(set(kata))

# print(kata_unik("belajar python itu menyenangkan"))

# Sistem hitung jumlah nilai di atas rata-rata
# def di_atas_rata(nilai):
#     rata = sum(nilai) / len(nilai)
#     return len([n for n in nilai if n > rata])

# print(di_atas_rata([60, 70, 80, 90]))

# Sistem voting sederhana
# def voting(data):
#     hasil = {}
#     for vote in data:
#         hasil[vote] = hasil.get(vote, 0) + 1
#     return hasil

# print(voting(["A", "B", "A", "C", "B", "A"]))

# Sistem hitung selisih waktu dalam jam dan menit
# def selisih_waktu(w1, w2):
#     j1, m1 = map(int, w1.split(":"))
#     j2, m2 = map(int, w2.split(":"))
#     total1 = j1 * 60 + m1
#     total2 = j2 * 60 + m2
#     selisih = abs(total2 - total1)
#     return f"{selisih // 60} jam {selisih % 60} menit"

# print(selisih_waktu("08:30", "10:00"))

# Sistem filter kata yang mengandung huruf tertentu
# def filter_kata(kata_list, huruf):
#     return [k for k in kata_list if huruf.lower() in k.lower()]

# print(filter_kata(["python", "java", "pseudocode"], "o"))

# Sistem filter kata yang mengandung huruf tertentu
# def filter_kata(kata_list, huruf):
#     return [k for k in kata_list if huruf.lower() in k.lower()]

# print(filter_kata(["python", "java", "pseudocode"], "o"))

# Sistem antrian pembeli di pras_phone.id
# antrian = []

# def masuk(nama):
#     antrian.append(nama)
#     return antrian

# def keluar():
#     return antrian.pop(0) if antrian else "Antrian kosong"

# masuk("Dicky")
# masuk("Andi")
# print(keluar())


# Sistem antrian pembeli di pras_phone.id
# antrian = []

# def masuk(nama):
#     antrian.append(nama)
#     return antrian

# def keluar():
#     return antrian.pop(0) if antrian else "Antrian kosong"

# masuk("Dicky")
# masuk("Andi")
# print(keluar())

# Sistem cek palindrome
# def palindrome(kata):
#     return kata == kata[::-1]

# print(palindrome("katak"))

# Sistem hitung rata-rata nilai tanpa nilai terendah
# def rata_tanpa_terendah(nilai):
#     nilai.remove(min(nilai))
#     return sum(nilai) / len(nilai)

# print(rata_tanpa_terendah([60, 75, 80, 90]))


# Sistem validasi nomor HP Indonesia
# def valid_hp(no):
#     return no.startswith("08") and no.isdigit() and len(no) >= 10

# print(valid_hp("08123456789"))

# Sistem hitung jumlah kata dalam teks dengan mengabaikan tanda baca
# import string

# def hitung_kata(teks):
#     for p in string.punctuation:
#         teks = teks.replace(p, "")
#     return len(teks.split())

# print(hitung_kata("Belajar, python itu seru!"))


# Sistem cek tahun kabisat
# def kabisat(tahun):
#     return tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)

# print(kabisat(2024))


# Sistem cek tahun kabisat
# def kabisat(tahun):
#     return tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)

# print(kabisat(2024))

# Sistem ambil tiga nilai terbesar dari daftar
# def top_tiga(data):
#     return sorted(data, reverse=True)[:3]

# print(top_tiga([60, 90, 75, 85, 70]))

# Sistem bayar dengan saldo di pras_phone.id
# saldo = 100000

# def bayar(jumlah):
#     global saldo
#     if saldo >= jumlah:
#         saldo -= jumlah
#         return "Pembayaran berhasil"
#     return "Saldo tidak cukup"

# print(bayar(25000))

# Sistem predikat kelulusan siswa
# def predikat(nilai):
#     return "Lulus" if nilai >= 70 else "Tidak Lulus"

# print(predikat(68))

# Sistem cek kekuatan password
# def password_kuat(pw):
#     return (
#         len(pw) >= 8 and
#         any(c.isupper() for c in pw) and
#         any(c.isdigit() for c in pw)
#     )

# print(password_kuat("Python123"))

# Sistem hitung rata-rata nilai tanpa nilai terendah
# def rata_tanpa_terendah(nilai):
#     nilai.remove(min(nilai))
#     return sum(nilai) / len(nilai)

# print(rata_tanpa_terendah([60, 70, 80, 90]))

# Sistem hitung rata-rata nilai tanpa nilai terendah
# def rata_tanpa_terendah(nilai):
#     nilai.remove(min(nilai))
#     return sum(nilai) / len(nilai)

# print(rata_tanpa_terendah([60, 70, 80, 90]))

# Sistem konversi teks ke snake_case
# def snake_case(teks):
#     return teks.lower().replace(" ", "_")

# print(snake_case("Belajar Python Dasar"))

#   Sistem hitung jumlah digit genap dalam angka
# def hitung_genap(angka):
#     return sum(1 for d in str(angka) if int(d) % 2 == 0)

# print(hitung_genap(123456))

# Sistem hitung jumlah digit genap dalam angka
# def hitung_genap(angka):
#     return sum(1 for d in str(angka) if int(d) % 2 == 0)

# print(hitung_genap(123456))

# Sistem cek palindrome
# def palindrom(teks):
#     teks = teks.replace(" ", "").lower()
#     return teks == teks[::-1]

# print(palindrom("Kasur ini rusak"))

# Sistem validasi email sederhana
# def valid_email(email):
#     return "@" in email and "." in email.split("@")[-1]

# print(valid_email("user@gmail.com"))

# Sistem validasi email sederhana
# def valid_email(email):
#     return "@" in email and "." in email.split("@")[-1]

# print(valid_email("user@gmail.com"))

# Sistem hitung diskon berdasarkan total belanja di pras_phone.id
# def hitung_diskon(total):
#     if total >= 500000:
#         return total * 0.8
#     elif total >= 250000:
#         return total * 0.9
#     return total

# print(hitung_diskon(300000))

# Sistem login dengan batas percobaan di pras_phone.id
# def login(max_coba):
#     while max_coba > 0:
#         pw = input("Password: ")
#         if pw == "admin123":
#             return "Login sukses"
#         max_coba -= 1
#     return "Akun terkunci"

# # sistem login dengan batas percobaan di pras_phone.id
# def login(max_coba):
#     while max_coba > 0:
#         pw = input("Password: ")
#         if pw == "admin123":
#             return "Login sukses"
#         max_coba -= 1
#     return "Akun terkunci"

# sistemkelompokkan angka genap dan ganjil dari daftar
# def kelompokkan(data):
#     return {
#         "genap": [x for x in data if x % 2 == 0],
#         "ganjil": [x for x in data if x % 2 != 0]
#     }

# print(kelompokkan([1,2,3,4,5,6]))

# Sistem hitung skor jawaban ujian
# def skor(jawaban, kunci):
#     return sum(1 for j, k in zip(jawaban, kunci) if j == k)

# print(skor(["A","B","C"], ["A","C","C"]))

# Sistem deteksi gaming the system
# def deteksi_gaming(waktu, benar):
#     if waktu < 30 and benar < 0.4:
#         return "Gaming the System"
#     return "Normal"

# print(deteksi_gaming(20, 0.3))

# Sistem klasifikasi siswa berdasarkan nilai dan percobaan
# def klasifikasi(nilai, percobaan):
#     if nilai < 60 and percobaan > 3:
#         return "Struggling"
#     if nilai < 60 and percobaan <= 3:
#         return "Gaming the System"
#     if nilai >= 60 and nilai < 85:
#         return "Normal"
#     return "Ideal"

# print(klasifikasi(55, 5))

# Sistem evaluasi jawaban ujian dengan bobot
# def evaluasi(jawaban, kunci, bobot):
#     skor = 0
#     for j, k, b in zip(jawaban, kunci, bobot):
#         if j == k:
#             skor += b
#     return skor

# print(evaluasi(["A","B","C"], ["A","C","C"], [10,20,30]))

# Sistem deteksi penurunan performa siswa
# def deteksi_penurunan(nilai):
#     for i in range(len(nilai)-2):
#         if nilai[i] > nilai[i+1] > nilai[i+2]:
#             return "Performa menurun"
#     return "Stabil"

# print(deteksi_penurunan([85, 80, 70, 72]))

# Sistem berikan hint berdasarkan status
# def hint_system(status):
#     hints = {
#         "Array": ["Array menyimpan data sejenis", "Index dimulai dari 0"],
#         "Loop": ["Loop digunakan untuk pengulangan"]
#     }
#     return hints.get(status, [])

# print(hint_system("Array"))

# Sistem deteksi anomali waktu penyelesaian tugas
# def anomali(waktu):
#     rata = sum(waktu) / len(waktu)
#     return [w for w in waktu if w < rata * 0.3]

# print(anomali([120, 130, 15, 140]))

# Sistem chatbot sederhana dengan state dan performa
# def chatbot_state(state, performa):
#     if state == "QUESTION" and performa == "Low":
#         return "EXPLANATION"
#     if state == "EXPLANATION":
#         return "QUESTION"
#     return state

# print(chatbot_state("QUESTION", "Low"))

# Sistem hitung skor performa siswa
# def skor_performa(nilai, waktu, percobaan):
#     return (nilai * 0.6) + ((1 / waktu) * 20) - (percobaan * 5)

# print(skor_performa(70, 120, 2))

# Sistem adaptif tingkat kesulitan soal
# def adaptif(skor):
#     if skor < 40:
#         return "Easy"
#     elif skor < 70:
#         return "Medium"
#     return "Hard"

# print(adaptif(65))

# Sistem deteksi siswa yang kesulitan
# def struggling(history):
#     return sum(history[-3:]) / 3 < 60

# print(struggling([80, 55, 50, 45]))

# Sistem batasi jumlah hint yang ditampilkan
# def hint_limit(jumlah_hint):
#     return "Hint ditampilkan" if jumlah_hint < 3 else "Hint dibatasi"

# print(hint_limit(4))

# Sistem prediksi performa siswa berdasarkan nilai
# def prediksi_performa(nilai):
#     peluang = min(nilai / 100, 1)
#     return round(peluang, 2)

# print(prediksi_performa(78))

# Sistem identifikasi topik dengan performa rendah
# def gap(topik, benar):
#     return [t for t, b in zip(topik, benar) if b < 0.5]

# print(gap(["Array","Loop","Function"], [0.3,0.8,0.4]))

# Sistem routing mode pembelajaran berdasarkan performa siswa
# def router(performa):
#     routes = {
#         "Struggling": "Explanation Mode",
#         "Gaming": "Restriction Mode",
#         "Normal": "Practice Mode",
#         "Ideal": "Challenge Mode"
#     }
#     return routes.get(performa)

# print(router("Struggling"))


# Sistem kumpulkan data event pembelajaran
# def collect_event(waktu, benar, percobaan):
#     return {
#         "time": waktu,
#         "accuracy": benar,
#         "attempts": percobaan
#     }

# event = collect_event(120, 0.6, 3)
# print(event)

# # Sistem hitung performance index dari event pembelajaran
# def performance_index(event):
#     return (event["accuracy"] * 100) - (event["time"] / 10) - (event["attempts"] * 5)

# print(performance_index(event))


# def classify(index, event):
#     if index < 40 and event["attempts"] > 3:
#         return "Struggling"
#     if index < 40 and event["time"] < 30:
#         return "Gaming the System"
#     if index < 70:
#         return "Normal"
#     return "Ideal"

# print(classify(performance_index(event), event))


# def classify(index, event):
#     if index < 40 and event["attempts"] > 3:
#         return "Struggling"
#     if index < 40 and event["time"] < 30:
#         return "Gaming the System"
#     if index < 70:
#         return "Normal"
#     return "Ideal"

# print(classify(performance_index(event), event))
# def suggest_mode(classification):
#     modes = {
#         "Struggling": "Explanation Mode",
#         "Gaming the System": "Restriction Mode",
#         "Normal": "Practice Mode",
#         "Ideal": "Challenge Mode"
#     }
#     return modes.get(classification)

# def chatbot_response(status, materi):
#     konsep = {
#         "Array": [
#             "Array adalah struktur data linear",
#             "Menyimpan data bertipe sama",
#             "Index dimulai dari 0"
#         ]
#     }
#     if status in ["Struggling", "Gaming the System"]:
#         return konsep.get(materi)
#     return "Silakan lanjutkan pengerjaan soal"

# print(chatbot_response("Struggling", "Array"))


# def hint_controller(jumlah_hint, status):
#     if status in ["Struggling", "Gaming the System"] and jumlah_hint < 2:
#         return "Hint diizinkan"
#     return "Hint ditunda"

# print(hint_controller(1, "Struggling"))


# def learning_state(state, status):
#     if state == "QUESTION" and status in ["Struggling", "Gaming the System"]:
#         return "EXPLANATION"
#     if state == "EXPLANATION":
#         return "QUESTION"
#     return state

# print(learning_state("QUESTION", "Struggling"))


# def estimate_difficulty(avg_time, error_rate):
#     if avg_time > 180 and error_rate > 0.6:
#         return "Hard"
#     elif avg_time > 90:
#         return "Medium"
#     return "Easy"

# print(estimate_difficulty(200, 0.7))


# def effort_analysis(time_spent, attempts):
#     if time_spent > 180 and attempts > 4:
#         return "High Effort"
#     if time_spent < 30 and attempts > 3:
#         return "Low Effort (Gaming)"
#     return "Normal Effort"

# print(effort_analysis(20, 5))


# def mastery_tracker(correct_history):
#     mastery = sum(correct_history) / len(correct_history)
#     return round(mastery, 2)

# print(mastery_tracker([1, 0, 1, 1, 0]))


# def mastery_tracker(correct_history):
#     mastery = sum(correct_history) / len(correct_history)
#     return round(mastery, 2)

# print(mastery_tracker([1, 0, 1, 1, 0]))


# def select_material(status, topic):
#     materials = {
#         "Array": {
#             "basic": "Pengertian array dan index",
#             "example": "Contoh array satu dimensi"
#         }
#     }
#     if status in ["Struggling", "Gaming the System"]:
#         return materials[topic]["basic"]
#     return materials[topic]["example"]

# print(select_material("Struggling", "Array"))

# system keputusan intervensi berdasarkan status dan mastery
# def intervention_decision(status, mastery):
#     if status in ["Struggling", "Gaming the System"] and mastery < 0.6:
#         return "Intervensi diperlukan"
#     return "Tidak perlu intervensi"

# print(intervention_decision("Struggling", 0.5))


# def generate_report(name, mastery, status):
#     return {
#         "student": name,
#         "mastery_level": mastery,
#         "performance_status": status
#     }

# print(generate_report("Mahasiswa A", 0.58, "Struggling"))

# Sistem ekstrak fitur dari log pembelajaran
# def extract_features(log):
#     return {
#         "avg_time": sum(l["time"] for l in log) / len(log),
#         "error_rate": 1 - (sum(l["accuracy"] for l in log) / len(log)),
#         "avg_attempts": sum(l["attempts"] for l in log) / len(log)
#     }

# logs = [
#     {"time":120, "accuracy":0.6, "attempts":3},
#     {"time":200, "accuracy":0.4, "attempts":4}
# ]
# print(extract_features(logs))

# def infer_performance(features):
#     if features["error_rate"] > 0.6 and features["avg_time"] > 150:
#         return "Struggling"
#     if features["error_rate"] > 0.6 and features["avg_time"] < 40:
#         return "Gaming the System"
#     if features["error_rate"] < 0.3:
#         return "Ideal"
#     return "Normal"

# print(infer_performance(extract_features(logs)))
# def cognitive_load(time_spent, attempts):
#     return round((time_spent / 60) + (attempts * 0.5), 2)

# print(cognitive_load(180, 4))

# def intervention_type(status, load):
#     if status == "Struggling" and load > 5:
#         return "Concept Reinforcement"
#     if status == "Gaming the System":
#         return "Motivational Feedback"
#     return "No Intervention"

# print(intervention_type("Struggling", 6))

# def concept_coverage(concepts):
#     return [c for c, score in concepts.items() if score < 0.6]

# print(concept_coverage({"Array":0.5, "Loop":0.8, "Function":0.4}))


# def feedback(status, concept):
#     if status == "Struggling":
#         return f"Perhatikan kembali konsep dasar {concept}"
#     if status == "Gaming the System":
#         return "Coba kerjakan dengan lebih teliti"
#     return "Lanjutkan latihan berikutnya"

# print(feedback("Struggling", "Array"))

# def session_outcome(before, after):
#     if after > before:
#         return "Intervensi efektif"
#     return "Perlu penyesuaian"

# print(session_outcome(0.55, 0.7))

# Sistem cek konsistensi skor pembelajaran
# def consistency(scores):
#     if len(scores) < 3:
#         return "Data tidak cukup"
#     variance = max(scores) - min(scores)
#     return "Konsisten" if variance < 0.2 else "Tidak konsisten"

# print(consistency([0.7, 0.75, 0.72]))

# def time_pattern(times):
#     avg = sum(times) / len(times)
#     if avg < 40:
#         return "Terlalu cepat (potensi gaming)"
#     if avg > 180:
#         return "Terlalu lama (potensi struggling)"
#     return "Normal"

# print(time_pattern([20, 25, 30]))


# def adaptive_threshold(class_avg):
#     return {
#         "low": class_avg * 0.8,
#         "high": class_avg * 1.2
#     }

# print(adaptive_threshold(70))

# def confidence_score(features):
#     score = 0
#     if features["error_rate"] > 0.6:
#         score += 1
#     if features["avg_time"] > 150 or features["avg_time"] < 40:
#         score += 1
#     return score / 2

# print(confidence_score({"error_rate":0.7, "avg_time":160}))

# def content_depth(status):
#     return {
#         "Struggling": "Basic Concept",
#         "Gaming the System": "Concept Reminder",
#         "Normal": "Worked Example",
#         "Ideal": "Challenge Problem"
#     }.get(status)

# print(content_depth("Gaming the System"))

# def cooldown(last_intervention, current_time):
#     return (current_time - last_intervention) > 300

# print(cooldown(1000, 1400))

# def effectiveness(before, after):
#     improvement = after - before
#     return {
#         "improvement": round(improvement, 2),
#         "effective": improvement > 0.1
#     }

# print(effectiveness(0.55, 0.7))

# Sistem voting sederhana
# def voting(data):
#     hasil = {}
#     for nama in data:
#         hasil[nama] = hasil.get(nama, 0) + 1
#     return max(hasil, key=hasil.get)

# print(voting(["A","B","A","C","A","B"]))

# Sistem validasi username
# def valid_username(username):
#     return username.isalnum() and 5 <= len(username) <= 12

# print(valid_username("user123"))

# Sistem hitung median dari daftar angka
# def median(data):
#     data.sort()
#     n = len(data)
#     mid = n // 2
#     return data[mid] if n % 2 != 0 else (data[mid-1] + data[mid]) / 2

# print(median([7, 3, 5, 1]))

# Sistem transfer saldo antar akun
# def transfer(saldo_pengirim, saldo_penerima, jumlah):
#     if saldo_pengirim >= jumlah:
#         saldo_pengirim -= jumlah
#         saldo_penerima += jumlah
#     return saldo_pengirim, saldo_penerima

# print(transfer(100000, 50000, 30000))

# Sistem cari posisi semua kemunculan huruf dalam teks
# def cari_posisi(teks, huruf):
#     return [i for i, c in enumerate(teks) if c == huruf]

# print(cari_posisi("programming", "g"))

# Sistem konversi detik ke format jam:menit:detik
# def konversi_waktu(detik):
#     jam = detik // 3600
#     menit = (detik % 3600) // 60
#     detik = detik % 60
#     return f"{jam}:{menit}:{detik}"

# print(konversi_waktu(3661))

# Sistem hitung skor jawaban ujian
# def hitung_skor(jawaban, kunci):
#     skor = 0
#     for j, k in zip(jawaban, kunci):
#         if j == k:
#             skor += 1
#     return skor

# print(hitung_skor(["A","B","C","D"], ["A","C","C","D"]))


# Sistem validasi bukti transfer pembayaran di pras_phone.id
# def validasi_transfer(nama_pengirim, jumlah_transfer):
#     nama_akun = "Dicky"
#     saldo_akun = 7000000
#     if nama_pengirim != nama_akun:
#         return "Nama pengirim tidak sesuai"
#     if jumlah_transfer > saldo_akun:
#         return "Saldo tidak cukup"
#     return "Transfer valid"
# print(validasi_transfer("Dicky", 5000000))


# sistem 
# def extract_features(log):
#     return {
#         "avg_time": sum(l["time"] for l in log) / len(log),
#         "error_rate": 1 - (sum(l["accuracy"] for l in log) / len(log)),
#         "avg_attempts": sum(l["attempts"] for l in log) / len(log)
#     }

# logs = [
#     {"time":120, "accuracy":0.6, "attempts":3},
#     {"time":200, "accuracy":0.4, "attempts":4}
# ]
# print(extract_features(logs))
# def infer_performance(features):
#     if features["error_rate"] > 0.6 and features["avg_time"] > 150:
#         return "Struggling"
#     if features["error_rate"] > 0.6 and features["avg_time"] < 40:
#         return "Gaming the System"
#     if features["error_rate"] < 0.3:
#         return "Ideal"
#     return "Normal"

# print(infer_performance(extract_features(logs)))

# def cognitive_load(time_spent, attempts):
#     return round((time_spent / 60) + (attempts * 0.5), 2)

# print(cognitive_load(180, 4))

# def cognitive_load(time_spent, attempts):
#     return round((time_spent / 60) + (attempts * 0.5), 2)

# print(cognitive_load(180, 4))


# def ada_duplikat(data):
#     return len(data) != len(set(data))

# print(ada_duplikat([1,2,3,4,2]))


# def total_jam(data):
#     return sum(jam for jam in data if jam > 0)

# print(total_jam([2, 3, -1, 4]))

# Sistem cek irisan antara dua daftar
# def ada_irisan(a, b):
#     return bool(set(a) & set(b))

# print(ada_irisan([1,2,3], [4,5,3]))

# Sistem hitung jumlah bilangan prima dalam daftar
# def is_prima(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def hitung_prima(data):
#     return sum(1 for x in data if is_prima(x))

# print(hitung_prima([2,3,4,5,6,7]))

# Sistem urutkan dictionary berdasarkan nilai
# def urut_dict(data):
#     return dict(sorted(data.items(), key=lambda x: x[1]))

# print(urut_dict({"A":3, "B":1, "C":2}))

# Sistem hitung total hari dari tahun, bulan, dan hari
# def total_hari(tahun, bulan, hari):
#     return tahun * 365 + bulan * 30 + hari

# print(total_hari(2025, 1, 15))

# Sistem cari kata terpanjang dalam teks
# def kata_terpanjang(teks):
#     kata = teks.split()
#     return max(kata, key=len)

# print(kata_terpanjang("belajar algoritma dengan python"))

# Sistem cek stok barang di pras_phone.id
# def cek_stok(stok, jual):
#     stok -= jual
#     return "Restock" if stok < 5 else "Aman"

# print(cek_stok(10, 7))

# Sistem hitung nilai akhir siswa
# def nilai_akhir(tugas, uts, uas):
#     return round((tugas*0.3) + (uts*0.3) + (uas*0.4), 2)

# print(nilai_akhir(80, 75, 90))

# Sistem hitung rata-rata nilai
# def rata_rata(nilai):
#     return sum(nilai) / len(nilai)

# print(rata_rata([80, 75, 90, 85]))

# Sistem cek palindrome
# def palindrom(teks):
#     teks = teks.replace(" ", "").lower()
#     return teks == teks[::-1]

# print(palindrom("Kasur ini rusak"))

# Sistem klasifikasi performa siswa berdasarkan nilai
# def performa(nilai):
#     if nilai < 60:
#         return "Low Performance"
#     elif nilai < 85:
#         return "Normal"
#     return "High Performance"

# print(performa(88))

# Sistem hitung jumlah kata unik dalam teks
# def kata_unik(teks):
#     return len(set(teks.lower().split()))

# print(kata_unik("belajar python belajar logika"))

# Sistem tarik saldo dari akun
# def tarik(saldo, jumlah):
#     if saldo >= jumlah:
#         saldo -= jumlah
#     return saldo

# print(tarik(200000, 50000))

# Sistem cari nilai minimum dan maksimum dalam daftar
# def min_max(data):
#     return min(data), max(data)

# print(min_max([10, 5, 30, 20]))

# Sistem klasifikasi berdasarkan waktu penyelesaian
# def kategori_waktu(detik):
#     if detik > 300:
#         return "Struggling"
#     elif detik < 60:
#         return "Gaming the System"
#     return "Normal"

# print(kategori_waktu(420))

# Sistem hitung akurasi jawaban ujian
# def akurasi(benar, total):
#     return round((benar / total) * 100, 2)

# print(akurasi(7, 10))

# Sistem deteksi pola jawaban mencurigakan
# def pola_jawaban(jawaban):
#     return "Mencurigakan" if len(set(jawaban)) == 1 else "Normal"

# print(pola_jawaban(["A", "A", "A", "A"]))

# Sistem klasifikasi performa berdasarkan percobaan dan waktu
# def classify_performance(attempts, time_spent):
#     if attempts > 5 and time_spent > 300:
#         return "Struggling"
#     elif attempts < 2 and time_spent < 60:
#         return "Gaming the System"
#     return "Normal"

# print(classify_performance(7, 420))

# Sistem hitung rata-rata waktu penyelesaian tugas
# def avg_time(times):
#     return sum(times) / len(times)

# print(avg_time([120, 150, 300]))

# Sistem chatbot respons berdasarkan status siswa
def chatbot_response(status):
    responses = {
        "Struggling": "Tampilkan konsep dasar",
        "Gaming": "Batasi bantuan",
        "Normal": "Lanjutkan pembelajaran"
    }
    return responses.get(status)

print(chatbot_response("Struggling"))
