from abc import ABC, abstractmethod
import pickle

class DAO(ABC):
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__cache = {}
    
    def dump(self):
        file = open(self.__datasource, "wb")
        pickle.dump(self.__cache, file)

    def load(self):
        file = open(self.__datasource, "rb")
        try:
            a = pickle.load(file)
        except pickle.io.UnsupportedOperation:
            pickle.dump(self.__cache, file)
        else:
            self.__cache = a

    @abstractmethod
    def add(self, obj):
        pass

    def get(self, key):
        return self.__cache[key]

    def remove(self, key):
        self.__cache.pop(key)

    def get_all(self):
        for key in self.__cache.keys():
            print(f"{key}, {self.__cache[key]}")

    @property
    def cache(self):
        return self.__cache

    @property
    def datasource(self):
        return self.__datasource