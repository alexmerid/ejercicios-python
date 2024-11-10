'''
Programa para generar el siguiente patron:
*****
*   *
*   *
*   *
*****
'''

n = int(input("N: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")
