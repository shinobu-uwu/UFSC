def gauss_pp(matriz):
    maximo = matriz[0][0]#Pode ser qualquer elemento da primeira coluna
    linha = matriz[0] #Armazenar a linha do elemento
    for i in range(len(matriz)):
        if abs(maximo) < abs(matriz[i][0]):
            maximo = matriz[i][0]
            linha = matriz[i]
    matriz.remove(linha)
    matriz.insert(0, linha)
    #A partir daqui é exatamente igual a gauss sem pivotamento
    for k in range(len(matriz[0]) - 1):
        for i in range(k + 1, len(matriz)):
            pivo = matriz[i][k] / matriz[k][k]                  
            for j in range(len(matriz[i])):                     
                matriz[i][j] -= pivo * matriz[k][j]
    solucao = [0 for x in range(len(matriz))]
    solucao[-1] = matriz[-1][-1] / matriz[-1][-2]
    for i in range(len(matriz) - 2, -1, -1):
        soma = 0
        for j in range(i + 1, len(matriz)):
            soma = soma + matriz[i][j] * solucao[j]
        solucao[i] = (matriz[i][-1] - soma) / matriz[i][i]
    return solucao
    
#Exercício
a = [
        [1, -1, 1, 1],
        [2, 3, -1, 4],
        [-3, 1, 1, -1]
    ]
print(gauss_pp(a))