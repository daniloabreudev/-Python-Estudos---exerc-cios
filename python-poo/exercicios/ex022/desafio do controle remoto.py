from rich.panel import Panel
from rich import print

class ControleRemoto:
    canal_min:int =1
    canal_max:int = 6
    volume_min:int = 1
    vol_maximo:int = 5

    def __init__(self,canal =1,volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual +=1
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -=1
    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.vol_maximo:
                self.volume_atual +=1
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self):
        conteudo =''
        if not self.ligado:
            conteudo = "[red]:prohibited: A tv está desligada"
        else:
            conteudo ='CANAL  = '
            for canal in range(ControleRemoto.canal_min,ControleRemoto.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min,ControleRemoto.vol_maximo+1):
                if volume <= self.volume_atual:
                    conteudo += '[black on cyan] [/]'
                else:
                    conteudo += '[black on white] [/]'


        tv = Panel(conteudo,title ="TV",width=30)
        print(tv)

c = ControleRemoto()
while True:
    c.mostrar_tv()
    comando = str(input(f"\n < CH{c.canal_atual} > - VOL{c.volume_atual} + "))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()



