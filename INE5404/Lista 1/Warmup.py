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

#    def muda_canal_para_cima(self):
#        self.canal += 1

#    def muda_canal_para_baixo(self):
#        self.canal -= 1

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

    

    



# criando objetos para parte 2:

tv1 = Televisao(21, "Philips", 2)
tv2 = Televisao(24, "Toshiba", 2)
print(f"""
Tamanho televisão 1: {tv1.tamanho}
Marca televisão 1: {tv1.marca}
Tamanho televisão 2: {tv2.tamanho}
Marca televisão 2: {tv2.marca}
""")