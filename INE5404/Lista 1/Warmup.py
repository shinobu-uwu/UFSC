import math

class Televisao:

    # parte 1:

    def __init__(self, tamanho, marca, canal):
        self.ligada = False
        self.canal = 2

    # parte 2:

        self.tamanho = tamanho
        self.marca = marca

    # parte 3:

        self.canal = canal

    # parte 4:

        self.canal_minimo = 1
        self.canal_maximo = 99



    # métodos da parte 3, comentados pois terei que mudar para parte 4:

    """def muda_canal_para_cima(self):
        self.canal += 1

    def muda_canal_para_baixo(self):
        self.canal -= 1"""

    # parte 4:

    def muda_canal_para_baixo(self):
        if(self.canal == self.canal_minimo):
            self.canal = self.canal_maximo

        else:
            self.canal += 1

    def muda_canal_para_cima(self):
        if(self.canal == self.canal_maximo):
            self.canal = self.canal_minimo

        else:
            self.canal += 1

    #parte 5:
    """
    def __init__(self, tamanho, marca, canal, canal_minimo = 2, canal_maximo = 14):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca
        self.canal = canal
    """

#parte 7:
class Estado:

    def __init__(self, nome, sigla, cidades : []):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        self.populacao = self.__populacao()

    def __populacao(self):
        resultado = 0
        for cidade in self.cidades:
            resultado += cidade.populacao
        return resultado

class Cidade:

    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

#parte 8:
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def polar(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 1/2, math.atan(self.x / self.y)

    #comparação de coordenadas, deve ser usado os operados padrão do python para comparar os objetos
    def __ge__(self, coord):
        return self.x >= coord.x and self.y >= coord.y

    def __gt__(self, coord):
        return self.x > coord.x and self.y > coord.y

    def __le__(self, coord):
        return self.x <= coord.x and self.y <= coord.y

    def __lt__(self, coord):
        return self.x < coord.x and self.y < coord.y

    def __eq__(self, coord):
        return self.x == coord.x and self.y == coord.y

#parte 9:
class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura

class Circulo:

    def __init__(self, raio):
        self.raio = raio
        self.diametro = raio * 2

    def area(self):
        return math.pi * self.raio ** 2

#parte 10:
class Fracao:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self. denominador = denominador

    #metodo para calcular o mínimo múltiplo comum para a soma e subtração de fraçoes
    def mmc(self, numero):
        if self.denominador > numero:
            maior = self.denominador
        else:
            maior = numero
        while True:
            if maior % self.denominador == 0 and maior % numero == 0:
                resultado = maior
                break
            maior += 1
        return resultado

    #magic methods para operações entre frações, devem ser usados os operadores padrões da linguage (+, -, *, /, >, >=, etc)
    def __add__(self, fracao):#soma (+)
        mmc = self.mmc(fracao.denominador)
        num = self.numerador * (mmc / self.denominador) + fracao.numerador * (mmc / fracao.denominador)
        return Fracao(num, mmc) 

    def __sub__(self, fracao):#subtração (-)
        mmc = self.mmc(fracao.denominador)
        num = self.numerador * (mmc / self.denominador) - fracao.numerador * (mmc / fracao.denominador)
        return Fracao(num, mmc)

    def __mul__(self, fracao):#multiplicação (*)
        num = self.numerador * fracao.numerador
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def __truediv__(self, fracao):#divisão (/)
        fracao = Fracao(fracao.denominador, fracao.numerador)
        return self.__mul__(fracao)        

    def __str__(self):#esse método é chamado quando damos print no objeto
        return f"{self.numerador}/{self.denominador}"

    def inverter(self):
        return Fracao(self.denominador, self.numerador)

    def valor_real(self):
        return self.numerador / self.denominador

    def transformar_fracao(self, numero):
        #usando a função as_integer_ratio ele decompõe o número em 2 inteiros e retorna em uma tupla
        num = numero.as_integer_ratio()[0]
        den = numero.as_integer_ratio()[1]
        return Fracao(num, den)

#criando objetos para parte 2:
tv1 = Televisao(21, "Philips", 2)
tv2 = Televisao(24, "Toshiba", 2)
print(f"""
Tamanho televisão 1: {tv1.tamanho}
Marca televisão 1: {tv1.marca}
Tamanho televisão 2: {tv2.tamanho}
Marca televisão 2: {tv2.marca}
""")

#objetos para parte 7:
cidade1 = Cidade("Americana", 230000)
cidade2 = Cidade("Registro", 56000)
cidade3 = Cidade("São José dos Campos", 533000)
estado1 = Estado("São Paulo", "SP", [cidade1, cidade2, cidade3])
cidade1 = Cidade("Florianópolis", 477000)
cidade2 = Cidade("Blumenau", 357000)
cidade3 = Cidade("Itajaí", 200000)
estado2 = Estado("Santa Catarina", "SC", [cidade1, cidade2, cidade3])
cidade1 = Cidade("Porto Alegre", 1400000)
cidade2 = Cidade("Caxia do Sul", 415000)
cidade3 = Cidade("Gramado", 31000)
estado3 = Estado("Rio Grando do Sul", "RS", [cidade1, cidade2, cidade3])
print(f"""
População de São Paulo: {estado1.populacao}
População de Santa Catarina: {estado2.populacao}
População de Rio Grande do Sul: {estado3.populacao}
""")
a = Fracao(1, 2)
print(a.transformar_fracao(0.25))