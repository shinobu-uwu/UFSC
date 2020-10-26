from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, capacidade, totalPessoas, andarAtual, totalAndaresPredio):
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas
        self.__totalAndaresPredio = totalAndaresPredio
        self.__andarAtual = andarAtual

    def descer(self):
        if self.__andarAtual == 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andarAtual -= 1
            return str(self.__andarAtual)

    def entraPessoa(self):
        if self.__totalPessoas == self.__capacidade:
            raise ElevadorCheioException
        else:
            self.__totalPessoas += 1
            return str(self.__totalPessoas)

    def saiPessoa(self):
        if self.__totalPessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.__totalPessoas -= 1
            return str(self.__totalPessoas)

    def subir(self):
        if self.__andarAtual == self.__totalAndaresPredio:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andarAtual += 1
            return str(self.__andarAtual)

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def totalPessoas(self):
        return self.__totalPessoas

    @property
    def totalAndaresPredio(self):
        return self.__totalAndaresPredio

    @property
    def andarAtual(self):
        return self.__andarAtual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio):
        self.__totalAndaresPredio = totalAndaresPredio