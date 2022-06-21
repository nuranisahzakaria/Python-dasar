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