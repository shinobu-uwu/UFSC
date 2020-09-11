import datetime

class Transacao:
    
    def __init__(self, tipo, valor):
        self.__tipo = tipo
        self.__valor = valor
        self.__data = datetime.datetime.now()

    @property
    def tipo(self):
        return self.__tipo

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return self.__data     

class Cliente:

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

class ContaCorrente: #Como o banco tatu quer controlar o saldo dos seus correntistas, toda conta que criaremos será uma conta corrente

    def __init__(self, clientes): 
        self.__titular = clientes
        self.__saldo = 0
        self.__historico = list()
        self.__data_criacao = datetime.date.today()

    def saque(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            self.__historico.append(Transacao("Saque", valor))
        else:
            raise Exception("Saldo insuficiente")


    def deposito(self, valor):
        self.__saldo += valor
        self.__historico.append(Transacao("Depósito", valor))


    def extrato(self):
        print("Extrato da conta: \n")
        for transacao in self.__historico:
            print(f'{transacao.data} - {transacao.tipo} de R${str(transacao.valor)}')
        print()

    def resumo(self):
        print("Titular: \n")
        for cliente in self.__titular:
            print(f"{cliente.nome}, telefone: {cliente.telefone}")
        print(f"\nSaldo de R${self.__saldo}")
        print(f"Data de criação: {self.__data_criacao}")

class ContaEspecial(ContaCorrente):

    def __init__(self, clientes, limite): 
        super().__init__(clientes)#Herda o método, nesse caso o construtor, da classe mãe
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    def saque(self, valor):
        if self.__saldo + self.limite >= valor :
            self.__saldo -= valor
            self.__historico.append(Transacao("Saque", valor))
        else:
            raise Exception("Saldo insuficiente")

class ContaPoupança(ContaCorrente):

    def __init__(self, clientes, rendimento_inicial):
        super().__init__(clientes)
        self.__rendimento = rendimento_inicial

    @property
    def rendimento(self):
        return self.__rendimento

    @rendimento.setter
    def rendimento(self, rendimento):
        self.__rendimento = rendimento

    def deposito(self, valor):
        hoje = datetime.date.today()
        ultima_transacao = self.__historico[-1].data
        meses = (hoje.year - ultima_transacao.year) * 12 + (hoje.month - ultima_transacao.month)
        super().deposito(valor * self.rendimento * meses)