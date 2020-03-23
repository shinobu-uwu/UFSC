class Televisao:

    #parte 1:

    def __init__(self, tamanho, marca):
        self.ligada = False
        self.canal = 2

    #parte 2:

        self.tamanho = tamanho
        self.marca = marca

    #parte 3:

        def muda_canal_para_cima():
            self.canal += 1

        def muda_canal_para_baixo():
            self.canal -= 1



#criando objetos para parte 2:

tv1 = Televisao(21, "Philips")
tv2 = Televisao(24, "Toshiba")
print(f"""
Tamanho televisão 1: {tv1.tamanho}
Marca televisão 1: {tv1.marca}
Tamanho televisão 2: {tv2.tamanho}
Marca televisão 2: {tv2.marca}
""")