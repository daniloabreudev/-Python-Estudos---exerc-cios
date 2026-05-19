from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self,jogo):
        self.favoritos.append(jogo)

    def ficha(self):
        meus_jogos = ""
        for jogo in self.favoritos:
            meus_jogos += f":slot_machine:{jogo}\n"
        conteudo = f"Nome real: [blue]{self.nome}[/]\n[yellow]Jogos Favoritos:[/]\n[green]{meus_jogos}"

        print(Panel(conteudo,title= self.nick, expand=False ))





j1 = Gamer("Fabricio da Silva","Detonador2k25")
j1.add_favoritos("Bomba Patch")
j1.add_favoritos("Gta")
j1.add_favoritos("MArio Bross")
j1.add_favoritos("Residente evil")
j1.ficha()

j2=Gamer("Andrei de oliveira", "Elias Gravações")
j2.add_favoritos("Sony")
j2.ficha()

