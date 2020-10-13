import random
from bot import Bot

class Comando:
    def __init__(self, id, mensagem, respostas=None):
        if respostas is None:
            respostas = []
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__mensagem

    @property
    def respostas(self):
        return self.__respostas

    def get_resposta_random(self):
        if not self.respostas:
            return 'Nenhuma resposta encontrada'
        else:
            x = random.choice(self.respostas)
            return x

    def add_resposta(self, resposta):
        if isinstance(resposta, str):
            if resposta in self.respostas:
                return 'Resposta já inclusa na lista'
            else:
                self.respostas.append(resposta)
        else:
            return 'Resposta recebida não é string'

    def del_resposta(self, resposta): 
        if isinstance(resposta, str):
            if resposta not in self.respostas:
                return 'Nenhuma resposta encontrada'
            else:
                self.respostas.remove(resposta)
        else:
            return 'Resposta recebida não é string'


class XANDAO(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []
        self.__id = 1

    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def apresentacao(self):
        x = 'SEM PRESSÃO, AQUI É XANDÃO!'
        return x

    def mostra_comandos(self):
        x = ''
        for i in self.comandos:
            x += 'Comandos: ' + 'Id: ' + str(i.id) + 'Mensagem:' + i.mensagem + 'Respostas: ' + i.resposta
        return x

    def cria_comandos(self, mensagem, respostas):
        if isinstance(mensagem, str):
            self.comandos.append(Comando(self.id, mensagem, respostas))
            self.id += 1
        else:
            return 'Tipo recebido inválido'
    
    def despedida(self):
        return 'Nao se preocupe que no fim da escuridao sempre havera Xandao'

    def executa_comando(self, id):
        for i in self.comandos:
            if i.id == id:
                i.get_resposta_random()

    def boas_vindas(self):
      boas_vindas = ['TOMA ESSE DOUBLE BICEPES AQUI', 'CAPSLOCK LIGADO, SINAL DE PERSONALIDADE FORTE',
                      'VAMOS TRILHAR O CAMINHO DOS CAMPEOES']
      x = random.choice(boas_vindas)
      return x     