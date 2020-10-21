from DAO import DAO
from Cliente import Cliente
import pickle

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__("clientes.pkl")
        try:
            self.load()
        except FileNotFoundError:
            self.dump()
        finally:
            self.load()

    def add(self, cliente):
        self.cache[cliente.codigo] = cliente

    def get(self, cod):
        try:
            return super().get(cod)
        except KeyError:
            raise KeyError
        except LookupError:
            raise LookupError

    def remove(self, cod):
        super().remove(cod)