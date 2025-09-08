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
        double phi = 3.14;
        int r;
        double luas;
        Scanner inputUser = new Scanner(System.in);
        System.out.print("Masukkan jari-jari lingkaran: ");
        r = inputUser.nextInt();

        luas = phi * r * r;
        System.out.println("Luas lingkaran: " + luas);
    }
}
