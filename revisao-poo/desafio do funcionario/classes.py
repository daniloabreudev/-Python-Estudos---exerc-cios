from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        if salario > self._salario:
            self._salario = salario
        else:
            raise ValueError (f"Você não pode diminuir o salário !")

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self) -> str:
        return (
            f"{self.nome} ganha R$ {self.salario:.2f} e por ser {self.__class__.__name__} o bônus será de R$ {self.calcular_bonus():.2f}"
        )

#bônus 20%
class Gerente(Funcionario):

    def calcular_bonus(self):
        return (self.salario * 20) / 100

#bônus de 12 %
class Designer(Funcionario):

    def calcular_bonus(self):
        return (self.salario * 12) / 100


#bônus de 15%
class Desenvolvedor(Funcionario):

    def calcular_bonus(self):
        return (self.salario * 15) / 100

