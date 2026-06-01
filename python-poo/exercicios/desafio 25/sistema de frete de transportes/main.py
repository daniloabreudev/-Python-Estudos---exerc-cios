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

def main():
    dist= 80
    viagem = [Moto(dist),Caminhao(dist), Drone(dist)]
    # entrega = Drone(dist)
    # print(f"Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}")
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    for item in viagem:
        tabela.add_row(f"{dist}km",f"{type(item).__name__}",f"{item.calc_frete()}")
    print(tabela)

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
