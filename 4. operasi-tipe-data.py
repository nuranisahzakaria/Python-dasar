# len()
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))

contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_set)
print(len(contoh_set))

contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))

# min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# count()
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# Penggabungan dan Replikasi
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)

learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2
print(replikasi)

# Fungsi pengali juga dapat Anda manfaatkan untuk inisialisasi List.
tujuh = [7] * 7
print(len(tujuh))
print(tujuh)

# Range
    # range dengan parameter n
for i in range(5):
    print(i)
    # range dengan parameter 2
for i in range(1, 11):
    print(i)
    # range dengan parameter 3
print([_ for _ in range(0,20,5)])

# in dan not in
    # untuk mengetahui sebuah nilai atau objek ada dalam list
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# Memberikan nilai untuk multiple variable
    # Kodingan biasa
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
    # Menggunakan list/tupple python
data = ['shirt', 'white', 'L']  # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data
    # Menukar nilai multi variabel
apparel, color = 'shirt', 'white'
apparel, color = color, apparel
print(apparel)
print(color)

# Sort
    # Mengurutkan angka atau huruf dalam list ()
    # Contoh 1
angka = [100, 1000, 500, 200, 5]
angka.sort()
print(angka)
    # Contoh 2
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)
    # contoh 3, urutan terbalik menggunakan reverse
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)
    # Note................
    # 1. Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya
    # 2. Metode sort menggunakan urutan ASCII, sehingga nilai huruf kapital (uppercase) akan lebih
        # dahulu dibandingkan huruf kecil (lowercase) ===> Untuk mengatasi kendala ini, Anda dapat
        # memasukkan keyword str.lower pada parameter. Hal ini akan membuat metode sort menganggap
        # semua objek menggunakan huruf kecil, tanpa mengubah kondisi asli dari objek tersebut.
    # Contoh 4
kendaraan = ['Motor', 'Mobil', 'helikopter', 'pesawat']
kendaraan.sort(key=str.lower)
print(kendaraan)