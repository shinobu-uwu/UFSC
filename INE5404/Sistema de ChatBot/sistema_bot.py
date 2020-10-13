from bot_xandao import BotXandao
from bot_triste import BotTriste
from bot_tudo import BotaTudo
from bot_xandao2 import XANDAO as BotXandao2
from bot_soneca import BotSoneca
from bot import Bot
from comando import Comando

class SistemaChatBot():
    
    def __init__(self, nome_empresa):
        self.__empresa = nome_empresa
        self.__lista_bots = []

    def adicionar_bot(self, bot):
        if isinstance(bot, Bot):
            self.__lista_bots.append(bot)

    def boas_vindas(self):
        print("Olá, esse é o sistema de chatbots da empresa CrazyBots")

    def escolhe_bot(self):
        n = int(input("Digite o bot com que você deseja conversar: "))
        try:
            self.__bot = self.__lista_bots[n - 1]
        except IndexError:
            print("Bot inexistente")
            return self.escolhe_bot()

    def mostra_menu(self):
        for i in range (0,len(self.__lista_bots)):
            print(i + 1,'- Bot: ', self.__lista_bots[i].nome(),'-Mensagem de Apresentação:',self.__lista_bots[i].apresentacao() + '\n')

    def mostra_comandos_bot(self):
        print (f"-->{self.__bot.nome()} diz:{self.__bot.mostra_comandos()}\n")

    def le_envia_comando(self):
        com = input("Digite o comando que gostaria de realizar:\n")
        if com == "-1":
            return com
        return self.__bot.executa_comando(com)
            
    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            try:
                a = self.le_envia_comando()
                assert(a is not None)
            except AssertionError as e:
                print("Comando não encontrado")
            except Exception as e:
                print(f"Erro: {e}")
                break

            if a == "-1":
                self.__bot.despedida()
                return
            else:
                print(a)


class FabricaBot:

    def criar_bot_xandao(self, nome, sistema):
        sistema.adicionar_bot(BotXandao(nome))

    def criar_bot_xandao2(self, nome, sistema):
        sistema.adicionar_bot(BotXandao2(nome))

    def criar_bot_triste(self, nome, sistema):
        sistema.adicionar_bot(BotTriste(nome))

    def criar_bot_tudo(self, nome, sistema):
        sistema.adicionar_bot(BotaTudo(nome))

    def criar_bot_soneca(self, nome, sistema):
        sistema.adicionar_bot(BotSoneca(nome))


sistema = SistemaChatBot("")
a = FabricaBot()
a.criar_bot_xandao("XANDAO", sistema)
a.criar_bot_xandao2("XANDAO", sistema)
sistema.inicio()
