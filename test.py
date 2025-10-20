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
import random

jurusan = ["TI", "RPL", "SI"]
data_mahasiswa = []

for i in range(10):
    nama = f"Mahasiswa_{i+1}"
    nilai = random.randint(40, 100)
    waktu = random.randint(10, 40)
    jur = random.choice(jurusan)
    data_mahasiswa.append({"nama": nama, "jurusan": jur, "nilai": nilai, "waktu": waktu})

for m in data_mahasiswa:
    print(m)