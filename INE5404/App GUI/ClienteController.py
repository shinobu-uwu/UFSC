from ClienteView import ClienteView
from Cliente import Cliente
from ClienteDAO import ClienteDAO
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clienteDAO = ClienteDAO()

    def inicia(self):
        container = self.__telaCliente.tela_consulta()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            print(self.__clienteDAO.cache)
            event, values = self.__telaCliente.le_eventos()
            if event == sg.WIN_CLOSED:
                self.__clienteDAO.dump()
                rodando = False
            elif event == 'Cadastrar':
                try:
                    self.adiciona_cliente(values["codigo"], values["nome"])
                except AssertionError:
                    resultado = "Usuário já cadastrado!"
                else:
                    resultado = "Usuário cadastrado com sucesso!"                 
            elif event == 'Consultar':
                if values["codigo"] != '':
                    try:
                        resultado = self.busca_codigo(str(values["codigo"]))
                    except KeyError:
                        resultado = "Cliente não encontrado!"
                    else:
                        resultado = f"Nome: {resultado.nome}, código: {resultado.codigo}"
                else:
                    try:
                        lista_resutlado = self.busca_nome(values["nome"])
                    except LookupError:
                        resultado = "Cliente não encontrado!"
                    else:
                        resultado = ''
                        for cliente in lista_resutlado:
                            resultado += f"Nome: {cliente.nome} Código: {cliente.codigo}. "
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)
                
        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clienteDAO.get(codigo)
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        cliente = Cliente(codigo, nome)
        if str(codigo) not in self.__clienteDAO.cache.keys():
            self.__clienteDAO.add(cliente)
        else:
            raise AssertionError
    
    def busca_nome(self, nome):
        resultado = []
        for key in self.__clienteDAO.cache.keys():
            if self.__clienteDAO.cache[key].nome == nome:
                resultado.append(self.__clienteDAO.cache[key])
        return resultado