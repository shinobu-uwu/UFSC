class Serie:

    def fibonacci(self, elemento):
        if elemento == 0:
            return 0
        elif elemento == 1:
            return 1       
        else:
            return self.fibonacci(elemento - 1) + self.fibonacci(elemento - 2)

    def fatorial(self, elemento):
        if elemento == 0:
            return 1
        return elemento * self.fatorial(elemento - 1)

    #Esse método retorna todos os números primos em um dado intervalo
    def primo(self, intervalo):
        resultado = []
        comeco = intervalo[0]
        fim = intervalo[1] + 1
        for i in range(comeco, fim):
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                resultado.append(i)
        return resultado

a = Serie()
print(a.fibonacci(8))
print(a.fatorial(10))
print(a.primo([0, 200]))