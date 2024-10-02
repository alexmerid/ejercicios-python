# Leer una cadena de caracteres y generar una tabla con el número de veces de dos vocales contiguas en la cadena.
# Ejem.     ecuacion contigua y conciencia
#           A   E   I   O   U
#       A   0   0   0   0   0
#       E   0   0   0   0   0
#       I   1   1   0   0   0
#       O   0   0   0   0   0
#       U   2   0   0   0   0

tabla = [
        [' ', 'A', 'E', 'I', 'O', 'U'],
        ['A', 0, 0, 0, 0, 0],
        ['E', 0, 0, 0, 0, 0],
        ['I', 0, 0, 0, 0, 0],
        ['O', 0, 0, 0, 0, 0],
        ['U', 0, 0, 0, 0, 0]
]


def n_vocal(car):
    if car.lower() == 'a':
        return 1
    elif car.lower() == 'e':
        return 2
    elif car.lower() == 'i':
        return 3
    elif car.lower() == 'o':
        return 4
    elif car.lower() == 'u':
        return 5
    else:
        return 0


cadena = input("Escriba una cadena: ")

for i in range(len(cadena)-1):
    f = n_vocal(cadena[i])
    c = n_vocal(cadena[i+1])
    if f > 0 and c > 0:
        tabla[f][c] = tabla[f][c] + 1

for lista in tabla:
    fila = ''
    for elem in lista:
        fila = fila + str(elem) + '\t'
    print(fila)
