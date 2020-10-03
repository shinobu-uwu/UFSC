from bot import Bot
import random

class XANDAO(Bot):
    def __init__(self,nome):
        self.__nome = nome
    
    def nome(self):
        x = 'AQUI É XANDÃO, O ÚLTIMO HERÓI DA TERRA!'
        return x

    def apresentacao(self):
        x = 'SEM PRESSÃO, AQUI É XANDÃO!'
        return x

    def boas_vindas(self):
      boas_vindas = ['TOMA ESSE DOUBLE BICEPES AQUI', 'CAPSLOCK LIGADO, SINAL DE PERSONALIDADE FORTE', 'VAMOS TRILHAR O CAMINHO DOS CAMPEOES' ]
      x = random.choice(boas_vindas)
      return x

    def despedida(self):
      despedida = ['Nao se preocupe que no fim da escuridao sempre havera Xandao', 'XANDAO FOREVER']
      x = random.choice(despedida)
      return x


    def mostrar_conselhos(self):
      conselhos = ['Nao tenha medo da escuridao, pois no fim havera XANDAO','O apocalipse so vao acontecer para os perdedores','Se capotar so segura no braço do XANDAO que ninguem morre',
'Vem com o XANDAO exalando energia','Trilhando o caminho dos campeoes que no fim tem XANDAO']
      x = random.choice(conselhos)
      return x

    def mostra_comandos(self):
        return 'Lista de Comandos:\n1 - Bom Dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n 4 - Despedida'

    def executa_comando(self, cmd):
        if cmd == "1":
          return self.boas_vindas()
        if cmd == "2":
          return self.nome()
        if cmd == "3":
          return self.mostrar_conselhos()
        if cmd == "4":
          return self.despedida()