# BREAK.................................................

# CONTOH 1
for huruf in 'Nur Anisah':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

# CONTOH 2
for i in range (0,10):
    for j in range (0,10):
        if j>i:
            print()
            break
        else:
            print("*",end="")

# CONTINUE .............................................
# CONTOH 1
for huruf in 'Nur Anisah':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# CONTOH 2
jumlah_baris = 20
baris = 0
bintang = 0
while baris < jumlah_baris:
    if (bintang) >= (baris+1):
        print()
        baris = baris+1
        bintang = 0
        continue  # Saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*", end="")
    bintang = bintang+1

# ELSE SETELAH FOR ...................................
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break

# ELSE SETELAH WHILE..................................
# CONTOH 1
n = 13
while n > 0:
    n = n-1
    if n == 8:
        break
    print (n)
else: print("Loop selesai")

# CONTOH 2
n = 10
while n > 0:
    n = n - 2
    print(n)
else:
    print("Loop selesai")

# PASS ................................................
    # sebuah pernyataan atau blok pernyataan (statement), namun tidak melakukan apapun - melanjutkan eksekusi sesuai
    # dengan urutannya. Kontrol ini banyak digunakan saat Anda belum melakukan implementasi (atau menyiapkan tempat
    # untuk implementasi), serta membiarkan program tetap berjalan saat misalnya Anda mengalami kegagalan atau exception.
# import sys
# data=''
# while(data!='exit'):
#     try:
#         data=input('Please enter an integer (type exit to exit): ')
#         print('got integer: {}'.format(int(data)))
#     except:
#         if data == 'exit':
#             pass  # exit gracefully without prompt any error
#         else:
#             print('error: {}'.format(sys.exc_info()[0]))

# LIST COMPREHENTION
# CONTOH 1 tanpa list comprehention
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)
# CONTOH 1 dengan list comprehention
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

# CONTOH 2
list1 = ['n', 'i', 's', 'a']
list2 = ['n', 'u', 'r', 'a']
# tanpa list comprehention
duplikats = []
for a in list1:
    for b in list2:
        if a == b:
            duplikats.append(a)
print(duplikats)

# dengan list comprehention
duplikats = [a for a in list1 for b in list2 if a == b]
print (duplikats)

# CONTOH 3
# kecilkan semua huruf
a = ["Halo", 'Nisa', 'Apa', 'Kabar']
a_huruf_kecil = [ulang.lower() for ulang in a]
print(a_huruf_kecil)

# CONTOH 4
angka = range (1, 10, 2)
x = [[g**2, g**3] for g in angka] # g => angka 1, 3, 5, 7, 9
print(x)