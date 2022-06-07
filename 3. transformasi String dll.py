# 1. Mengubah Huruf Besar/Kecil
# upper() dan lower()
kata1 = 'dicoding'
kata1 = kata1.upper()
print(kata1)

kata2 = 'DICODING'
kata2 = kata2.lower()
print(kata2)


# 2. Awalan dan Akhiran
# a. rstrip() -> menghapus whitespace pada sebelah kanan string atau akhir string
print('Dicoding    '.rstrip())

# b. lstrip() -> menghapus whitespace pada sebelah kiri atau awal string
print('    Dicoding'.lstrip())

# c. strip() -> menghapus whitespace pada bagian awal atau akhir string
print('    Dicoding    '.strip())
# menghapus karakter
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code'))

# d. startswith()
# mengembalikan nilai True jika string diawali dengan kata awalan tertentu
# yang kita inginkan, jika tidak maka akan mengembalikan nilai False.
print('Dicoding Indonesia'.startswith('Dicoding'))

# e. endswith()
# mengembalikan nilai True jika string diakhiri dengan kata akhiran tertentu
# yang kita inginkan, jika tidak maka akan mengembalikan nilai False.
print('Dicoding Indonesia'.endswith('Indonesia'))


# 3. Memisah dan Menggabung String
# a. join() -> metode yang dipakai untuk menggabungkan sejumlah string
print(' '.join(['Dicoding', 'Indonesia', '!']))
print('123'.join(['Dicoding', 'Indonesia', '!']))

# b. split() -> memisahkan substring berdasarkan delimiter tertentu (defaultnya
# adalah whitespace, tab, atau newline)
print('Dicoding Indonesia !'.split())
print('Dicoding123Indonesia123!'.split('123'))
# metode split() untuk memisahkan setiap baris pada string multiline
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))


# 4. Mengganti Elemen String
# a. replace() -> mengembalikan string baru dalam kondisi substring telah tergantikan
# dengan parameter yang dimasukkan
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1))


# 5. Pengecekan String
# a. isupper() -> Metode isupper() akan mengembalikan nilai True jika semua huruf dalam
# string adalah huruf besar, dan akan mengembalikan nilai False jika terdapat satu saja
# huruf kecil di dalam string tersebut.
kata = 'DICODING' # contoh true
kata.isupper()

kata = 'Dicoding' # contoh false
kata.isupper()

# b. islower() -> kebalikan dari metode isupper(), metode ini akan mengembalikan nilai True
# jika semua huruf dalam string adalah huruf kecil, dan akan mengembalikan nilai False jika
# terdapat satu saja huruf besar di dalam string tersebut
kata = 'dicoding'
kata.islower()
# Bahkan Anda bisa melakukan operasi pada hasil operasinya (chain of method).
print('Dicoding'.upper().lower())
print('Dicoding'.lower().upper())
print('DICODING'.upper().lower().islower())
print('DICODING'.upper().lower().isupper())

# c. isalpha() -> mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet,
# jika tidak maka akan mengembalikan nilai False.
print("dicoding".isalpha())

# d. isalnum() -> mengembalikan nilai True jika karakter dalam string adalah alfanumerik yaitu hanya
# huruf atau hanya angka atau berisi keduanya, jika tidak maka akan mengembalikan nilai False
print("dicoding123".isalnum())

# e. isdecimal() -> mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik,
# jika tidak maka akan mengembalikan nilai False
'12345'.isdecimal()

# f. isspace() -> mengembalikan nilai True jika string berisi hanya karakter whitespace, seperti spasi,
# tab, newline, atau karakter whitespaces lainnya, jika tidak maka akan mengembalikan nilai False
'    '.isspace()

# g. istitle() -> mengembalikan True jika string berisi huruf kapital di setiap kata dan dilanjutkan
# dengan huruf kecil seterusnya, jika tidak maka akan mengembalikan nilai False
'Dicoding Indonesia'.istitle()

# contoh implementasi
while True:
    print('Masukkan nama Anda:')
    name = input()
    if name.isalpha():
        print("Halo", name)
        break
    print('Masukkan nama Anda dengan benar.')


# 6. Formatting pada String
# a. zfill() -> metode yang dapat menambahkan nilai numerik berupa 0 di sebelah kiri sebuah angka atau string
# pada angka
    # Contoh 1: Penggunaan zfill 5 pada angka satuan
    angka = 5
    print (str(angka).zfill(5));
    # Contoh 2: Penggunaan zfill 5 pada angka ratusan
    angka = 300
    print (str(angka).zfill(5));
    # Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
    angka = -0.45 # outputnya sama yaitu -0.45, karena  jumlah karakter yang ada sudah berjumlah 5 yang di mana
                  # karakter koma (“,”) dan negatif (“-”) juga dihitung
    print (str(angka).zfill(5));
    # Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
    angka = -0.45
    print (str(angka).zfill(7));

# pada string
    # Contoh 1
    kata = 'aku'
    print (kata.zfill(5));
    # Contoh 2
    kata = 'kamu'
    print (kata.zfill(5));
    # Contoh 3
    kata = 'dirinya'
    print (kata.zfill(5));

# Teks rata kanan/kiri/tengah dengan rjust(), ljust(), dan center()
# b. rjust()
    'Dicoding'.ljust(20)
# Penjelasan: Dicoding'.rjust(20) dapat diartikan sebagai kita ingin menuliskan ‘Dicoding’
# dengan mode rata kanan yang total panjang stringnya adalah 20. Karena panjang ‘Dicoding’
# adalah 8 karakter, maka 12 spasi akan ditambahkan di sebelah kiri.
# Begitu pula pada 'Dicoding'.ljust(20). Kita ingin menuliskan ‘Dicoding’ dengan mode rata
# kiri yang total panjang stringnya adalah 20. Karena panjang ‘Dicoding’ adalah 8 karakter,
# maka 12 spasi akan ditambahkan di sebelah kanan.
# Selain spasi, Anda juga bisa menambahkan karakter lain dengan mengisikan parameter kedua
# pada fungsi rjust() atau ljust() seperti berikut:
    'Dicoding'.ljust(20, '!') #'Dicoding!!!!!!!!!!!!'

# c. center() -> Metode center() seperti namanya akan membuat teks menjadi rata tengah.
    'Dicoding'.center(20)
    'Dicoding'.center(20, '-')

# d. String Literals
    # st1 = 'Jum'at' -> contoh penggunaan yang salah
    st1 = "Jum'at"
    st1 = 'Jum\'at'
# Python mengetahui bahwa pada Jum\’at, sebelum petik terdapat backslash (\) yang menandakan petik
# tunggal merupakan bagian dari string dan bukan merupakan akhir dari string. Escape character \'
# dan \" memungkinkan Anda untuk memasukkan karakter ' dan '' dalam bagian string. Beberapa contoh
# Escape Character
    # \' Single quote
    # \" Double quote
    # \t Tab
    # \n Newline (line break)
    # \\ Backslash
    print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# 3 kutip-satu atau 3 kutip-dua, yang juga memiliki kemampuan untuk menyimpan String lebih dari satu
# baris (multi-line).
    multi_line = """Halo!
    Kapan terakhir kali kita bertemu?
    Kita bertemu hari Jum’at yang lalu."""
    print(multi_line)

# e. Raw Strings
#  untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan
    print(r'Dicoding\tIndonesia')
# Seharusnya, perintah \t akan membuat tab dan menghasilkan Dicoding    Indonesia, tapi karena kita
# menggunakan raw strings, maka kalimat tersebut secara mentah tercetak apa adanya.


