from bot import Bot
import random

class BotaTudo(Bot):
    def __init__(self, nome):
        self.__nome = nome

    def nome(self):
      return f'{self.__nome}, o BotaTudo.'
      #return self.__nome

    def apresentacao(self):
      return 'Eu sou o bot BotaTudo. BotaTudo.'

    def mostra_comandos(self):
      print('Pedir ajuda ao BotaTudo\nDigite 0 para sair:')
      print('1 - Apresentação')
      print('2 - Reclamar do dia')
      print('3 - Reclamar da aula')
      print('4 - Xau')
      print('0 - Sair') 

    def executa_comando(self,cmd):
      if cmd=="1":
        return self.apresentacao()
      elif cmd=="2":
        return self.reclamar_dia()
      elif cmd=="3":
        return self.reclamar_aula()
      elif cmd=="4":
        return self.despedida()
      else:
        return 'Tu é burro ou oq'

    def reclamar_dia(self):
      frases = ['Esse dia tá tão chato que parece EAD', 'Meu dia estava indo bem, até você chegar', 'Reclamar não resolve nada, mas não quero resolver, eu quero reclamar', 'Meu dia tá tão ruim que parece um jogo do Palmeiras']
      choice = random.randint(0, len(frases) - 1)
      return frases[choice]  

    def reclamar_aula(self):
      frases = ['Isso não vai acabar hoje não?', 'Esse professor não para de falar?', '2 doutorados na Europa mas não tem didática, enfim a hipocrisia', 'Mais valia ter ido ver o filme do Pelé', 'Tô com fome', 'Quero ir embora', 'Mãe, vem me buscar', 'Alguém sabe se ainda pode trancar essa disciplina?', 'Dá pra trocar pra outra turma?']
      choice = random.randint(0,len(frases) - 1)
      return frases[choice]
    
    def boas_vindas(self):
      frases = ['Veio fazer o que aqui? não tem mais nada pra fazer?', 'Tá sobrando tempo que veio brincar com bot?', 'Não tem nada melhor pra fazer que me incomodar?', 'Quem te chamou aqui?', 'Ninguém te convidou', 'Bom dia pra quem?', 'Que tu quer?', 'Chatão hem, todo dia isso']
      choice = random.randint(0,len(frases) - 1)
      return frases[choice]

    def despedida(self):
      frases = ['Já vai tarde.', 'tchau.']
      return random.choice(frases)