biblioteca = __import__("Exercício 2: Biblioteca")



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
        for livro in self.__armazenamento:
            if livro.titulo == parametro:
                resultado.append(livro.titulo)

            elif livro.autores == parametro:
                resultado.append(livro.titulo)

            elif livro.ano == parametro:
                resultado.append(livro.titulo)

            elif livro.editora == parametro:
                resultado.append(livro.titulo)

            elif livro.edicao == parametro:
                resultado.append(livro.titulo)

            elif livro.volume == parametro:
                resultado.append(livro.titulo)

            else:
                return "Nenhum livro encontrado no acervo"
        
        return resultado


    def leitura(self, usuario, livro):            
        if usuario.lendo == False and livro.sendo_lido == False:
            for i in range(livro.numero_paginas):
                #mostra a página do livro na tela
                input("Aperte ENTER para ir para próxima página")

        else:
            print("Você não pode ler esse livro no momento")