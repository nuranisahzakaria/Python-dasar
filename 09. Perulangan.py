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

# -----------------------------------------------PERULANGAN BERTINGKAT--------------------------------------------------
var = 1
while var == 1:     # Struktur infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))

while True:     #