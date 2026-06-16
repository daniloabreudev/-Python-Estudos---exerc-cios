from uteis import traco
from rich import print
class ContaBancaria:
    """Cria uma conta bancária e permite fazer saques e depósitos"""

    def __init__(self,id,nome = 'Desconhecido',saldo = 0):
        self.id = id #publico (+)
        self._titular = nome #protegido (#)
        self.__saldo = saldo #privado (-)
        print(f"[green]Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")


    def __str__(self):
        # return f":book: [yellow]A conta {self.id}, do _titular, {self._titular} tem __saldo {self.__saldo:.2f}"
        return f"Estado atual da conta: {self.__dict__}"

    def depositar (self,valor):
        self.__saldo += valor
        traco()
        print(f"[blue]Depósito de {valor} autorizado na conta {self.id}")
        print(f":money_with_wings: Novo __saldo de : {self.__saldo}")
        traco()


    def sacar (self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            traco()
            print(f"[red]Saque de {valor} autorizado na conta {self.id}")
            print(f":money_with_wings: Novo __saldo de : {self.__saldo}")
            traco()
        else:
            traco()
            print(f":money_with_wings: Saldo não disponível:")
            print(f"Você tentou sacar {valor},mais seu __saldo é de {self.__saldo}.\nSaindo!")
            traco()





