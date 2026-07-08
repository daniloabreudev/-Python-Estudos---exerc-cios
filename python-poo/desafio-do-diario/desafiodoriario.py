class Diario:
    def __init__(self):
        self.paginas = []


    def escrever (self,txt):
        self.paginas.append(txt)

    def ler(self):
        print(self.paginas)
