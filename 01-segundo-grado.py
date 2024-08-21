# Resolver una ecuación de segundo grado
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

print("x1 =", x1)
print("x2 =", x2)
