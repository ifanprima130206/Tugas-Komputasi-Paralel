import numpy as np

def f(x):
        return x**2

a = int(input("Masukan batas bawah (a): "))
b = int(input("Masukan batas atas (b): "))

n = int(input("Masukan jumlah partisi (n): "))

h = (b - a) / n

x = np.linspace(a, b, n+1)
y = f(x)
integral = (h/2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])

print("Hasil integrasi numerik: ", integral)