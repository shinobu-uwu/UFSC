from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self):
        super().__init__(3, 3)

    def mover(self):
        return super().mover()

    def produzir_som(self):
        return super().produzir_som()

    def latir(self):
        return super().produzir_som() + "SOM: AU"