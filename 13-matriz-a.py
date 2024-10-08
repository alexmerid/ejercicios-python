# Escribir un programa para generar la siguiente matriz de n x n
#   Si n = 4
#   1   2   3   4
#   2   3   4   3
#   3   4   3   2
#   4   3   2   1

import numpy as np

n = int(input("N = "))
m = np.ones([n, n], dtype=int)

for i in range(n):
    t = i + 1
    if t < n:
        inc = 1
    else:
        inc = -1
    for j in range(n):
        m[i][j] = t
        t = t + inc
        if t > n:
            t = t - 2
            inc = -1

print(m)
