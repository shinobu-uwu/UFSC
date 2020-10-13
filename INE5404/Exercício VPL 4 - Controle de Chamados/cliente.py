from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, codigo, nome):
        self.__nome = nome
        self.__codigo = codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo

    def __eq__(self, cliente):
        return self.__codigo == cliente.codigo