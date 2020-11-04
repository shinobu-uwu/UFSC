from empresa_dao import EmpresaDAO
from empresa import Empresa
from empresa_duplicada_exception import EmpresaDuplicadaException


class ControladorSistemaEmpresas:
    def __init__(self):
        self.__empresa_dao = EmpresaDAO()

    def inclui_empresa(self, empresa):
        if isinstance(empresa, Empresa):
            self.__empresa_dao.add(empresa)

    def exclui_empresa(self, empresa):
        self.__empresa_dao.remove(empresa)

    def busca_empresa_pelo_cnpj(self, cnpj):
        return self.__empresa_dao.get(int(cnpj))
    
    @property
    def empresas(self):
        return self.__empresa_dao.get_all()

    def calcula_total_impostos(self):
        empresas = self.__empresa_dao.get_all()
        resultado = 0
        for empresa in empresas:
            resultado += empresa.total_impostos()
        return resultado