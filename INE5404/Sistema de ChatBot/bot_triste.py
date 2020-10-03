from bot import Bot
import random as r

class BotTriste(Bot):
    def __init__(self,nome):
        self.__nome = nome

    def nome(self):
        return self.__nome

    def apresentacao(self):
        return f'Eu sou o {self.__nome}'
 
    def mostra_comandos(self):
        return 'Comandos: \n1 - apresentacao() \n2 - boas_vindas() \n3 - despedida() \n4 - conselho()'

    def executa_comando(self,cmd):
        if cmd == '1':
            return self.apresentacao()
        elif cmd == '2':
            return self.boas_vindas()
        elif cmd == '3':
            return self.despedida()
        elif cmd == '4':
            return self.conselho()
        else:
            return 'Comando inválido.'

    def boas_vindas(self):
        return 'Olá...Como posso te atrapalhar? Whoops, ajudar?'

    def despedida(self):
        return f'Já vai embora? Sniff...'

    def conselho(self):
        conselhos = ['Vai dormir!', 'Larga esse curso!', 'Quem não tenta não fracassa!', 'Tururu ♬', 'Chore!']
        return r.choice(conselhos)