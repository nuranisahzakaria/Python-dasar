# CONTOH 1
z = 0
try:
    x = 1 / z
    print(x)
except ZeroDivisionError:
    print('tidak bisa membagi angka dengan nilai nol')

# CONTOH 2
# try:
#         with open('contoh_tidak_ada.py') as file:
#              print(file.read())
#      except (FileNotFoundError, ):
#          print('file tidak ditemukan')

# CONTOH 3
d = {'ratarata': '10.0'}
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except ValueError:
    print('nilai tidak sesuai')

# kunci tidak ditemukan di dictionary
try:
    print('rata-rata: {}'.format(d['ratarata']/3))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('nilai atau tipe tidak sesuai')
# nilai atau tipe tidak sesuai
try:
    print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:
    print('penangan kesalahan: {}'.format(e))

# penangan kesalahan: invalid literal for int() with base 10: '10.0'


# BENTUK LENGKAP DARI PERNYATAAN TRY ADALAH SBB:
# try:
    # pass      (pernyataan yang mungkin terjadi pengecualian)
# except:
    # pass      (pernyataan dioperasikan jika terjadi pengecualian)
# else:
    # pass      (pernyataan dioperasikan jika tidak terjadi pengecualian)
# finally:
    # pass      (pernyataan dioperasikan setelah semua pernyataan diatas terjadi)

# Misalnya dalam contoh berikut, Anda mewajibkan sebuah
# dictionary memiliki kunci (key) total.
d = {'ratarata': '10.0'}
if 'total' not in d:
    raise KeyError('harus memiliki total')