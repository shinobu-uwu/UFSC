import math

def falsa_posicao(a, b, erro, funcao):
    fa = funcao(a)
    fb = funcao(b)
    fxk = erro + 1
    k = 0

    while abs(fxk) > erro:
        k += 1
        xk = a - ((fa * (b - a))/ (fb - fa))
        fxk = funcao(xk)
        if fa*fxk < 0:
            b = xk
            fb = fxk
        else:
            a = xk
            fa = fxk
    return k, xk, fxk

#Letra a:
def f(x):#Função para ser usada na falsa posição
    return math.exp(x) + x

print(falsa_posicao(-1, 0, 10 ** (-2), f))

#Letra b:
def g(x):
    return math.exp(x) - (2 * math.cos(x))

print(falsa_posicao(0, 2, 10 ** (-2), g))

#Letra c:
def h(x):
    return math.exp(x) * math.sin(x) - 1

print(falsa_posicao(0, 1, 10 ** (-2), h))
