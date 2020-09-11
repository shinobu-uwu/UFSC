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
        self.__sendo_lido = False

    @property
    def titulo(self):
        return self.__titulo

    @property
    def sendo_lido(self):
        return self.__sendo_lido

    @property
    def numero_paginas(self):
        return self.__numero_paginas

    @sendo_lido.setter
    def sendo_lido(self, x):
        self.__sendo_lido = x

    #Magic methods para comparação entre livros
    def __ge__(self, livro):
        return self.__titulo >= livro.titulo

    def __le__(self, livro):
        return self.__titulo <= livro.titulo

    def __gt__(self, livro):
        return self.__titulo > livro.titulo

    def __lt__(self, livro):
        return self.__titulo < livro.titulo 

    def __eq__(self, livro):
        return livro.titulo == self.__titulo