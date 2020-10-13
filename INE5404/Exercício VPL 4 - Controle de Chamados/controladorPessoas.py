from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def tecnicos(self):
        return self.__tecnicos

    def incluiCliente(self, codigo, nome):
        cliente = Cliente(codigo, nome)
        for clientes in self.__clientes:
            if clientes.codigo == cliente.codigo:
                return
        self.__clientes.append(cliente)
        return cliente
    
    def incluiTecnico(self, codigo, nome):
        tecnico = Tecnico(codigo, nome)
        for tecnicos in self.__tecnicos:
            if tecnicos.codigo == tecnico.codigo:
                return
        self.__tecnicos.append(tecnico)
        return tecnico