""" 
Programa para encontrar una palabra en una sopa de letras.
La sopa de letras debe ser cargada en el archivo 19-sopa-letras.txt
"""

from pathlib import Path


# Función para mostrar la sopa de letras
def mostrar_sopa(sop, enc):
    nf = len(sop)
    nc = len(sop[0])

    for f in range(nf):
        fila = ""
        for c in range(nc):
            if enc[f][c]:
                fila = fila + "\033[1;34m" + sop[f][c] + "\033[m "
            else:
                fila = fila+sop[f][c] + " "
        print(fila)

# Función para "pintar" la matriz de encontrados


def pintar(pal, enc, i, j, inc_i, inc_j):
    for c in range(len(pal)):
        enc[i][j] = True
        i = i + inc_i
        j = j + inc_j


# Función para verificar si existe una palabra en una posicion de la Sopa
def ver_pal(pal, sop, i, j, inc_i, inc_j):
    i_enc = i
    j_enc = j
    c_pal = 0
    enc = ""
    while c_pal < len(pal) and sop[i][j] == pal[c_pal]:
        enc = enc+sop[i][j]
        i = i + inc_i
        j = j + inc_j
        c_pal += 1
        if i < 0 or i >= len(sop) or j < 0 or j >= len(sop[0]):
            break
    return (pal == enc)


# Función para recorrer letra a letra la Sopa para buscar la palabra
def buscar(pal, sop, enc):
    nf = len(sop)
    nc = len(sop[0])
    for f in range(nf):
        for c in range(nc):
            if ver_pal(pal, sop, f, c, 0, 1):
                pintar(pal, enc, f, c, 0, 1)
            if ver_pal(pal, sop, f, c, 1, 0):
                pintar(pal, enc, f, c, 1, 0)
            if ver_pal(pal, sop, f, c, 0, -1):
                pintar(pal, enc, f, c, 0, -1)
            if ver_pal(pal, sop, f, c, -1, 0):
                pintar(pal, enc, f, c, -1, 0)
            if ver_pal(pal, sop, f, c, 1, 1):
                pintar(pal, enc, f, c, 1, 1)
            if ver_pal(pal, sop, f, c, 1, -1):
                pintar(pal, enc, f, c, 1, -1)
            if ver_pal(pal, sop, f, c, -1, -1):
                pintar(pal, enc, f, c, -1, -1)
            if ver_pal(pal, sop, f, c, -1, 1):
                pintar(pal, enc, f, c, -1, 1)


archivo = Path("19-sopa-letras.txt")
lineas = archivo.read_text("utf-8").split("\n")

sopa = []
encontrados = []
for linea in lineas:
    fila = []
    fila_encontrados = []
    for letra in linea:
        fila.append(letra.upper())
        fila_encontrados.append(False)
    sopa.append(fila)
    encontrados.append(fila_encontrados)

mostrar_sopa(sopa, encontrados)
palabra = input("Palabra a buscar: ").upper()
buscar(palabra, sopa, encontrados)
print()
mostrar_sopa(sopa, encontrados)
