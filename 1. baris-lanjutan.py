# DISARANKAN
# Opsi 1
# Rata kiri dengan kurung atau pemisah dengan argumen utama
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Opsi 2
# Tambahkan indentasi ekstra - (level indentasi baru) untuk memisahkan parameter/argument dari bagian lainnya
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Opsi 3
# Hanging indents dengan penambahan level indentasi saja
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Hanging indents *boleh* menggunakan selain 4 spasi
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


# TIDAK DISARANKAN
# Contoh kesalahan 1
# Tidak rata kiri dengan bagian yang relevan
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Contoh kesalahan 2
# Sulit dibedakan antara baris lanjutan atau fungsi baru
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# NOTE : ython Standard Library selalu dikembangkan secara konservatif dan mempertahankan
# standar 79 karakter pada kode, dan 72 pada komentar/dokumentasi.

