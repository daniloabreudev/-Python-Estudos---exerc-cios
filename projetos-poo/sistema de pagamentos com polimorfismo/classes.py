from abc import ABC,abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:int|float):
        self.valor = valor
        self.__valor = None

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def pagar(self):
        return f"Pagamento CONFIRMADO de {self.valor} no {Boleto}"


class Pix(Pagamento):
    def pagar(self):
        pass


class Credito(Pagamento):
    def pagar(self):
        pass


def finalizar_compra(objeto):
    try:
        objeto.