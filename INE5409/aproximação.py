def aproximação(x, n):
    soma = 1
    num = 1
    fat = 1
    for i in range(1, n):
        num *= x
        fat *= i
        soma += num / fat
    return soma

print(aproximação(2, 5))