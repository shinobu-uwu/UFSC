import PySimpleGUI as sg 

# View do padrão MVC
class ClienteView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))
        self.__theme = sg.theme("Reddit")

    def tela_consulta(self):
        self.__container = [
                            [sg.Text(text = "Digite o código ou o nome do cliente e clique na ação desejada:", font = ("Helvetica", 14))],
                            [sg.Text(text = "Nome", font = ("Helvetica", 14)), sg.InputText(size = (50, 50), font = ("Helvectica", 14), key = "nome")],
                            [sg.Text(text = "Código", font = ("Helvetica", 14)), sg.InputText(size = (50, 50), font = ("Helvectica", 14), key = "codigo")],
                            [sg.Button(button_text = "Cadastrar", font = ("Helvectica", 14)), sg.Button(button_text = "Consultar", font = ("Helvectica", 14))],
                            [sg.Text(text = "", font = ("Helvetica", 14), key = "resultado", size = (50, 1))]
                           ]
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))
        return self.__container

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
