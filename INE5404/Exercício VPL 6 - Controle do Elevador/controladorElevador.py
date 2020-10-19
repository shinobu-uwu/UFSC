from abstractControladorElevador import AbstractControladorElevador
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorCheioException import ElevadorCheioException
from elevadorJahVazioException import ElevadorJahVazioException
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador

class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = Elevador(0, 0, 30, 30)

    def subir(self):
        try:
            self.__elevador.subir()
        except ElevadorJahNoUltimoAndarException:
            raise ElevadorJahNoUltimoAndarException
        else:
            return "Elevador subiu um andar!"

    def descer(self):
        try:
            self.__elevador.descer()
        except ElevadorJahNoTerreoException:
            raise ElevadorJahNoTerreoException
        else:
            return "Elevador desceu um andar!"

    def entraPessoa(self):
        try:
            self.__elevador.entraPessoa()
        except ElevadorCheioException:
            raise ElevadorCheioException
        else:
            return "Entrou uma pessoa!"

    def saiPessoa(self):
        try:
            self.__elevador.saiPessoa()
        except ElevadorJahVazioException:
            raise ElevadorJahVazioException
        else:
            return "Saiu uma pessoa!"

    @property
    def elevador(self):
        return self.__elevador

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        if isinstance(andarAtual, int) and andarAtual >= 0 and andarAtual <= totalAndaresPredio and isinstance(totalAndaresPredio, int) and totalAndaresPredio\
 >= 0 and isinstance(capacidade, int) and capacidade >= 0 and isinstance(totalPessoas, int) and totalPessoas >= 0 and totalPessoas <= capacidade:
            self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
        else:
            raise ComandoInvalidoException