from random import randint
from copy import deepcopy

class Fracao:

    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador
    
    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    def decimal(self):
        return self.__numerador / self.__denominador

class Fatorial:

    def __init__(self, numero):
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    def resolve(self):
        n = self.__numero
        resultado = 1
        while n > 1:
            resultado *= n
            n -= 1
        return resultado

class AnaliseCombinatoria:

    def __init__(self, elementos, posicoes):
        self.__elementos = elementos
        self.__posicoes = posicoes
        self.__tamanho = len(elementos)

    #Para alguns métodos precisarei fazer uma cópia profunda para não alterar a lista inicial
    def __copia(self, lista):
        lista_copiada = list()
        for elemento in lista:
            lista_copiada.append(elemento)
        return lista_copiada

    def permutacao(self):
        repeticoes = dict()
        for elemento in self.__elementos:
            if elemento not in repeticoes:
                repeticoes[elemento] = 1
            else:
                repeticoes[elemento] += 1
        numerador = Fatorial(self.__tamanho).resolve()
        denominador = 1
        for numero in repeticoes.values():
            denominador *= Fatorial(numero).resolve()
        return Fracao(numerador, denominador).decimal()

    def arranjo(self):
        numerador = Fatorial(self.__tamanho).resolve()
        denominador = Fatorial(self.__tamanho - self.__posicoes).resolve()
        return Fracao(numerador, denominador).decimal()

    def combinacao(self):
        numerador = Fatorial(self.__tamanho).resolve()
        denominador = Fatorial(self.__posicoes).resolve() * Fatorial(self.__tamanho - self.__posicoes).resolve()
        return Fracao(numerador, denominador).decimal()
    
    #Permutar é simplesmente trocar a ordem dos elementos de uma sequência,
    #então só precisamos embaralhar a lista que teremos uma das permutações
    def permutaAleatoria(self):
        elementos = self.__copia(self.__elementos)        
        resultado = list()                  
        for i in range(0, len(elementos)):
            j = randint(0, len(elementos) - 1)
            resultado.append(elementos[j])
            elementos.pop(j)
        return resultado

    #No caso do arranjo, a ordem dos elementos importa, então só precisamos agrupar os elementos da
    #sequência de forma aleatória, sem repetí-los
    def arranjoAleatorio(self):
        elementos = self.__copia(self.__elementos)
        resultado = list()
        for i in range(self.__posicoes):
            j = randint(0, len(elementos) - 1)
            resultado.append(elementos[j])
            elementos.pop(j)
        return resultado

    #Como na combinação a ordem dos elementos não importa, precisamos apenas ordenar os elementos
    #do arranjo
    def combinacaoAleatoria(self):
        resultado = self.arranjoAleatorio()
        resultado.sort()
        return resultado

a = AnaliseCombinatoria(["A", "A", "B", "D", "C", "F", "O"], 3)
print(f"""
Número de prmutas possíveis: {a.permutacao()}
Permuta aleatória: {a.permutaAleatoria()}
Número de arranjos possíveis: {a.arranjo()}
Arranjo aleatório: {a.arranjoAleatorio()}
Número de combinações possíveis: {a.combinacao()}
Combinação aleatória: {a.combinacaoAleatoria()}""")