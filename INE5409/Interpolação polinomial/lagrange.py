from math import sin, pi


def lagrange(x, y, ponto):
    n = len(x)
    p = 0
    for i in range(n):
        num = 1
        den = 1
        for j in range(n):
            if i != j:
                num *= (ponto - x[j])
                den *= (x[i] - x[j])
        p += y[i] * num/den
    return p

# Por padrão da linguagem, não é possível passar um float como parametro para o step do for
# Então criarei uma função para criar uma lista com a variação dos pontos desejada
def my_range(comeco, fim, variacao):
    n = comeco
    pontos = []
    while n <= fim:
        pontos.append(n)# Erros de representação ocorrem a torto e a direito...
        n += variacao
    return pontos

x = my_range(-pi, pi, 0.75)
y = [sin(x) for x in x]
print(f"""
Lagrange: {lagrange(x, y, 1)}
sin(1): {sin(1)}
""")
for xx in x:
    print(f"""
    Lagrange({xx}): {lagrange(x, y, xx)}
    sin({xx}): {sin(xx)}
    erro: {abs(sin(xx) - lagrange(x, y, xx))}
    """)