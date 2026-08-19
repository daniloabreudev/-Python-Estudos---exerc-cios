class Numero:

    def __init__(self, valor: int|float = 0):
        self.valor = valor

    def dobrar(self):
        pass

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do número"

class Texto:

    def __init__(self, txt: str = ""):
        self.texto = txt

    def dobrar(self):
        pass

    def __str__(self):
        return f"Tenho o texto {self.texto} dentro do texto"

class Lista:

    def __init__(self, lst:list = []):
        self.valores = lst

    def dobrar(self):
        pass

    def __str__(self):
        return f"Tenho a lista {self.valores} dentro da lista"

class Papel:

    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        pass

    def __str__(self):
        return f"O papel está dobrado ? {self.dobrado}"

class Casa:

    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa muito engraçada..."

# DUCK TYPING

def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Tive dificuldades para dobrar o objeto {objeto.__class__.__name__}")

