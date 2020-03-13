from random import randint, shuffle



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
        


class Baralho:
    
    def __init__(self, cartas):
        self.cartas = cartas
        
        
        
    def embaralhar(self):
        shuffle(self.cartas)           
                    
    
    
    def sacar(self):
        self.cartas.pop(0)



dm = CartaMonstro("Mago Negro", "Monstro Normal", "O mago definitivo em termos de ataque e defesa", "Trevas", 7, "Mago")
pog = CartaMagica("Pote da ganância", "Magia Normal", "?")
bewd = CartaMonstro("Dragão branco de olhos azuis", "Monstro Normal" ,"Descrição muito grande", "Luz", 8, "Dragão")

deck = Baralho([dm, pog, bewd])
deck.embaralhar()
deck.sacar()
for i in range(len(deck.cartas)):
    print(deck.cartas[i].nome)
    
