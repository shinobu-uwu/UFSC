from imposto import Imposto


class IRPJ(Imposto):
    def __init__(self, aliquota, incidencia_imposto, desconto):
        super().__init__(aliquota, incidencia_imposto)
        self.__desconto = desconto

    def calcula_aliquota(self):
        return self.aliquota - self.__desconto