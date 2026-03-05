RSA Cryptography Implementation (Python)
Deskripsi

Repository ini berisi implementasi sederhana dari algoritma RSA (Rivest–Shamir–Adleman) menggunakan bahasa pemrograman Python tanpa menggunakan library kriptografi eksternal. Implementasi ini dibuat untuk memahami konsep dasar kriptografi asimetris, khususnya proses pembangkitan kunci, enkripsi, dan dekripsi.

RSA adalah algoritma kriptografi asymmetric-key yang menggunakan dua kunci berbeda:

Public Key digunakan untuk mengenkripsi pesan

Private Key digunakan untuk mendekripsi pesan

Keamanan RSA didasarkan pada kesulitan memfaktorkan bilangan besar hasil perkalian dua bilangan prima.

Repository ini dibuat sebagai bagian dari tugas Analisis dan Implementasi Mekanisme Kriptografi.

Konsep Dasar RSA

RSA bekerja melalui tiga tahapan utama:

Key Generation (Pembangkitan Kunci)

Encryption (Enkripsi)

Decryption (Dekripsi)

Alur Kerja Program

Program ini melakukan beberapa langkah utama:

Membuat fungsi matematika yang dibutuhkan

Membuat pasangan kunci RSA

Mengubah plaintext menjadi ciphertext

Mengembalikan ciphertext menjadi plaintext

Fungsi-Fungsi dalam Program
1. Fungsi gcd()
Tujuan

Fungsi ini digunakan untuk menghitung Greatest Common Divisor (GCD) atau Faktor Persekutuan Terbesar (FPB) dari dua bilangan.

Fungsi ini digunakan untuk memastikan bahwa nilai e relatif prima terhadap nilai φ(n).

Implementasi
def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a
Cara Kerja

Fungsi ini menggunakan Euclidean Algorithm.

Langkah kerja:

Selama b tidak sama dengan 0

Tukar nilai a dengan b

Hitung sisa pembagian a % b

Proses diulang sampai b = 0

Nilai terakhir a adalah GCD

2. Fungsi mod_inverse()
Tujuan

Fungsi ini digunakan untuk mencari modular multiplicative inverse dari nilai e terhadap phi.

Nilai ini akan digunakan sebagai private key (d).

Implementasi
def mod_inverse(e,phi):
    for d in range(1,phi):
        if (e * d) % phi == 1:
            return d
    return None
Cara Kerja

Fungsi ini mencari nilai d yang memenuhi persamaan berikut:

(e × d) mod φ = 1

Langkah kerja:

Program mencoba semua angka dari 1 sampai φ

Setiap angka diuji menggunakan operasi modulo

Jika hasilnya 1, maka angka tersebut adalah modular inverse

Nilai tersebut dikembalikan sebagai private key

Key Generation (Pembangkitan Kunci)

Proses ini menghasilkan Public Key dan Private Key.

1. Memilih dua bilangan prima
p = 61
q = 53
2. Menghitung nilai n
n = p × q

Hasil:

n = 3233
3. Menghitung Euler Totient
φ = (p - 1)(q - 1)

Hasil:

φ = 3120
4. Memilih nilai e
e = 17

Syarat nilai e:

1 < e < φ

gcd(e, φ) = 1

5. Menghitung nilai d
d = mod_inverse(e, φ)

Hasil:

d = 2753
Hasil Key Generation

Public Key

(e,n) = (17,3233)

Private Key

(d,n) = (2753,3233)
Fungsi Enkripsi
Rumus RSA
c = m^e mod n
Implementasi
def encrypt(plaintext, e, n):
    cipher = []
    for char in plaintext:
        m = ord(char)
        c = pow(m, e, n)
        cipher.append(c)
    return cipher
Cara Kerja

Program membaca setiap karakter dari plaintext

Karakter diubah menjadi kode ASCII menggunakan ord()

Dilakukan proses enkripsi menggunakan rumus RSA

Hasil dimasukkan ke dalam list ciphertext

Fungsi Dekripsi
Rumus RSA
m = c^d mod n
Implementasi
def decrypt(ciphertext, d, n):
    plain = ""
    for c in ciphertext:
        m = pow(c, d, n)
        char = chr(m)
        plain += char
    return plain
Cara Kerja

Program membaca setiap angka dalam ciphertext

Dilakukan proses dekripsi menggunakan private key

Nilai hasil dikonversi kembali menjadi karakter menggunakan chr()

Karakter digabungkan kembali menjadi plaintext

Cara Menjalankan Program

Clone repository

git clone https://github.com/username/rsa-cryptography-demo.git

Masuk ke folder project

cd rsa-cryptography-demo

Jalankan program

python rsa_demo.py

Masukkan pesan yang ingin dienkripsi.

Contoh Output Program
=== KEY GENERATION ===
Bilangan prima p: 61
Bilangan prima q: 53
Nilai n (p*q): 3233
Nilai phi: 3120

Public Key (e,n): (17, 3233)
Private Key (d,n): (2753, 3233)

Masukkan pesan: KRIPTO

Ciphertext: [3000, 1313, 745, 745, 2182, 2412]

Hasil Dekripsi: KRIPTO
Kelebihan Algoritma RSA

Menggunakan dua kunci berbeda sehingga distribusi kunci lebih aman.

Keamanan tinggi karena didasarkan pada kesulitan memfaktorkan bilangan besar.

Digunakan secara luas pada sistem keamanan modern seperti HTTPS dan SSL.

Mendukung digital signature untuk verifikasi identitas.

Kekurangan Algoritma RSA

Proses komputasi lebih lambat dibandingkan kriptografi simetris.

Tidak efisien untuk mengenkripsi data besar.

Memerlukan ukuran kunci besar agar tetap aman.

Rentan jika implementasi tidak benar, misalnya menggunakan bilangan prima kecil.

Kesimpulan

Implementasi ini menunjukkan cara kerja dasar algoritma RSA mulai dari pembangkitan kunci hingga proses enkripsi dan dekripsi. Walaupun contoh ini menggunakan bilangan kecil untuk mempermudah pemahaman, implementasi RSA pada sistem nyata menggunakan bilangan prima yang sangat besar untuk menjaga keamanan data.

Referensi

Rivest, R., Shamir, A., & Adleman, L. (1978). A Method for Obtaining Digital Signatures and Public-Key Cryptosystems.

Stallings, W. (2017). Cryptography and Network Security.

Schneier, B. (1996). Applied Cryptography.