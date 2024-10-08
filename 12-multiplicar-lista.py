# Programa para leer dos números enteros, almacenarlos dígito a dígito cada uno en una lista,
# para luego generar otra lista con la multiplicación de estos números

n1 = input("Escriba el primer número: ")
n2 = input("Escriba el segundo número: ")

v1 = list(map(int, n1))
l1 = len(n1)
v2 = list(map(int, n2))
l2 = len(n2)

v1.reverse()
v2.reverse()
v = [0] * (l1 + l2)

for b in range(l2):
    acarreo = 0
    c = b
    for a in range(l1):
        aux = v[c] + v1[a] * v2[b] + acarreo
        v[c] = aux % 10
        acarreo = aux // 10
        c += 1
    if acarreo > 0:
        v[c] = v[c] + acarreo

v.reverse()
print(v)
