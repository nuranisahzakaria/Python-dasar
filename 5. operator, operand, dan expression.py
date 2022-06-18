# ...................OPERATOR, OPERANDS, DAN EXPRESSIONS....................
# Operasi Bit
    # << (left shift)
        # Menggeser representasi bit/binary dari operand pertama sebanyak operand kedua ke kiri
print(2 << 2)
        # menghasilkan 8
        # 2 direpresentasikan sebagai 10 dalam binary
        # Geser ke kiri sebanyak 2x, menjadi 1000 (tambahkan 0 di belakangnya)
        # 1000 dalam binary bernilai 8 dalam desimal

    # >> (right shift)
        # Menggeser representasi bit/binary dari operand pertama sebanyak operand kedua ke kanan
print(11 >> 1)
        # menghasilkan 5
        # 11 direpresentasikan sebagai 1011 dalam binary.
        # Geser ke kanan sebanyak 1x, menjadi 101.
        # 101 dalam binary bernilai 5 dalam desimal.

    # & (bit-wise AND)
        # Menjalankan operasi binary AND pada representasi operand pertama dan kedua.
print(5 & 3)
        # menghasilkan 1.
        # Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011. 101 and 011 bernilai 001.
        # 001 dalam desimal adalah 1.

    # | (bit-wise OR)
        # Menjalankan operasi binary OR pada representasi operand pertama dan kedua.
print(5 | 3)
        # menghasilkan 7.
        # Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011. 101 or 011 bernilai 111.
        # 111 dalam desimal adalah 7.

    # ^ (bit-wise XOR)
        # Menjalankan operasi binary XOR pada representasi operand pertama dan kedua.
print(5 ^ 3)
        # menghasilkan 6.
        # Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011. 101 xor 011 bernilai 110.
        # 110 dalam desimal adalah 6.

    # ~ (bit-wise invert)
        # Menjalankan operasi binary invert pada representasi operand. Nilai invert dari x adalah -(x+1), menggunakan metode Two’s Complement
print(~5)
        # menghasilkan -6

# Operator Perbandingan
    # < atau operator.lt (less than)
    # > atau operator.gt (greater than)
    # <= atau operator.le (less than or equal to)
    # >= atau operator.ge (greater than or equal to)
    # != atau operator.ne (not equal to)
from operator import *
hijau = 5
kuning = 10
print('Kelereng Hijau = {}'.format(hijau))
print('Kelereng Kuning = {}'.format(kuning))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(hijau, kuning): {}'.format(func.__name__, func(hijau, kuning)))