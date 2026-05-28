from abc import ABC,abstractmethod
import math

class Poligono(ABC):
    def __init__(self,lado):
        self.lado = lado

    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self,lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self) ->float:
        return self.lado *4

    def area(self) ->float :
        return self.lado **2

class Circulo(Poligono):
    def __init__(self,raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2* math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2



