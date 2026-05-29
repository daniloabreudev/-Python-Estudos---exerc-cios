from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self,distancia,frete):
        self.distancia = distancia
        self.frete =frete

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self,distancia,peso,fator):
        self.fator = fator

    def calc_frete(self):
        pass


class Caminhao(Transporte):
    def __init__(self, taxa=0):
        self.fator = taxa

    def calc_frete(self):
        pass


class Drone(Transporte):
    def __init__(self, taxa=0):
        self.fator = taxa

    def calc_frete(self):
        pass
