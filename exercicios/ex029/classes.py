from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som")


class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está fazendo PRR Prr patapimba")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e tá fazendo auauau")

class Splitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e tá fazendo LALALA")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e tá fazendo TRALAREIRO TRALALÁ")


class Gato(Animal):
    pass

class Galinha(Animal):
    pass