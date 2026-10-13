from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Mensagem(ABC):
    def __init__(self, msg: str):
        self.msg = msg

    @abstractmethod
    def mostrar(self) -> None:
        pass

class Erro(Mensagem):
    def mostrar(self) -> None:
        # Formata o texto com a cor vermelha e coloca dentro do Panel
        conteudo = f"[red]{self.msg}[/red]"
        print(Panel(conteudo, title="ERRO"))


class Aviso(Mensagem):
    def mostrar(self) -> None:
        # Exemplo com formatação em amarelo para o Aviso
        conteudo = f"[yellow]{self.msg}[/yellow]"
        print(Panel(conteudo, title="AVISO"))