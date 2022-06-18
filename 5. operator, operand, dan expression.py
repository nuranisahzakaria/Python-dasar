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