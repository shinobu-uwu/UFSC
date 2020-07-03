#Nesse arquivo implementei apenas a classe necessária para criar os livros para o sistema completo no exercício 7
class Livro:


    def __init__(self, titulo, autores, ano, editora, edicao, volume, numero_paginas):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume
        self.__numero_paginas = numero_paginas
        self.sendo_lido = False
    
    @property
    def titulo(self):
        return self.__titulo

    @property
    def autores(self):
        return self.__autores

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def edicao(self):
        return self.__edicao

    @property
    def volume(self):
        return self.__volume

    @property
    def numero_paginas(self):
        return self.__numero_paginas