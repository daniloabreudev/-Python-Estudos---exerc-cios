class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco


    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= self.preco:
            print("Preço Inválido! Deve ser maior que o valor atual")
        else:
            self._preco = valor