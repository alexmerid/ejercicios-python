# Programa para contar el número de vocales y consonantes en una cadena de texto.

vocales = list("aeiouáéíóú")
consonantes = list("bcdfghjklmnñpqrstvwxyz")

texto = input("Escriba una cadena de texto: ")

nv = 0
nc = 0
for letra in texto:
    if letra.lower() in vocales:
        nv += 1
    elif letra.lower() in consonantes:
        nc += 1
print(f"La cadena tiene {nv} vocales y {nc} consonantes.")
