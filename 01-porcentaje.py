# Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres
# hay en un grupo de estudiantes

hombres = int(input("Cantidad de hombres: "))
mujeres = int(input("Cantidad de mujeres: "))
total = hombres + mujeres
porcentaje_hom = hombres*100/total
porcentaje_muj = mujeres*100/total
print(f"El porcentaje de Hombres es {porcentaje_hom} %")
print(f"El porcentaje de Mujeres es {porcentaje_muj} %")
