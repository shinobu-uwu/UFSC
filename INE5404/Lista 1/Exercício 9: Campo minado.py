import keyboard

class Campo:

    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura
        

class Mina:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def explodir(self, jogador):  
        jogador.vivo = False
        print(f"Você perdeu para uma mina na posição {self.__x}, {self.__y}")

class Jogador:

    def __init__(self, campo, x, y):
        self.__x = campo.largura // 2
        self.__y = campo.altura // 2
        self.__vivo = True

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @property
    def vivo(self):
        return self.__vivo

    def andar(self, tecla):
        if keyboard.is_pressed("up"):
            self.__y += 1
        elif keyboard.is_pressed("down"):
            self.__y -= 1
        elif keyboard.is_pressed("left"):
            self.__x -= 1
        else:
            self.__x += 1