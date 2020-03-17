"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

from copy import deepcopy

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        array_ordenado = list()

        while self.array != []:
            minimo = self.achaMinimo(self.array)
            array_ordenado.append(minimo)
            self.array.pop(self.array.index(minimo))  

        self.array = deepcopy(array_ordenado)         

        return array_ordenado

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """
        resultado = ""
        for i in range(len(self.array)):
            if i != len(self.array) - 1:
                resultado += str(self.array[i]) + ","
            else:
                resultado += str(self.array[i])
        
        return resultado 

    def achaMinimo(self, lista):
        minimo = lista[0]
        for numero in lista:
            if numero < minimo:
                minimo = numero

        return minimo
            
