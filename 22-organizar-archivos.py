# Programa para organizar los archivos de un directorio en subdirectorios de acuerdo a su tipo.
from pathlib import Path
import os
import shutil

patrones = [("*.txt", "Textos"),
            ("*.png", "Imagenes"),
            ("*.py", "Python"),
            ("*.md", "Markdown")]

# directorio = Path("/home/alexander/Tmp/")
directorio = Path(input("Ingrese el directorio a organizar: "))
if (not directorio.exists()) or (not directorio.is_dir()):
    print("Debe ingresar un  directorio válido")
    exit()
print("Organizando...")
for p in patrones:
    archivos = [a for a in directorio.glob(p[0])]
    if len(archivos) > 0:
        nuevo_dir = str(directorio) + "/" + p[1]
        if not os.path.exists(nuevo_dir):
            os.mkdir(nuevo_dir)
        for a in archivos:
            shutil.move(a, nuevo_dir)
            print(f"{a} --> {nuevo_dir}")  # Revisar
