'''
Programa para generar el siguiente patron:
*   *
 * *
  *
 * *
*   *
'''

n = int(input("N: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i or j == (n-i+1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
