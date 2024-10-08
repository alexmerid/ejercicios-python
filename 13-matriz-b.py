# Escribir un programa para generar la siguiente matriz de n x n
#   Si n = 4
#   1   2   6    7
#   3   5   8   13
#   4   9   12  14
#   10  11  15  16

import numpy as np

n = int(input("N = "))
m = np.zeros([n, n], dtype=int)

f = 0
c = 0
inc = 1
for i in range(n*n):
    m[f][c] = i + 1
    f = f - inc
    c = c + inc
    if inc == 1:
        if c == n:
            f = f + 2
            c = c - 1
            inc = -1
        if f == -1:
            f = f + 1
            inc = -1
    if inc == -1:
        if f == n:
            c = c + 2
            f = f - 1
            inc = 1
        if c == -1:
            c = c + 1
            inc = 1

print(m)
