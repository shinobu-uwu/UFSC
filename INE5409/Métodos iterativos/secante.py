import math

def secante(x0, x1, erro, f):
    f0 = f(0)
    f1 = f(1)
    k = 0
    while (abs(f1) > erro):
        k += 1
        xk = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        x0 = x1
        x1 = xk
        f0 = f1
        f1 = f(x1)
    return xk, f1, k

def f(x): #Exemplo qualquer
    return x**5 + 7 * x - 6

print(secante(1, 3, 10 ** -6, f))