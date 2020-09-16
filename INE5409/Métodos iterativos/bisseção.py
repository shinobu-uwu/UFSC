import math

def bissecao(a, b, erro, funcao):
    fa = funcao(a)
    fb = funcao(b)
    fxm = erro + 1#Aqui pode ser qualquer número maior que o erro
    k = 0

    while abs(fxm) > erro:
        k += 1
        xm = (a + b) / 2
        fxm = funcao(xm)
        if fa*fxm < 0:
            b = xm
            fb = fxm
        else:
            a = xm
            fa = fxm
    return k, xm, fxm

#Letra a:
def f(x):#Função para ser usada na bisseção
    return math.exp(x) + x

print(bissecao(-1, 0, 10 ** (-2), f))

#Letra b:
def g(x):
    return math.exp(x) - (2 * math.cos(x))

print(bissecao(0, 2, 10 ** (-2), g))

#Letra c:
def h(x):
    return math.exp(x) * math.sin(x) - 1

print(bissecao(0, 1, 10 ** (-2), h))