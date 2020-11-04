from imposto import Imposto


class IPI(Imposto):
    def __init__(self, aliquota, incidencia_imposto, aliquota_adicional):
        super().__init__(aliquota, incidencia_imposto)
        self.__aliquota_adicional = aliquota_adicional

    def calcula_aliquota(self):
        return self.aliquota + self.__aliquota_adicional*0.1*self.aliquota