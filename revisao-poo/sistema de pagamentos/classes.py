from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:int|float):
        self._valor = valor

    @property
    def valor(self) -> int | float:
        return self._valor

    @abstractmethod
    def pagar(self) -> None:
        pass

class Boleto(Pagamento):
    def pagar(self) -> None:
        print(f"Pagamento confirmado de R$ {self._valor:.2f} confirmado via Boleto")

class Pix(Pagamento):
    def pagar(self) -> None:
        print(f"Pagamento confirmado de R$ {self._valor:.2f} confirmado via Pix")

class Credito(Pagamento):
    def pagar(self) -> None:
        print(f"Pagamento confirmado de R$ {self._valor:.2f} confirmado via Crédito")

def finalizar_compra(obj:Pagamento) -> None:
    try:
        obj.pagar()
    except Exception as e:
        raise ValueError (f"Não consegui processar o pagamento: {e}")