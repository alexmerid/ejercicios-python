# Programa para organizar los archivos de un directorio en subdirectorios de acuerdo a su tipo.
from pathlib import Path

patrones = [("*.txt", "Textos"),
            ("*.png", "Imagenes"),
            ("*.py", "Python"),
            ("*.md", "Markdown")]

directorio = Path("/home/alexander/Tmp/")

for p in patrones:
    archivos = [a for a in directorio.glob(p[0])]
    if len(archivos) > 0:
        print(p[1])
        for a in archivos:
            print(f"{a} --> {a}/{p[1]}")  # Revisar
        print()
