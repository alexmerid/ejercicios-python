# Programa para contar el número de mayúsculas y minúsculas de una cadena de texto.

texto = input("Escriba una cadena de texto: ")

mayus = 0
minus = 0

for letra in texto:
    if letra.isalpha():
        if letra == letra.upper():
            mayus += 1
        elif letra == letra.lower():
            minus += 1

print(f"La cadena tiene {mayus} mayúsculas y {minus} minúsculas.")
