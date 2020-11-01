def gauss(matriz):
    for k in range(len(matriz[0]) - 1):#o último elemento da linha é o termo independente
        for i in range(k + 1, len(matriz)):
            """Só queremos zerar as colunas de valor maior que k, exemplo: 
                vamos zerar a segunda e terceira linha da primeira coluna,
                terceira linha da segunda coluna e assim por diante"""
            pivo = matriz[i][k] / matriz[k][k]                  
            for j in range(len(matriz[i])):                     
                matriz[i][j] -= pivo * matriz[k][j]
    solucao = [0 for x in range(len(matriz))]
    solucao[-1] = matriz[-1][-1] / matriz[-1][-2]
    for i in range(len(matriz) - 2, -1, -1):
        soma = 0
        for j in range(i + 1, len(matriz)):
            soma = soma + a[i][j] * solucao[j]
        solucao[i] = (matriz[i][-1] - soma) / matriz[i][i]
    return solucao
    
#Exercício
a = [
        [4, 2, 3, 7],
        [2, -4, -1, 1],
        [-1, 1, 4, -5]
    ]

resultado = gauss(a)
for i in range(len(resultado)):
    print(f"x{i + 1}: {resultado[i]}")