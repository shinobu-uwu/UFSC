from random import randrange

class Jogador:

    def __init__(self, vidas):
        self.__vidas = vidas

    def adivinhar(self, jogo, tentativa):
        certo = False
        for i in range(len(jogo.letras)):
            if tentativa.lower() == jogo.letras[i].lower():
                certo = True
                jogo.segredo[i] = jogo.letras[i]
        if certo == False:
            self.vidas -= 1
        
    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, valor):
        self.__vidas = valor

class Jogo:

    def __init__(self, palavra):
        self.__palavra = palavra
        self.__letras = []
        for letra in palavra:
            self.__letras.append(letra)
        self.__segredo = [" _"] * len(palavra)

    @property
    def letras(self):
        return self.__letras

    @property
    def segredo(self):
        return self.__segredo

    def jogar(self, jogador):
        print()
        while jogador.vidas > 0:
            for char in self.__segredo:
                print(char, end = '')
            print()
            if " _" not in self.__segredo:
                print("Você ganhou!")
                break
            tentativa = input("Qual letra você gostaria de adivinhar? \n")
            jogador.adivinhar(self, tentativa)
        if jogador.vidas == 0:
            print("Você perdeu!")

palavras = ["Computador", "Abacaxi", "Problema", "Pirulito", "Pedra"]
jogador = Jogador(5)
n = randrange(0, len(palavras))
jogo = Jogo(palavras[n])
jogo.jogar(jogador)
