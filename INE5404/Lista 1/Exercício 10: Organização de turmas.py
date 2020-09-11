class Aluno:

    def __init__(self, nome, matricula, nota, presenca):
        self.__nome = nome
        self.__matricula = matricula
        self.__nota = nota
        self.__presenca = presenca

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def nota(self):
        return self.__nota

    @property
    def presenca(self):
        return self.__presenca

    @nota.setter
    def nota(self, valor):
        self.__nota = valor

    def __str__(self):
        return f"{self.__nome} ({self.__matricula}): Nota de {self.__nota} com {round(self.__presenca * 100, 2)}% de presença"

class Professor:

    def __init__(self, nome, registro, materias):
        self.__nome = nome
        self.__registro = registro
        self.__materias = materias

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f"Prof. {self.__nome}, registro: {self.__registro}"

class Secretario:

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha

    @property
    def nome(self):
        return self.__nome

class Turma:

    def __init__(self, materia, numero, alunos, professor, sala):
        self.__materia = materia
        self.__numero = numero
        self.__alunos = alunos
        self.__professor = professor
        self.__sala = sala
    
    @property
    def alunos(self):
        return self.__alunos

    @property
    def materia(self):
        return self.__materia

    @property
    def professor(self):
        return self.__professor

    def __str__(self):
        return f"Turma {self.__numero} de {self.__materia}. Professor: {self.__professor.nome}"
    
class Sistema:

    def __init__(self):
        self.__secretarios = []
        self.__turmas = []

    def pesquisa_secretario(self, nome):
        minimo = 0
        maximo = len(self.__secretarios)
        meio = maximo // 2
        while minimo <= maximo:
            if self.__secretarios[meio].nome == nome:
                return self.__secretarios[meio]
            elif self.__secretarios[meio].nome < nome:
                minimo = meio + 1
            else:
                maximo = meio - 1
        #se nada for retornado
        raise Exception("Secretário não encontrado")

    def criar_secretario(self, nome, senha):
        secretario = Secretario(nome, senha)
        for i in range(len(self.__secretarios)):
            if secretario.nome < self.__secretarios[i].materia:
                self.__secretarios.insert(i, secretario)
                return
        self.__secretarios.append(secretario)


    def criar_turma(self, materia, numero, alunos, professor, sala):
        turma = Turma(materia, numero, alunos, professor, sala)
        for i in range(len(self.__turmas)):
            if turma.materia < self.__turmas[i].materia:
                self.__turmas.insert(i, turma)
                return
        self.__secretarios.append(turma)


    def listar_alunos(self):
        usuario = input("Digite seu login: ")
        usuario = self.pesquisa_secretario(usuario)
        senha = input("Digite sua senha: ")
        if senha != usuario.senha:
            raise Exception("Senha incorreta")
        for i in range(len(self.__turmas)):
            print(f"{i + 1}. {self.__turmas[i]}")
        escolha = int(input("Escolha uma turma: "))
        turma = self.__turmas[escolha - 1]
        for aluno in turma.alunos:
            print(aluno)

    def professores_disciplina(self, disciplina):
        resultado = []
        for turma in self.__turmas:
            if turma.materia == disciplina:
                resultado.append(turma)
        print(f"Professores da matéria: {disciplina}")
        for turma in resultado:
            print(turma.professor)