from abc import ABC, abstractmethod
from time import sleep


class BebidaQuente(ABC):

    def preparar(self):
        print(f"--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida pronta ---")


    def ferver_agua(self):
        print(f"1. Fervendo água a 100 Graus Célsius")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        print(f'2. Passando a água pressurizada pelo pó de café moído')
    def servir(self):
        print(f"3. Servindo Numa xícara de porcelana , com açúcar a gosto.")

class Cha(BebidaQuente):

    def misturar(self):
        print(f'2. Adicione as ervas turcas á agua')
    def servir(self):
        print(f"3. Servindo o chá Numa xícara de porcelana inglesa,adicione açucar a gosto")

class Leite(BebidaQuente):

    def misturar(self):
        print(f'2. Adicione o leite em pó')
    def servir(self):
        print(f"3. Sirva numa caneca grande chinesa ! Adicione chocolate , a gosto.")



