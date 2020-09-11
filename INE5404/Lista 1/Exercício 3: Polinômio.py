from numpy import linspace
import matplotlib.pyplot as mpl

class Polinomio:

    def __init__(self, coeficientes):
        self.__coeficientes = coeficientes
        self.__grau = len(self.__coeficientes) - 1  

    @property
    def coeficientes(self):
        return self.__coeficientes

    @property
    def grau(self):
        return self.__grau

    #para um método vou precisar fazer uma cópia profunda para não modificar o polinômio inicial
    #então criei um método privado para isso
    def __copia(self, lista):
        resultado = []
        for item in lista:
            resultado.append(item)
        return resultado

    def avaliar(self, x):
        resultado = self.__coeficientes[0]
        for i in range(1, len(self.__coeficientes)):
            resultado += self.__coeficientes[i] * x ** i
        return resultado

    def __add__(self, polinomio):
        resultado = list()
        if self.__grau > polinomio.grau:
            resultado = self.__copia(self.__coeficientes)
            for i in range(len(polinomio.coeficientes)):
                resultado[i] += polinomio.coeficientes[i]
        else:
            resultado = self.__copia(polinomio.coeficientes)
            for i in range(len(self.__coeficientes)):
                resultado[i] += self.__coeficientes[i]
        return Polinomio(resultado)

    def __mul__(self, polinomio):
        resultado = [0] * (self.grau + polinomio.grau + 1)
        for i in range(len(self.__coeficientes)):
            for j in range(len(polinomio.coeficientes)):
                resultado[i + j] += self.__coeficientes[i] * polinomio.coeficientes[j] 
        return Polinomio(resultado)

    #Para o método funcionar é necessário ter o tkinter, numpy e matplotlib instalado
    def plot(self, a, b): #Desafio de plotar o polinômio no intervalo [a,b]
        x = linspace(a, b, 500)
        y = self.__coeficientes[0]
        for i in range(1, len(self.__coeficientes)):
            y += self.__coeficientes[i] * x ** i    
        mpl.axvline()
        mpl.axhline()
        mpl.plot(x, y)
        mpl.grid()
        mpl.show()

a = Polinomio([1, 2, 4, 7])
b = Polinomio([4, 1, 0, 3, 8])
print(a.avaliar(4))
print(b.avaliar(7))
print((a + b).coeficientes)
print((a * b).coeficientes)
b.plot(-100, 100)