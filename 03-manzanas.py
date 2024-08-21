
# Una frutería ofrece las manzanas con descuento según la siguiente tabla:
#  0    -  2 Kg   sin descuento
#  2.01 -  5 Kg   10% de descuento
#  5.01 - 10 Kg   15% de descuento
# 10.01 Kg o más  20% de descuento
# Determinar cuanto pagaŕa una persona que compre manzanas en esa frutería

precio = float(input("Precio Kg de manzanas: "))
kilos = float(input("Cantidad de Kg: "))

if kilos < 2:
    descuento = 0
elif kilos < 5:
    descuento = 0.1
elif kilos < 10:
    descuento = 0.15
else:
    descuento = 0.2

total = precio * kilos * (1 - descuento)
print("El total a pagar es", total)
