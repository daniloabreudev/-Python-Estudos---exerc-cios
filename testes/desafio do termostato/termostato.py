class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return f"{self.__temperatura}°C."

    @temperatura.setter
    def temperatura(self,valor):
        if (valor <16 or valor >32) or (valor % 0.5 != 0):
            print(f"Temperatura Inválida! Tente números entre 16 e 32 de meio em meio")
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C."

