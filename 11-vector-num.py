# Leer una lista de n elementos y un número a. Posteriormente generar dos listas, la primera con
# los números menores o iguales que a y la segunda con los números mayores que a.

def mostrar_lista(lista):
    for i in lista:
        print(i)


n = int(input("N: "))
lista = []
for i in range(n):
    elem = int(input(f"Elemento {i+1}: "))
    lista.append(elem)
a = int(input("A: "))
lista_men = []
lista_may = []
for elem in lista:
    if elem <= a:
        lista_men.append(elem)
    else:
        lista_may.append(elem)
print(f"Los elementos menores o iguales que {a} son:")
print(lista_men)
print(f"Los elementos mayores que {a} son:")
print(lista_may)
