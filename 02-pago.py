# Calcular el total a pagar por la compra de un cierto producto, tomando en cuenta que si se
# compran tres o mas unidades de dicho producto, se aplica un descuento del 20% sobre el
# total de la compra y si son menos de tres unidades , un descuento del 10%

precio_uni = float(input("Precio unitario del producto: "))
cantidad = int(input("Cantidad: "))

if cantidad < 3:
    total = cantidad * precio_uni * 0.90
else:
    total = cantidad * precio_uni * 0.80

print("El total a pagar es", total)
