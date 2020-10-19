from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]     

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autores(self):
        return self.__autores

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano    

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores and autor != None:
            self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if autor in self.__autores and autor != None:
            self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        #Como são passados o número e o título do capítulo, não precisamos fazer uma verificação de tipo, apenas criar um objeto capítulo
        capitulo = Capitulo(numeroCapitulo, tituloCapitulo)
        if capitulo not in self.__capitulos:
            self.__capitulos.append(capitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == tituloCapitulo:
                self.__capitulos.pop(self.__capitulos.index(capitulo))

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == tituloCapitulo:
                return capitulo