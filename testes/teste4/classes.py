from abc import ABC
from datetime import datetime
ano_atual = datetime.now().year


class Veiculo(ABC):
    def __init__(self, marca: str, ano: int):
        self._ano = 0
        self.ano = ano
        self.marca = marca

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        if 1900  <= ano <= ano_atual+1:
            self._ano = ano
        else:
            raise ValueError ("O ano está inválido")

class Carro(Veiculo):
    def __init__(self,marca: str, ano: int, portas: int):
        super().__init__(marca, ano)
        self.portas = portas

    def __str__(self):
        return f"Marca: {self.marca}\nano: {self.ano}\nportas: {self.portas}"




