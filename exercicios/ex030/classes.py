class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com leite condesado e calda")

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha no òleo de Soja")


class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz com Leite ninho e NUtella")

class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} faz coxinha na AIR_frier")