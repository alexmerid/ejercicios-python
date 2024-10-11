# Se tiene la sigueinte información correspondiente a cada uno de los alumnos de un curso:
#       Nombre, Primer Parcial, Segundo Parcial, Examen Final
#
# Usando listas y diccionarioss realizar un programa que tenga las siguientes opciones:
#       1. Adicionar datos.
#       2. Eliminar datos.
#       3. Modificar datos.
#       4. Listar de datos
#       5. Salir del programa.

def adicionar(cur):
    nombre = input("Nombre del Estudiante: ")
    pp = float(input("Primer Parcial: "))
    sp = float(input("Segundo Parcial: "))
    ef = float(input("Exámen Final: "))
    estudiante = dict(Nombre=nombre, PP=pp, SP=sp, EF=ef)
    cur.append(estudiante)


def eliminar(cur):
    listar(cur)
    n = int(
        input("Escriba el número del estudiante del cual desea eliminar sus datos: "))
    n -= 1
    if n < 0 or n >= len(cur):
        print("Ése estudiante NO existe.")
        return
    print(
        f"Los datos del estudiante \"{cur[n]['Nombre']}\" serán eliminados.")
    res = input("¿Está seguro? (S/N): ")
    if res.lower() == "s":
        cur.pop(n)
        print("Se eliminaron los datos del estudiante.")
    else:
        print("Eliminación cancelada.")


def modificar(cur):
    listar(cur)
    n = int(
        input("Escriba el número del estudiante del cual desea modificar sus datos: "))
    n -= 1
    if n < 0 or n >= len(cur):
        print("Ése estudiante NO existe.")
        return
    print("Escriba los nuevos datos del estudiante (Enter para mantener los datos)")
    nombre = input(f"Nombre del Estudiante ({cur[n]['Nombre']}): ")
    if nombre != "":
        cur[n]['Nombre'] = nombre
    pp = input(f"Primer Parcial ({cur[n]['PP']}): ")
    if pp != "":
        cur[n]['PP'] = float(pp)
    sp = input(f"Segundo Parcial ({cur[n]['SP']}): ")
    if sp != "":
        cur[n]['SP'] = float(sp)
    ef = input(f"Exámen Final ({cur[n]['EF']}): ")
    if ef != "":
        cur[n]['EF'] = float(ef)


def listar(cur):
    print("Nº\tNOMBRE\t\t\tPP\tSP\tEF")
    n = 0
    for estudiante in cur:
        n += 1
        print(
            f"{n}\t{estudiante['Nombre']:24}{estudiante['PP']}\t{estudiante['SP']}\t{estudiante['EF']}")


# curso = [
#     {"Nombre": "Samantha Mérida",
#      "PP": 70,
#      "SP": 80,
#      "EF": 75},
#     {"Nombre": "Cristian",
#      "PP": 75,
#      "SP": 68,
#      "EF": 85}
# ]

curso = []
while True:
    print("""
                    MENÚ
            1. Adicionar datos.
            2. Eliminar datos.
            3. Modificar datos.
            4. Listar de datos
            5. Salir del programa.
          """)
    op = input("Elija una opcion: ")
    if op == "1":
        adicionar(curso)
    elif op == "2":
        eliminar(curso)
    elif op == "3":
        modificar(curso)
    elif op == "4":
        listar(curso)
    elif op == "5":
        break
    else:
        print("OPCIÓN INCORRECTA.")
