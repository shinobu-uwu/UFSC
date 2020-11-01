from empresa_dao import EmpresaDao
from empresa import Empresa
from empresa_duplicada_exception import EmpresaDuplicadaException

class ControladorSistemaEmpresas:
    def __init__(self):
        self.__empresa_dao = EmpresaDao()

    def inclui_empresa(self, empresa):
        if isinstance(empresa, Empresa):
            self.__empresa_dao.add(empresa)
            self.__empresa_dao.dump()

    def exclui_empresa(self, empresa):
        self.__empresa_dao.remove(empresa)
        self.__empresa_dao.dump()

    def busca_empresa_pelo_cnpj(self, cnpj):
        return self.__empresa_dao.get(int(cnpj))
    
    def empresas(self):
        return self.__empresa_dao.get_all()

    def calcula_total_impostos(self):
        empresas = self.__empresa_dao.get_all()
        resultado = 0
        for empresa in empresas:
            resultado += empresa.total_impostos()