from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass
 
