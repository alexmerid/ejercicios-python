# Resolver un sistema de n ecuaciones con n incógnitas por cualquier método

# Función para leer los valores de la matriz de coeficientes y el vector de constantes
def leer(m, v, n):
    print("\nIngrese los valores para la matriz de coeficientes:")
    for f in range(n):
        for c in range(n):
            m[f][c] = float(input(f"M[{f+1}][{c+1}]: "))
    print("\nIngrese los valores para el vector de constantes:")
    for f in range(n):
        v[f] = float(input(f"V[{f+1}]: "))

# Función para el método de Gauss Jordan


def gauss_jordan(m, v, n):
    # Eliminación hacia adelante
    for f in range(n-1):
        v[f] = v[f]/m[f][f]
        for c in range(n-1, f-1, -1):
            m[f][c] = m[f][c]/m[f][f]
        for i in range(f+1, n):
            aux = m[i][f]
            for c in range(f, n):
                m[i][c] = m[i][c]-m[f][c]*aux
            v[i] = v[i]-v[f]*aux

    # Eliminación hacia atrás
    for f in range(n-1, 0, -1):
        v[f] = v[f]/m[f][f]
        m[f][f] = 1
        for i in range(f-1, -1, -1):
            v[i] = v[i]-v[f]*m[i][f]
            m[i][f] = 0


num = int(input("Número de ecuaciones e incógnitas: "))

# Inicalizar el vector de constantes
vec = [0] * num

# Inicializar la matriz de coeficientes
mat = []
for i in range(num):
    a = [0]*num
    mat.append(a)

leer(mat, vec, num)

gauss_jordan(mat, vec, num)

print("\El vector solución es:")
print(vec)
