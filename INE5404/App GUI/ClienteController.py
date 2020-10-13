from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

    def inicia(self):
        container = self.__telaCliente.tela_consulta()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                self.adiciona_cliente(values["codigo"], values["nome"])                   
            elif event == 'Consultar':
                if values["codigo"] != '':
                    try:
                        resultado = self.busca_codigo(str(values["codigo"]))
                    except KeyError:
                        resultado = "Cliente não encontrado!"
                    else:
                        resultado = f"Nome: {resultado.nome} Código: {resultado.codigo}"
                else:
                    try:
                        resultado = self.busca_nome(values["nome"])
                    except LookupError:
                        resultado = "Cliente não encontrado!"
                    else:
                        resultado = f"Nome: {resultado.nome} Código: {resultado.codigo}"
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)
                
        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def busca_nome(self, nome):
        for key, cliente in self.__clientes.items():
            if cliente.nome == nome:
                return cliente

        raise LookupError