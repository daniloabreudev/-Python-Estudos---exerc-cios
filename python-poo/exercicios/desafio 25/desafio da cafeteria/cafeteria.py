from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print(f"--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print(f"1. Fervendo água a 100 Graus Célsius")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__(self):
        pass
        super().__init__()

    def misturar(self):
        print(f'2. Adicione o pó de café a água')
    def servir(self):
        print(f"3. Servindo Numa xícara de porcelana , com açúcar a gosto.")





