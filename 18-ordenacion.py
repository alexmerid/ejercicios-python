# Programa para ordenar una lista por diferentes métodos

# Ordenación burbuja
def burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux


# Ordenacion por selección
def seleccion(lista):
    for i in range(len(lista)-1):
        min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min]:
                min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux


# Ordenacion por inserción
def insercion(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
        j = i-1
        while elemento < lista[j] and j >= 0:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = elemento


lis = [13, 5, 23, 7, 9, 10, 12, -2, 32, 2]

print(lis)

# insercion(lis)
# seleccion(lis)
burbuja(lis)

print(lis)
