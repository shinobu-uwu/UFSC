#Para esta questão, eu farei um sistema de baralho o mais genérico possível, onde as únicas funções
#são as básicas para qualquer jogo de cartas, embaralhar e sacar. Todas as classes estão abertas para serem
#estendidas de acordo com o jogo e funcionalidades que quiserem implementar
from random import randint

class Carta:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Baralho:

    def __init__(self, cartas):
        self.cartas = cartas

class Jogador:

    def __init__(self, nome, mao_inicial, baralho):
        self.__mao = list()
        for i in range(0, mao_inicial):
            self.sacar()
        self.__baralho = baralho

    @property
    def mao(self):
        return self.__mao

    def sacar(self):
        self.__mao.append(self.__baralho.cartas[0])
        self.__baralho.cartas.pop(0)

    def embaralhar(self):
        baralho_embaralhado = list()
        for i in range(0, len(self.__baralho.cartas)):
            n = randint(0, len(self.__baralho.cartas) - 1)
            baralho_embaralhado.append(self.__baralho.cartas[n])
            self.__baralho.cartas.pop(n)
        for carta in baralho_embaralhado:
            self.__baralho.cartas.append(carta)