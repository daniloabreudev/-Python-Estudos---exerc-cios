class Porta:
    def abrir(self):
        print(f"Girar a maçaneta eempurrar/Puxar a porta")

class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor")


class Ovo:
    def abrir(self):
        print(f"Quebre a casca com uma colher e leve a frigideira")

class Pedra:
    pass

#Mètodo pythonico polimoórfico duck typing

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao abrir {objeto.__class__.__name__}")
