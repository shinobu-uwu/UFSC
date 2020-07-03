from copy import deepcopy
import numpy as np
import matplotlib.pyplot as mpl

class Polinomio:

    def __init__(self, coeficientes):
        self.__coeficientes = coeficientes
        self.__grau = len(self.coeficientes) - 1  

    @property
    def coeficientes(self):
        return self.__coeficientes

    @property
    def grau(self):
        return self.__grau

    def avaliar(self, x):
        resultado = self.coeficientes[0]
        for i in range(1, len(self.coeficientes)):
            resultado += self.coeficientes[i] * x ** i
        return resultado

    def soma(self, polinomio):
        resultado = list()
        if self.__grau > polinomio.grau:
            resultado = deepcopy(self.coeficientes)
            for i in range(len(polinomio.coeficientes)):
                resultado[i] += polinomio.coeficientes[i]
        else:
            resultado = deepcopy(polinomio.coeficientes)
            for i in range(len(self.coeficientes)):
                resultado[i] += self.coeficientes[i]
        return resultado

    def multiplicacao(self, polinomio):
        resultado = [0] * (self.grau() + polinomio.grau() + 1)
        for i in range(len(self.coeficientes)):
            for j in range(len(polinomio.coeficientes)):
                resultado[i + j] += self.coeficientes[i] * polinomio.coeficientes[j] 
        return resultado

    #Para o método funcionar é necessário ter o tkinter instalado
    def plot(self, a, b): #Desafio de plotar o polinômio no intervalo [a,b]
        x = np.linspace(a, b, 100)
        y = self.coeficientes[0]
        for i in range(1, len(self.coeficientes)):
            y += self.coeficientes[i] * x ** i    
        mpl.axvline()
        mpl.axhline()
        mpl.plot(x, y)
        mpl.grid()
        mpl.show()