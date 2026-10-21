# Em vez de apenas "from rich import print"
from rich.console import Console
from rich.panel import Panel

# force_terminal=True OBRIGA o console do PyCharm a renderizar as cores ANSI!
console = Console(force_terminal=True)
print = console.print


class Mensagem:
    def __init__(self, msg: str = '', tipo: str = 'aviso', icone: str = ":speech_balloon:"):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo.upper()} {self._icone}",
            style="bold white on blue",   # Fundo azul, letra branca
            border_style="bright_blue",
            width=55
        )
        console.print(msg)


class Erro(Mensagem):
    def __init__(self, msg: str = '', tipo: str = 'erro', icone: str = ":no_entry_sign:"):
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        meu_panel = Panel(
            f"[bold white]{self._mensagem}[/]",
            title=f"{self._icone} ERRO {self._icone}",
            style="bold white on red",    # Fundo vermelho vivo, letra branca
            border_style="bright_red",
            width=55
        )
        console.print(meu_panel)


class Aviso(Mensagem):
    def __init__(self, msg: str = '', tipo: str = 'aviso', icone: str = ":warning:"):
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        meu_panel = Panel(
            f"[bold black]{self._mensagem}[/]",
            title=f"{self._icone} AVISO {self._icone}",
            style="black on yellow",       # Fundo amarelo clássico, letra preta
            border_style="bright_yellow",
            width=55
        )
        console.print(meu_panel)