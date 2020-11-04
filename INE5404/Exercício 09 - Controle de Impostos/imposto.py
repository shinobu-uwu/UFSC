from abc import ABC, abstractmethod


class Imposto(ABC):
    def __init__(self, aliquota, incidencia_imposto):
        self.__aliquota = aliquota
        self.__incidencia_imposto = incidencia_imposto

    @abstractmethod
    def calcula_aliquota(self):
        pass

    @property
    def aliquota(self):
        return self.__aliquota

    @property
    def incidencia_imposto(self):
        return self.__incidencia_imposto