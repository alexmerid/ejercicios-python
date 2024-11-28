# Programa para buscar archivos en un directorio específico a partir de un término de búsqueda
from pathlib import Path

directorio = input("Ingrese el directorio dónde buscar: ")
ruta = Path(directorio)
if (not ruta.exists()) or (not ruta.is_dir()):
    print("Debe ingresar un  directorio válido")
    exit()
buscar = input("Ingrese el término de búsqueda: ")
print("Los archivos que coinciden con el término de búsqueda son:")
for i in ruta.iterdir():
    if i.is_file():
        if buscar in str(i):
            print(i)
