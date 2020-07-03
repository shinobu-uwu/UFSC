biblioteca = __import__("Exercício 2: Biblioteca")#Usar a class já feita para os livros


class Usuario:

    id_estatico = 1000 #atributo estático para o id

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        self.__id = Usuario.id_estatico
        self.lendo = False
        Usuario.id_estatico += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

    @property
    def id(self):
        return self.__id    

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha


class Sistema:

    def __init__(self):
        self.__armazenamento = []
        self.__usuarios = []
    
    def criar_usuario(self, nome, senha):
        usuario = Usuario(nome, senha)
        self.__usuarios.append(usuario)

    def listar_usuarios(self):
        resultado = []
        for usuario in self.__usuarios:
            resultado.append(usuario.nome)
        return resultado

    def inserir_livro(self, livro):
        self.__armazenamento.append(livro)

    def pesquisa(self, parametro):
        resultado = []
        parametro = parametro.lower()
        for livro in self.__armazenamento:
            if parametro in livro.titulo.lower():
                resultado.append(livro)
            elif parametro in livro.ano.lower():
                resultado.append(livro)
            elif parametro in livro.editora.lower():
                resultado.append(livro)
            elif parametro in livro.edicao.lower():
                resultado.append(livro)
            elif parametro in livro.volume.lower():
                resultado.append(livro)
            else:
                return "Nenhum livro encontrado no acervo"
        return resultado


    def leitura(self, usuario):
        procura = input("Digite o nome do livro que você deseja ler: \n")
        livros = self.pesquisa(procura)
        for i in range(len(livros)):
            print(f"{i + 1} - {livros[i].titulo}")
        escolha = int(input("Digite o número do livro que você deseja: \n"))
        livro = livros[escolha - 1]
        if usuario.lendo == False and livro.sendo_lido == False:
            usuario.lendo = True
            livro.sendo_lido = True
            for i in range(int(livro.numero_paginas)):
                #Mostra a página do livro na tela
                input("Aperte ENTER para ir para próxima página")
            #Quando o loop acabar:
            usuario.lendo = False
            livro.sendo_lido = False
        else:
            print("Você não pode ler esse livro no momento")