# TIPE DATA PYTHON
# beda kurung beda tipe

# LIST (kurung siku)
# Kumpulan variabel terurut
list = [1, 2.2, 'python']

list2 = [5, 10, 15, 20, 25, 30, 35, 40]
# 1. Menampilkan per elemet
print(list2[5])
print(list2[-1])
print(list2[3:5])
print(list2[:5])
print(list2[-3:])
print(list2[1:7:2])

# 2. Merubah elemen
list3 = [1, 2, 3]
list3[2] = 4
print(list3)

# 3. Menambahkan elemen -> pakai fungsi append
list3.append(5)
print(list3)

# 4. Menghapus element -> pakai fungsi del
binatang = ['kucing', 'rusa', 'badak', 'gajah']
del binatang[2]
print(binatang)

# --------------------------------------------------------------------------------------------------------
# SLICING PADA STRING
s = "Hello World!"
print(s[4])         # ambil karakter kelima dari string s
print(s[6:11])      # ambil karakter ketujuh hingga sebelas dari string s
s[5] = "d"          # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
s = "Halo Dunia!"   # ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print(s)

# --------------------------------------------------------------------------------------------------------
# TUPLE (kurung biasa)
# Tuple adalah jenis dari list yang tidak dapat diubah elemennya
tuple = (5, 'program', 1 + 3j)
print(tuple[1])
print(tuple[0:3])

# --------------------------------------------------------------------------------------------------------
# SET (kurung kurawal)
# Set adalah kumpulan item bersifat unik dan tanpa urutan
set = {1, 2, 2, 3, 3, 3}
print(set)

# --------------------------------------------------------------------------------------------------------
# KEY-VALUE
d = {1: 'value', 'key': 2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);

# --------------------------------------------------------------------------------------------------------
# KONVERSI TIPE DATA
print(float(5))
print(int(10.6))
print(int(-10.6))
print(float('2.5'))
print(str(25))
print(int('1p'))
print(set([1, 2, 3]))
print(tuple({5, 6, 7}))
print(list('hello'))
print(dict([[1, 2], [3, 4]]))
print(dict([(3, 26), (4, 44)]))

# cek tipe data
contoh = 19.7
print(type(contoh))

if False:
    9 + "satu"  # Baris ini tidak dioperasikan, sehingga tidak muncul notifikasi TypeError
else:
    9 + 1
