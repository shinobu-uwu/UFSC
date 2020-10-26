from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        pass

    def subir(self):
        try:
            self.__elevador.subir()
        except ElevadorJahNoUltimoAndarException:
            raise ElevadorJahNoUltimoAndarException
        else:
            return "Elevador subiu 1 andar!"

    def descer(self):
        try:
            self.__elevador.descer()
        except ElevadorJahNoTerreoException:
            raise ElevadorJahNoTerreoException
        else:
            return "Elevador desceu 1 andar!"

    def entraPessoa(self):
        try:
            self.__elevador.entraPessoa()
        except ElevadorCheioException:
            raise ElevadorCheioException
        else:
            return "Entrou uma pessoa no elevador!"

    def saiPessoa(self):
        try:
            self.__elevador.saiPessoa()
        except ElevadorJahVazioException:
            raise ElevadorJahVazioException
        else:
            return "Saiu uma pessoa do elevador!"

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        if isinstance(andarAtual, int) and isinstance(totalAndaresPredio, int) and isinstance(capacidade, int) and isinstance(totalPessoas, int) and\
        andarAtual >= 0 and totalAndaresPredio >= 0 and capacidade >= 0 and totalPessoas >= 0 and\
        andarAtual < totalAndaresPredio and totalPessoas <= capacidade:
            self.__elevador = Elevador(capacidade, totalPessoas, andarAtual, totalAndaresPredio)
        else:
            raise ComandoInvalidoException

    @property
    def elevador(self):
        return self.__elevador