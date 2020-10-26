def gauss(matriz):
    for k in range(len(matriz[0]) - 1):#o último elemento da linha é o termo independente
        for i in range(k + 1, len(matriz)):
            """Só queremos zerar as colunas de valor maior que k, exemplo: 
                vamos zerar a segunda e terceira linha da primeira coluna,
                terceira linha da segunda coluna e assim por diante"""
            pivo = matriz[i][k] / matriz[k][k]                  
            for j in range(len(matriz[i])):                     
                matriz[i][j] -= pivo * matriz[k][j]
    return matriz
    
#Exemplo
a = [
        [3, 5, 7, 9],
        [4, 5, 4, 3],
        [12, 16, 15, 2]
    ]
print(gauss(a))