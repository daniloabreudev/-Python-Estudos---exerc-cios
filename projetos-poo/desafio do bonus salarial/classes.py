from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str = '',salario :float|int = 0 ):
        self.nome = nome
        self._salario = salario
        self.bonus = 0

    @abstractmethod
    def calcular_bonus(self):
        pass


class Gerente(Funcionario):

    def __str__(self):
        return f"{self.nome} ganha R${self._salario} e por ser {self.__class__.__name__} o bônus será de R${self.bonus:.2f}"

    def calcular_bonus(self):  # Bonus de 12%
        self.bonus = 15 * self._salario / 100

class Designer(Funcionario):

    def __str__(self):
        return f"{self.nome} ganha R${self._salario} e por ser {self.__class__.__name__} o bônus será de R${self.bonus:.2f}"

    def calcular_bonus(self):  # Bonus de 12%
        self.bonus = 10 * self._salario / 100

class Desenvolvedor(Funcionario):

    def __str__(self):
        return f"{self.nome} ganha R${self._salario} e por ser {self.__class__.__name__} o bônus será de R${self.bonus:.2f}"

    def calcular_bonus(self): #Bonus de 12%
        self.bonus = 12 * self._salario / 100


def fazer_calculo(objeto):
    try:
        objeto.calcular_bonus()
    except:
        print(f"Não consegui dar o bônus a {objeto.__class__.__name__}")