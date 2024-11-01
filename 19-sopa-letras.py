""" 
Programa para encontrar una palabra en una sopa de letras.
La sopa de letras debe ser cargada en el archivo 19-sopa-letras.txt
"""

from pathlib import Path


# Función para mostrar la sopa de letras
def mostrar_sopa(sop):
    for linea in sop:
        fila = ""
        for letra in linea:
            fila = fila + letra + " "
        print(fila)


def ver_pal(pal, sop, i, j, inc_i, inc_j):
    i_enc = i
    j_enc = j
    c_pal = 0
    enc = ""
    while c_pal < len(pal) and i < len(sop) and j < len(sop[0]) and sop[i][j] == pal[c_pal]:
        enc = enc+sop[i][j]
        i = i + inc_i
        j = j + inc_j
        c_pal += 1
    return (pal == enc)


def buscar(pal, sop):
    nf = len(sop)
    nc = len(sop[0])
    for f in range(nf):
        for c in range(nc):
            if ver_pal(pal, sop, f, c, 0, 1):
                print(f, c, "-", 0, 1)
            if ver_pal(pal, sop, f, c, 1, 0):
                print(f, c, "-", 1, 0)
            if ver_pal(pal, sop, f, c, 0, -1):
                print(f, c, "-", 0, -1)
            if ver_pal(pal, sop, f, c, -1, 0):
                print(f, c, "-", -1, 0)


archivo = Path("19-sopa-letras.txt")
lineas = archivo.read_text("utf-8").split("\n")

sopa = []
for linea in lineas:
    fila = []
    for letra in linea:
        fila.append(letra.upper())
    sopa.append(fila)

mostrar_sopa(sopa)
palabra = input("Palabra a buscar: ").upper()

buscar(palabra, sopa)
