import datetime


class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class ContaCorrente: #Como o banco tatu quer controlar o saldo dos seus correntistas, toda conta que criaremos será uma conta corrente

    def __init__(self, clientes): #Os clientes serão dados em uma lista 
        self.titular = clientes
        self.saldo = 0
        self.historico = list()
        self.data_criacao = str(datetime.date.today())

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append({"Data" : datetime.datetime.now(), "Operação" : "Saque", "Valor" : valor})
        else:
            print("Saldo insuficiente")


    def deposito(self, valor):
        self.saldo += valor
        self.historico.append({"Data" : datetime.datetime.now(), "Operação" : "Depósito", "Valor" : valor})


    def extrato(self):
        print("Extrato da conta: \n")
        for transacao in self.historico:
            print(f'{transacao["Data"]} - {transacao["Operação"]} de R${transacao["Valor"]}')
        print()

    def resumo(self):
        print("Titular: \n")
        for cliente in self.titular:
            print(f"{cliente.nome}, telefone: {cliente.telefone}")
        print(f"\nSaldo de R${self.saldo}")
        print(f"Data de criação: {self.data_criacao[8:10]}/{self.data_criacao[5:7]}/{self.data_criacao[0:4]}")


class ContaEspecial(ContaCorrente):

    def __init__(self, clientes, limite): 
        super().__init__(clientes)#Herda o construtor da classe mãe
        self.limite = limite
    
    def saque(self, valor):
        if self.saldo + self.limite >= valor :
            self.saldo -= valor
            self.historico.append({"Data" : datetime.datetime.now(), "Operação" : "Saque", "Valor" : valor})
        else:
            print("Saldo insuficiente")

class ContaPoupança(ContaCorrente):

    def __init__(self, clientes, rendimento):
        super().__init__(clientes)
        self.rendimento = rendimento

    def deposito(self, valor):
        hoje = datetime.date.today()
        ultima_transacao = self.historico[-1]["Data"]
        meses = (hoje.year - ultima_transacao.year) * 12 + (hoje.month - ultima_transacao.month)
        super().deposito(valor * self.rendimento * meses)