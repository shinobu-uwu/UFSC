ex2 = __import__("Exercício 2: Biblioteca")#Usar a class já feita para os livros

class Usuario:

    id_estatico = 1000

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        self.__id = Usuario.id_estatico
        self.__lendo = False
        Usuario.id_estatico += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def lendo(self):
        return self.__lendo

    @property
    def senha(self):
        return self.__senha

    #Magic methods para comparação entre usários
    def __ge__(self, usuario):
        return self.__nome >= usuario.nome

    def __le__(self, usuario):
        return self.__nome <= usuario.nome

    def __gt__(self, usuario):
        return self.__nome > usuario.nome

    def __lt__(self, usuario):
        return self.__nome < usuario.nome 

    def __eq__(self, usuario):
        return usuario.nome == self.__nome

class Biblioteca:

    def __init__(self):
        self.__livros = []
        self.__usuarios = []
    
    def inserir_usuario(self, usuario):
        for i in range(len(self.__usuarios)):
            if usuario < self.__usuarios[i]:
                self.__usuarios.insert(i, usuario)
                return
        #se não tiver nenhum elemento menor que o livro, ele é adicionado em último
        self.__usuarios.append(usuario)

    def listar_usuarios(self):
        resultado = []
        for usuario in self.__usuarios:
            resultado.append(usuario.nome)
        return resultado

    #Como queremos uma lista ordenada para fazer busca binária mais para frente, temos que 
    #adicionar os elementos ordenados
    def inserir_livro(self, livro):
        for i in range(len(self.__livros)):
            if livro < self.__livros[i]:
                self.__livros.insert(i, livro)
                return
        #se não tiver nenhum elemento menor que o livro, ele é adicionado em último
        self.__livros.append(livro)

    def pesquisa_livro(self, titulo):
        #como ordenamos os livros sempre que inserimos um novo podemos pesquisar usando busca binária
        minimo = 0
        maximo = len(self.__livros) - 1
        meio = maximo // 2
        while minimo <= maximo:
            if self.__livros[meio].titulo == titulo:
                return self.__livros[meio]
            #ignoramos a primeira metade da lista
            elif self.__livros[meio].titulo < titulo:
                minimo = meio + 1
            #ignoramos a segunda metade da lista
            else:
                maximo = meio - 1
        #Caso nada seja retornado
        raise Exception("Nenhum livro encontrado")

    def pesquisa_usuario(self, login):
        minimo = 0
        maximo = len(self.__usuarios) - 1
        meio  = maximo // 2
        while minimo <= maximo:
            if self.__usuarios[meio].nome == login:
                return self.__usuarios[meio]
            elif self.__usuarios[meio].nome < login:
                minimo += 1
            else:
                minimo -= 1
        raise Exception("Nenhum usuário encontrado")

    def leitura(self):
        pesquisa = input("Digite o seu nome de usuário: \n")
        usuario = self.pesquisa_usuario(pesquisa)
        senha = str(input("Digite a sua senha: \n"))
        if senha != usuario.senha:
            raise Exception("Senha incorreta")
        pesquisa = input("Digite o nome do livro que você deseja ler: \n")
        livro = self.pesquisa_livro(pesquisa)
        if usuario.lendo == False and livro.sendo_lido == False:
            usuario.lendo = True
            livro.sendo_lido = True
            for i in range(int(livro.numero_paginas)):
                #Mostra a página do livro na tela
                input("Aperte ENTER para ir para próxima página")
            #Quando o loop acabar o estado do usuário volta ao original
            usuario.lendo = False
            livro.sendo_lido = False
        else:
            raise Exception("Você não pode ler esse livro no momento")