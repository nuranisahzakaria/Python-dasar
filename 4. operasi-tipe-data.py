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