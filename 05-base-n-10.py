# Dado un número entero en base cualquiera transformarlo a su equivalente en base diez

nb = int(input("Número: "))
b = int(input("Base: "))
n10 = 0
e = 0
while nb > 0:
    n10 = n10 + nb % 10 * b**e
    e += 1
    nb = nb // 10

print("El número en base 10 es", n10)
