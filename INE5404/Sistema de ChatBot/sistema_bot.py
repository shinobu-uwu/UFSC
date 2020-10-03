from bot_xandao import BotXandao
from bot_triste import BotTriste
from bot_tudo import BotaTudo
from bot_xandao2 import XANDAO as BotXandao2
from bot_soneca import BotSoneca

class SistemaChatBot():
    
    def __init__(self, nome_empresa, lista_bots):
        self.__empresa = nome_empresa
        self.__lista_bots = lista_bots

    def boas_vindas(self):
        print("Olá, esse é o sistema de chatbots da empresa CrazyBots")

    def escolhe_bot(self):
        n = int(input("Digite o bot com que você deseja conversar: "))
        self.__bot = self.__lista_bots[n - 1]

    def mostra_menu(self):
        for i in range (0,len(self.__lista_bots)):
            print(i + 1,'- Bot: ', self.__lista_bots[i].nome(),'-Mensagem de Apresentação:',self.__lista_bots[i].apresentacao() + '\n')

    def mostra_comandos_bot(self):
        print (f"-->{self.__bot.nome()} diz:{self.__bot.mostra_comandos()}\n")

    def le_envia_comando(self):
        com = input("Digite o comando que gostaria de realizar:\n")
        if com == "-1":
            return com
        return self.__bot.executa_comando(str(com))

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            a = self.le_envia_comando()
            if a == "-1":
                self.__bot.despedida()
                return
            else:
                print(a)

a = SistemaChatBot("XANDAO", [BotXandao("XANDAOBOT"), BotTriste("Bot Triste :("), BotaTudo("BotaTudo"), BotXandao2("XANDAO2"), BotSoneca("SONECA")])
a.inicio()