from imposto import Imposto


class ISS(Imposto):
    def __init__(self, aliquota, incidencia_imposto):
        super().__init__(aliquota, incidencia_imposto)
        self.__servicos = []

    def inclui_servico(self, nome):
        self.__servicos.append(nome)
    
    def exclui_servico(self, nome):
        self.__servicos.remove(nome)

    def calcula_aliquota(self):
        return self.aliquota - 0.1*len(self.__servicos)