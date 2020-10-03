from bot import Bot

class BotSoneca(Bot):
	def __init__(self,nome):
		self.__nome = nome

	def nome(self):
		return self.__nome

	def apresentacao(self):
		return 'zzzzzz...Oi...Meu nome é...Soneca.'

	def mostra_comandos(self):
		return '\n'.join(('1 - Quantos anos você tem?',
							  			'2 - Abra a minha caixa de email',
							  			'3 - Qual é o rank atual do brasileirão?',
							  			'4 - Quais são os filmes em cartaz?'))
	
	def executa_comando(self,cmd):
		if   cmd == '1': return 'Deixa eu ver...Eu deitei pela primeira vez em 87...'
		elif cmd == '2': return '*Yaaaawn* mó preguiça, depois eu faço.'
		elif cmd == '3': return 'A última vez que eu vi o Sport tava em primeiro...'
		elif cmd == '4': return '*Yawn* Império do Sol. Aquele lá com aquele garotinho novo... Christian Bale? Esse ai vai ter futuro, tô dizendo...zzzz'

	def boas_vindas(self):
		return 'zzzzzz'

	def despedida(self):
		return 'zzzzzz'