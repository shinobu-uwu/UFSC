class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone



class Conta:

    def __init__(self, clientes : []):
        self.titulares = clientes
        self.saldo = 0
        self.historico = list()

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque de {valor}")
        else:
            print("Saldo insuficiente")


    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(f"Depósito de {valor}")

    def get_saldo(self):
        return self.saldo

    def extrato(self):
        print("Extrato da conta: \n")
        for transacao in self.historico:
            print(transacao)
        print()

    def resumo_titulares(self):
        print("Titulares:\n")
        for cliente in self.titulares:
            print(cliente.nome + ", telefone " + cliente.telefone)
        print(f"\nSaldo de {self.saldo}")
        



class ContaCorrente(Conta):

    pass



class ContaEspecial(Conta):

    def __init__(self, clientes : [], limite):
        super().__init__(clientes)
        self.limite = limite

    def saque(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.historico.append(f"Depósito de {valor}")
        else:
            print("Saldo insuficiente")




cliente = Cliente("João", "3123")
conta = ContaCorrente([cliente])
conta.deposito(50)
conta.saque(25)
conta.extrato()
conta.resumo_titulares()