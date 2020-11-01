from imposto import Imposto

class Empresa:
    def __init__(self, nome_de_fantasia, cnpj):
        self.__cnpj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos = 0.0
        self.__faturamento_producao = 0.0
        self.__faturamento_vendas = 0.0 

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def nome_de_fantasia(self):
        return self.__nome_de_fantasia

    @nome_de_fantasia.setter
    def nome_de_fantasia(self, nome_de_fantasia):
        self.__nome_de_fantasia = nome_de_fantasia

    @property
    def impostos(self):
        return self.__impostos

    def inclui_imposto(self, imposto):
        if isinstance(imposto, Imposto):
            self.__impostos.append(imposto)

    def remove_imposto(self, imposto):
        self.__impostos.remove(imposto)

    @property
    def faturamento_servicos(self):
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self):
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self):
        return self.__faturamento_vendas

    def faturamento_total(self):
        return self.__faturamento_producao + self.__faturamento_servicos + self.__faturamento_vendas

    def total_impostos(self):
        resultado = 0
        for imposto  in self.__impostos:
            if imposto.incidencia_imposto.PRODUCAO:
                resultado += self.__faturamento_producao * imposto.calcula_aliquota()
            elif imposto.incidencia_imposto.SERVICOS:
                resultado += self.__faturamento_servicos * imposto.calcula_aliquota()
            elif imposto.incidencia_imposto.VENDAS:
                resutlado += self.__faturamento_vendas * imposto.calcula_aliquota()
            else:
                resultado += self.faturamento_total() * imposto.calcula_aliquota()
        return resultado

    def set_faturamentos(self, fat_servicos, fat_producao, fat_vendas):
        self.__faturamento_servicos = fat_servicos
        self.__faturamento_producao = fat_producao
        self.__faturamento_vendas = fat_vendas