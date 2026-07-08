from rich import print
class Funcionario:
    def __init__(self,nome,setor,cargo ):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao (self):
        return f":woman_technologist:Olá, Sou [green]{self.nome}[/] e sou {self.cargo} do setor de [yellow]{self.setor}[/] da empresa Curso em Vídeo!"

c1 = Funcionario("Maria","Administração","Diretora")
print(c1.apresentacao())
c2 = Funcionario("Anderson da Mídia","Engenharia de Software","Programador")
print(c2.apresentacao())