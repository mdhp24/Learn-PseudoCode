
// PSEUDOCODE
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // System.out.println("Hello, World!");

        // // Program dari PSEUDOCODE menentukan sebuah bilangan adalah ganjil atau
        // genap
        // int bilangan;

        // bilangan = 99;
        // if (bilangan % 2 == 0) {
        // System.out.print(bilangan + " Bilangan genap");
        // } else {
        // System.out.print(bilangan + " Bilangan ganjil");
        // }
        // }

        // Program dari PSEUDOCODE mencari luas lapangan sepak bola
        // int panjang, lebar, luas;

        // panjang = 100;
        // lebar = 64;
        // luas = panjang * lebar;

        // System.out.println("Luas lapangan sepak bola adalah " + luas);

        // PSEUDOCODE
        // Program menghitung persegi panjang

        // int panjang, lebar, luas;

        // Scanner inputUser = new Scanner(System.in);
        // System.out.print("Masukkan panjang: ");
        // panjang = inputUser.nextInt();

        // System.out.print("Masukkan lebar: ");
        // lebar = inputUser.nextInt();

        // luas = panjang * lebar;
        // System.out.println("Luas persegi panjang: " + luas);

        // PSEUDOCODE Konversi Celcius ke Fahrenheit
        // int c;
        // double F;

        // Scanner inputUser = new Scanner(System.in);
        // System.out.print("Masukkan suhu (Celcius): ");
        // c = inputUser.nextInt();

        // F = (c * 9/5) + 32;
        // System.out.println("Fahrenheit: " + F);

        // PSEUDOCODE Menghitung Volume Kubus
        // int sisi;
        // int volume;

        // Scanner inputUser = new Scanner(System.in);
        // System.out.print("Masukkan sisi kubus: ");
        // sisi = inputUser.nextInt();

        // volume = sisi * sisi * sisi;
        // System.out.println("Volume kubus: " + volume);

        // PSEUDOCODE Menghitung Luas Lingkaran
        // double phi = 3.14;
        // int r;
        // double luas;
        // Scanner inputUser = new Scanner(System.in);
        // System.out.print("Masukkan jari-jari lingkaran: ");
        // r = inputUser.nextInt();

        // luas = phi * r * r;
        // System.out.println("Luas lingkaran: " + luas);

        // int nilai;
        // Scanner inputUser = new Scanner(System.in);
        // System.out.print("Masukkan nilai (0-100): ");
        // nilai = inputUser.nextInt();

        // if (nilai >= 60) {
        // System.out.println("Lulus");
        // System.out.println("Selamat Anda lulus!");

        // } else {
        // System.out.println("Tidak Lulus");
        // }

        // PSEUDOCODE Menentukan Bilangan Positif, Negatif, atau Nol
        // int number;
        // Scanner inputUser = new Scanner(System.in);
        // System.out.print("Masukkan sebuah bilangan: ");
        // number = inputUser.nextInt();
        // if (number > 0) {
        // System.out.println(number + " adalah bilangan positif.");
        // } else if (number < 0) {
        // System.out.println(number + " adalah bilangan negatif.");
        // } else {
        // System.out.println("Bilangan yang dimasukkan adalah nol.");
        // }

        // PSEUDOCODE Menentukan Tahun Kabisat
        // int year;
        // Scanner inputUser = new Scanner(System.in);
        // System.out.print("Masukkan tahun: ");
        // year = inputUser.nextInt();
        // if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        // System.out.println(year + " adalah tahun kabisat.");
        // } else {
        // System.out.println(year + " bukan tahun kabisat.");
        // }

        // PSEUDOCODE Menjumlahkan 10 angka dari input user
        // int total = 0;

        // Scanner inputUser = new Scanner(System.in);
        // for (int i = 1; i <= 10; i++) {
        // System.out.print("Masukkan angka ke-" + i + ": ");
        // int angka = inputUser.nextInt();
        // total += angka;
        // }
        // System.out.println("Total penjumlahan 10 angka adalah " + total);

        // PSEUDOCODE Menampilkan Bilangan Genap dari 1 sampai 10000
        // System.out.println("Bilangan genap dari 1 sampai 1000:");
        // for (int i = 1; i <= 1000; i++) {
        // if (i % 2 == 0) {
        // System.out.print(i + " ");
        // }
        // }

        // PSEUDOCODE Menampilkan Bilangan dari 1 sampai N
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan nilai N: ");
        int N = input.nextInt();

        for (int i = 1; i <= N; i++) {
            System.out.print(i + " ");
        }

    }
}
