'''
Programa para generar el siguiente patron:
*****
****
***
**
*
'''

n = int(input("N: "))

for i in range(n, 0, -1):
    print("*" * i)
