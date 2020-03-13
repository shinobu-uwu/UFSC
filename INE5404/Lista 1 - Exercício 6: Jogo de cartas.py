from random import randint



class Carta:

    def __init__(self, titulo, tipo, descricao):
        self.nome = titulo
        self.tipo = tipo
        self.descricao = descricao



class CartaMagica(Carta):
    
    pass

class CartaArmadilha(Carta):

    pass
 

pog = CartaMagica("Pote da ganância", "Magia Normal", "?")

print(pog.nome, pog.descricao)