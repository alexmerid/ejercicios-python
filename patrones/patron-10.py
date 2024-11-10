'''
Programa para generar el siguiente patron:
    *
   * *
  *   *
 *     *
*********
'''

n = int(input("N: "))

for i in range(1, n):
    print(" " * (n - i) + "*" + " " * (2*i-3) + ("*" if i > 1 else ""))
print("*" * (n*2-1))
