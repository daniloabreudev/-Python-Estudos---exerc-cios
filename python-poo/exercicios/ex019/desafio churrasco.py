from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self,titulo,quantidade):
        self.titulo = titulo
        self.quant = quantidade
        self.consumo_padrao = 0.400
        self.valor_kg = 82.40

    def tot_compra_kg(self):
        return self.quant * self.consumo_padrao

    def custo_total(self):
        return self.tot_compra_kg() * self.valor_kg

    def custo_pessoa(self):
        return self.custo_total() / self.quant



    def analisar(self):
        conteudo = f"Analisando o [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\nCada participante comerá {self.consumo_padrao} kg e cada Kg custa R${self.valor_kg:.2f}\nRecomendo [blue]comprar {self.tot_compra_kg()} Kg[/] de carne\nO custo total será de [green]{self.custo_total():.2f}[/]\nCada pessoa pagará [yellow]R${self.custo_pessoa():.2f}[/] para participar"
        print(Panel(conteudo,title= self.titulo,expand= False))




c1 = Churrasco("Churras dos amigos",15)
c1.analisar()