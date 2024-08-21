# Calcular la sumatoria de los primeros n elementos de la siguiente serie:
# S = 1/n! - 3/(n-1)! + 5/(n-2)! - 7/(n-3)! + .........

n = int(input("Número de elementos: "))
signo = 1
num = 1
fact = 1
for i in range(2, n + 1):
    fact = fact * i
s = 0.0
for i in range(n):
    s = s + signo * num / fact
    signo = signo * (-1)
    num += 2
    fact = fact // (n - i)
print("Sumatoria =", s)
