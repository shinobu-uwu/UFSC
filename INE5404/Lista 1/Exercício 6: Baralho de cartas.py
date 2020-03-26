# Nesse exercício usei como modelo o jogo Yu-Gi-Oh!
# Nesse jogo cada baralho tem de 40 a 60 cartas e existem cartas de monstros, armadilhas e mágicas
# Cada jogador começa com 5 cartas e 8000 pontos de vida
# Apenas programei as interações do jogador com o baralho e os tipos de cartas, já que é o que o exercício pediu
# As interações do jogador com o baralho são apenas: Sacar ou embaralhar

from random import randrange
from copy import deepcopy



class Carta:

    def __init__(self, titulo, tipo, descricao):
        self.nome = titulo
        self.tipo = tipo
        self.descricao = descricao



class CartaMagica(Carta):
    
    pass



class CartaArmadilha(Carta):

    pass



class CartaMonstro(Carta):
    
    def __init__(self, titulo, tipo, descricao, atributo, nivel, raca):
        super().__init__(titulo, tipo, descricao)
        self.atributo = atributo
        self.nivel = nivel
        self.raca = raca
          
                    
class Jogador:

    def __init__(self, baralho : []):
        self.baralho = baralho
        self.vida = 8000
        self.mao = []
        for i in range(5):
            self.sacar()
        

    def sacar(self):
        self.mao.append(self.baralho[0])
        self.baralho.pop(0)


    def embaralhar(self):
        baralho_embaralhado = []

        for i in range(len(self.baralho)):
            n = randrange(0, len(self.baralho))
            baralho_embaralhado.append(self.baralho[n])
            self.baralho.pop(n)

        self.baralho = deepcopy(baralho_embaralhado)




dm = CartaMonstro("Mago Negro", "Monstro Normal", "O mago definitivo em termos de ataque e defesa", "Trevas", 7, "Mago")
pog = CartaMagica("Pote da ganância", "Magia Normal", "?")
bewd = CartaMonstro("Dragão branco de olhos azuis", "Monstro Normal" ,"Descrição muito grande", "Luz", 8, "Dragão")
dmg = CartaMonstro("Maga Negra", "Montrol de Efeito", "blah blah blah", "Trevas", 6, "Mago")
bd = CartaMonstro("Dragão Calibregado", "Monstrol Link", "idk idk", "Trevas", 4, "Dragão")

jogador = Jogador([dm, pog, bewd, dmg, bd])
jogador.sacar()
jogador.embaralhar()
for carta in jogador.baralho:
    print(carta.nome)
    
