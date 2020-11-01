import numpy as np

def decomposicao_lu(a, b):
#incializa todas as matrizes necessárias com 0 e preenche a diagonal principal da matriz u com 1
    n = len(a[0])
    l = [[0 for j in range(len(a[0]))]for i in range(n)]
    u = [[0 for j in range(len(a[0]))]for i in range(n)]
    y = [0 for j in range(len(b))]
    x = [0 for j in range(len(b))]
    for i in range(len(u)):
        for j in range(len(u[0])):
            if i == j:
                u[i][j] = 1
#calcula l, em i, e u, em j
    for k in range(n):
        for i in range(k, n):
            s1 = sum(l[i][r] * u[r][k] for r in range(k))
            l[i][k] = a[i][k] - s1
        for j in range(k + 1, n):
            s2 = sum(l[k][t] * u[t][j] for t in range(k))
            u[k][j] = (a[k][j] - s2) / l[k][k]
#calcula a matriz y
    y[0] = b[0] / l[0][0]
    for i in range(1, n):
        y[i] = (b[i] - sum(l[i][j] * y[j] for j in range(i))) / l[i][i]
#calcula a solução varrendo a matriz de baixo para cima
    x[-1] = y[-1] / u[-1][-1]
    for i in range(n - 1, -1, -1):
        s = sum(u[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - s)/u[i][i]

    return l, u, y, x

a = [
        [4, 2, 3],
        [2, -4, -1],
        [-1, 1, 4]
    ]
b = [7, 1, -5]

resultado = decomposicao_lu(a, b)
print("l")
for linha in resultado[0]:
    print(linha)
print("u")
for linha in resultado[1]:
    print(linha)
print("y")
print(resultado[2])
print("x")
print(resultado[3])