from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipo_chamados = []

    def totalChamadosPorTipo(self, tipo):
        total = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                total += 1
        return total
    
    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        if isinstance(data, Date) and isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico)\
and isinstance(titulo, str) and isinstance(descricao, str) and isinstance(prioridade, int) and isinstance(tipo, TipoChamado):
            chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
            for chamados in self.__chamados:
                if chamados == chamado:
                    return
            self.__chamados.append(chamado)
            return chamado

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        tipo = TipoChamado(codigo, descricao, nome)
        for tipo_chamado in self.__tipo_chamados:
            if tipo_chamado.nome == tipo.nome:
                return
        self.__tipo_chamados.append(tipo)
        return tipo

    @property
    def tipoChamados(self):
        return self.__tipo_chamados

