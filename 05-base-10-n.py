# Dado un número entero en base 10 transformarlo a su equivalente en cualquier base

n = int(input("Número en base 10: "))
b = int(input("Base destino: "))
nb = 0
m = 1
while n > 0:
    nb = nb + (n % b) * m
    n = n // b
    m *= 10

print("El resultado es", nb)
