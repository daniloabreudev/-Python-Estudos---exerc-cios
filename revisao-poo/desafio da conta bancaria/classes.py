class ContaBancaria:
    def __init__(self, id:int, nome:str,saldo:float):
        self._id  = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = None
        self.nome = nome


    def validar_senha(self, chave:str):
        pass


    def pede_senha(self):
        pass

    def sacar (self, valor:float, chave:str):
        pass

    def depositar(self, valor:float):
        pass
