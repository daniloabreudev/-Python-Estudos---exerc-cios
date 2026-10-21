class Produto:
    def __init__(self, nome: str, preco:int|float):
        self.nome = nome
        self._preco = 0.0
        self.preco = preco


    @property
    def preco(self):
        return f"R$ {self._preco:.2f}"

    @preco.setter
    def preco(self, valor):
        if valor is None or valor <=0 :
            print("O valor está iválido")
        else:
            self._preco = valor


    def __str__(self):
        divisor = "-" *15
        return f"{divisor}\n{self.nome} ({self.preco})\n{divisor}"