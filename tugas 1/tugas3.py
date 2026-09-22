n = int(input("Masukkan angka anda: "))
a, b = 0, 1

print("Deret Fibonacci hingga", n, ":")
while a <= n:
    print(a)
    a, b = b, a + b
