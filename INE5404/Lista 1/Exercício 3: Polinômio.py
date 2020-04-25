from copy import deepcopy



class Polinomio:



    def __init__(self, coeficientes):
        self.coeficientes = coeficientes


    
    def grau(self):
        return len(self.coeficientes) - 1

    

    def avaliar(self, x):
        resultado = self.coeficientes[0]

        for i in range(1, len(self.coeficientes)):
            resultado += self.coeficientes[i] * x ** i

        return resultado



    def soma(self, polinomio):
        resultado = list()

        if len(self.coeficientes) > len(polinomio.coeficientes):
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