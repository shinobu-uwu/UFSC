from abc import ABC, abstractmethod
from animal import Animal

class Ave(Animal, ABC):
    def __init__(self, tamanho_passo, altura_voo):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo

    def mover(self):
        return super().mover() + " VOANDO"

    @abstractmethod
    def produzir_som(self):
        return "AVE: PRODUZ SOM: "