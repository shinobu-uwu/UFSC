import pickle
from empresa import Empresa
from empresa_duplicada_exception import EmpresaDuplicadaException


class EmpresaDAO:
    def __init__(self, datasource = "empresa.pkl"):
        self.__datasource = datasource
        self.__object_cache = {}
        self.__load()

    @property
    def object_cache(self):
        return self.__object_cache

    def __dump(self):
        file = open(self.__datasource, 'wb')
        pickle.dump(self.__object_cache, file)

    def __load(self):
        try:
            file = open(self.__datasource, "rb")
        except FileNotFoundError:
            self.__dump()
            self.__load()
        else:
            self.__object_cache = pickle.load(file)
        
    def add(self, empresa):
        if isinstance(empresa, Empresa):
            if empresa in self.__object_cache.values():
                raise EmpresaDuplicadaException
            else:
                self.__object_cache[empresa.cnpj] = empresa
                self.__dump()

    def get(self, cnpj):
        try:
            a = self.__object_cache[cnpj]
        except KeyError:
            a = None
        finally:
            return a

    def remove(self, empresa):
        self.__object_cache.pop(empresa.cnpj)

    def get_all(self):
        return list(self.__object_cache.values())