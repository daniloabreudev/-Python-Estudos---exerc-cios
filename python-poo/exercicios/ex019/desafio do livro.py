from rich import print
class Livro:
    def __init__(self,titulo,total):
        self.titulo = titulo
        self.total = total
        self.pag_atual = 1

        print(f":open_book:Você acabou de abrir o livro {self.titulo} que tem {self.total} páginas no total.Você agora está na página {self.pag_atual}")
    def avancar_paginas(self,avanco):
        self.pag_atual += avanco
        for c in range(self.pag_atual):
            print(f"Pág{c} ",end='')


l1 = Livro("10 coisas que aprendi",20)
l1.avancar_paginas(5)
l1.avancar_paginas(4)