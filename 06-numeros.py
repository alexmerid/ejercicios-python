# Leer n números y mostrar el cuadrado y el cubo de los mismos.
# Además mostrar cuántos son multiplos de 3 y de 5

numeros = []
n = int(input("N: "))
for i in range(1, n + 1):
    num = int(input(f"N{i}: "))
    numeros.append(num)
m3 = 0
m5 = 0
for i in range(n):
    print(f"{numeros[i]} \t {numeros[i]**2} \t {numeros[i]**3}")
    if numeros[i] % 3 == 0:
        m3 += 1
    if numeros[i] % 5 == 0:
        m5 += 1
print(f"{m3} son múltiplos de 3")
print(f"{m5} son múltiplos de 5")
