from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, capacidade, andar, totalPesosas, totalAndaresPredio):
        self.__capacidade = capacidade
        self.__totalPessoas = totalPesosas
        self.__andarAtual = andar
        self.__totalAndaresPredio = totalAndaresPredio

    def descer(self):
        try:
            self.__andarAtual -= 1
        except self.__andarAtual == 0:
            raise ElevadorJahNoTerreoException
        else:
            return "Elevador desceu um andar!"
    
    def entraPessoa(self):
        try:
            self.__totalPessoas += 1
        except self.__totalPessoas == self.__capacidade:
            raise ElevadorCheioException
        else:
            return "Saiu uma pessoa!"

    def saiPessoa(self):
        try:
            self.__totalPessoas -= 1
        except self.__totalPessoas == 0:
            raise ElevadorJahVazioException
        else:
            return "Saiu uma pessoa"
    
    def subir(self):
        try:
            self.__andarAtual += 1
        except self.__andarAtual == self.__totalAndaresPredio:
            raise ElevadorJahNoUltimoAndarException
        else:
            return "Elevador subiu um andar!"

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