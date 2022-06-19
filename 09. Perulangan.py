# ----------------------------------------------------------FOR---------------------------------------------------------
for huruf in 'Nur Anisah':      # contoh pertama
    print('Huruf: {}'.format(huruf))

flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:      # contoh kedua
    print('Flower: {}'.format(flower))

# perulangan berdasarkan indeks atau range
flowers = ['mawar', 'melati', 'anggrek']
for index in range(len(flowers)):
    print('Flowers: {}'.format(flowers[index]))

# ---------------------------------------------------------WHILE--------------------------------------------------------
count = 0
while (count < 7):
    print('Hitungannya adalah: {}'.format(count))

    count =count + 1
var = 1
while var == 1:     # Struktur infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))
    var = var + 0.25

while True:     # Struktur infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))
    var = var + 0.25

# -----------------------------------------------PERULANGAN BERTINGKAT--------------------------------------------------
for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()