a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a > b and a > c:
    print("Angka terbesar adalah:", a)
elif b > a and b > c:
    print("Angka terbesar adalah:", b)
elif c > a and c > b:
    print("Angka terbesar adalah:", c)
else:
    print("tidak ada nilai terbesar")