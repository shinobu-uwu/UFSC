from random import randint

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
        n = self.__numero #Não queremos modificar o numero dado pelo usuário
        resultado = 1
        while n > 1:
            resultado *= n
            n -= 1
        return resultado

class AnaliseCombinatoria:

    def __init__(self, elementos, posicoes):
        self.elementos = elementos
        self.posicoes = posicoes
        self.tamanho = len(elementos)

    #Para alguns métodos precisarei fazer uma cópia profunda para não alterar a lista inicial
    def copia(self, lista):
        lista_copiada = list()
        for elemento in lista:
            lista_copiada.append(elemento)
        return lista_copiada

    def permutacao(self):
        repeticoes = dict()
        for elemento in self.elementos:
            if elemento not in repeticoes:
                repeticoes[elemento] = 1
            else:
                repeticoes[elemento] += 1
        numerador = Fatorial(self.tamanho).resolve()
        denominador = 1
        for numero in repeticoes.values():
            denominador *= Fatorial(numero).resolve()
        print(repeticoes)
        return Fracao(numerador, denominador).decimal()

    def arranjo(self):
        numerador = Fatorial(self.tamanho).resolve()
        denominador = Fatorial(self.tamanho - self.posicoes).resolve()
        return Fracao(numerador, denominador).decimal()

    def combinacao(self):
        numerador = Fatorial(self.tamanho).resolve()
        denominador = Fatorial(self.posicoes).resolve() * Fatorial(self.tamanho - self.posicoes).resolve()
        return Fracao(numerador, denominador).decimal()
    
    #Permutar é simplesmente trocar a ordem dos elementos de uma sequência,
    #então só precisamos embaralhar a lista de forma aleatória que teremos uma das permutações
    def permutaAleatoria(self):
        elementos = self.copia(self.elementos)        
        resultado = list()                  
        for i in range(0, len(elementos)):
            j = randint(0, len(elementos) - 1)
            resultado.append(elementos[j])
            elementos.pop(j)
        return resultado

    #No caso do arranjo, a ordem dos elementos importa, então só precisamos agrupar os elementos da
    #sequência de forma aleatória, sem repetí-los
    def arranjoAleatorio(self):
        elementos = self.copia(self.elementos)
        resultado = list()
        for i in range(self.posicoes):
            j = randint(0, len(elementos) - 1)
            resultado.append(elementos[j])
            elementos.pop(j)
        return resultado

    
    def combinacaoAleatoria(self):
        combinacoes = list()
        
        return combinacoes


a = AnaliseCombinatoria(["B", "A", "E", "D", "E", "F", "G"], 3)
print(len(a.combinacaoAleatoria()))
print(a.combinacao())
