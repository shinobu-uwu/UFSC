class Livro:


    def __init__(self, titulo, autores, ano, editora, edicao, volume):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume

    
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
