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
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

operasi = input("Masukkan operasi (+, -, *, /): ")

if operasi == "+":
    hasil = a + b
elif operasi == "-":
    hasil = a - b
elif operasi == "*":
    hasil = a * b
elif operasi == "/":
    hasil = a / b
else:
    hasil = None

if hasil is not None:
    print("Hasil: ", hasil)
else:
    print("Operasi tidak valid.")