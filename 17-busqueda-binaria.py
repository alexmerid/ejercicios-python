# Buśqueda binaria en una lista ordenada

def buscar(lis, elem):
    ini = 0
    fin = len(lis) - 1
    medio = fin // 2
    while (fin > ini) and (lis[medio] != elem):
        if elem > lis[medio]:
            ini = medio + 1
        else:
            fin = medio - 1
        medio = (fin + ini) // 2
    if elem == lis[medio]:
        return medio
    else:
        return -1


lista = [-1.2, 0.5, 1.0, 2.0, 3.4, 5.0, 7.0, 8.6, 9.2]

elemento = float(input("Elemento a buscar: "))

i = buscar(lista, elemento)
if i == -1:
    print("El elemento no existe.")
else:
    print(f"El elemnto fué encontrado en la posición {i}.")
