from rich.panel import Panel
from rich import print

class Produto:
    def __init__ (self,nome,preco):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        conteudo = f"[cyan]{self.nome}[/]\n {"-"*30}\nPreço: [green]R$ {self.preco:,.2f}[/]"
        print(Panel(conteudo, title="[bold yellow]PRODUTOS[/]", expand=False))



p1 = Produto("Iphone 17 Pro MAX", 25.000)
p2 = Produto("TV Samsung Tyzen 64 Polegadas",10000)

p1.etiqueta()
p2.etiqueta()