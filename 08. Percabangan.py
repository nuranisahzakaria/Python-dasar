# ---------------------------------------------------- IF ---------------------------------------------------------------
# Pakek garis-garis gini norak sih sebenarnya, tapi gapapa lah biar enak belajar. Suatu hari kalo aku udah pinter ngoding
    # dan liat kodingan ini, pasti aku ketawain, wkwkwkwk. Tapi kalo masih ada umur dimasa depan sih, hehehe.
# CONTOH 1
kelerengku = 10
if kelerengku:
    print("Cetak ini jika benar")
    print(kelerengku)

# CONTOH 2
def hitung(self, print(1+2)) # lupa cara definisikan fungsi wkwkwkw, ngga papa nanti kita belajar lagi nis
if kelerengku: hitung()  # function hitungnya buat dulu biar ngga error

# ------------------------------------------------------ ELSE ----------------------------------------------------------
# CONTOH 1
tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
if tinggi_badan>=160:
    print ("Silakan, Anda boleh masuk")
else:
    print ("Maaf, Anda belum boleh masuk")

# CONTOH 2
bilangan = 4
if bilangan % 2 == 0:
    print('Bilangan {} adalah genap'.format(bilangan))
else:
    print('Bilangan {} adalah ganjil'.format(bilangan))

# ------------------------------------------------------ ELIF ----------------------------------------------------------
# CONTOH 1
nilai = int(input("Masukkan nilai tugas Anda : "))
if nilai>80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai>70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai>60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

# CONTOH 2
bilangan = -3
if bilangan > 0:
    print('Bilangan {} adalah positif'.format(bilangan))
elif bilangan < 0:
    print('Bilangan {} adalah negatif'.format(bilangan))
else:
    print('Bilangan {} adalah nol'.format(bilangan))


# ------------------------------------------------ TERNARY OPERATORS --------------------------------------------------
# PERBANDINGAN IF DAN TERNARY
    # CONTOH 1
        # Menggunakan if
            # if (condition):
            # condition_if_true
            # else:
            # condition_if_false

            # lulus = True
            # if (lulus):
            #     kata = ”selamat”
            #     else:
            #     kata = “perbaiki”

        # Menggunakan Ternary Operators
            # condition_if_true if condition else condition_if_false

            # lulus = True
            # kata = "selamat" if lulus else "perbaiki"

# ------------------------------------------------ SHORTHAND TERNARY --------------------------------------------------
# memeriksa kode/hasil dari sebuah fungsi dan memastikan outputnya tidak menyebabkan error (atau minimal memberikan
# informasi relevan saat error):
    hasil = None
    pesan = hasil or "Tidak ada data"
    print(pesan)