from rich import print
class Caneta:
    def __init__(self,cor):
        self.cor = cor.lower()
        self.cores = {'verde':'green','azul':'blue','vermelho':'red','amarelo':'yellow','laranja':'orange','preto':'black','branco':'white','rosa':'pink'}
        self.tampada = True


    def cor_caneta(self):
        return self.cores.get(self.cor,'white')

    def escrever(self,msg):
       if self.tampada == False:
           cor_rich = self.cor_caneta()
           print(f"[{cor_rich}]{msg}[/]", end= self.quebrar_linha(1))

       else:
           print(f"Caneta {self.cor} tampada! Destampe-a para usar")

    def destampar(self):
        self.tampada = False

    def quebrar_linha(self,qtd = 1):
        print('\n'* qtd,end='')

c1 = Caneta("veRde")
c2 = Caneta("vermelho")
c3 = Caneta("azul")
c1.destampar()
c2.destampar()
c3.destampar()
c1.escrever("Olá,tudo bem?")
c2.escrever("Prr,Prr patapimba")
c2.quebrar_linha(2)
c3.escrever("A vida é bela")

