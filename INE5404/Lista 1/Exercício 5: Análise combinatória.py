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
        
