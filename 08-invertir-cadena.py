# Programa para invertir una cadena de dos maneras.

texto = input("Escriba una cadena de texto: ")

# Primera manera
inverso = ""
for letra in texto:
    inverso = letra+inverso
print("La cadena invertida es: ", inverso)

# Segunda manera
print("La cadena invertida es: ", texto[::-1])
