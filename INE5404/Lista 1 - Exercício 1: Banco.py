class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:

    def __init__(self, clientes : []):
        self.titulares = clientes
        self.saldo = 0

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


    def deposito(self, valor):
        self.saldo += valor

    def get_saldo(self):
        return self.saldo

class ContaCorrente(Conta):

    pass

class ContaEspecial(Conta):

    def __init__(self, clientes : [], limite):
        super().__init__(clientes)
        self.limite = limite

    def saque(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")




cliente = Cliente("João", "3123")
conta = ContaCorrente([cliente])
conta.deposito(50)
conta.saque(20)
print(conta.get_saldo())

conta = ContaEspecial([cliente], 50)
conta.deposito(50)
conta.saque(75)
print(conta.get_saldo())