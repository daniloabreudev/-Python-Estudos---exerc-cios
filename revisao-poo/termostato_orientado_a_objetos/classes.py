class Termostato:
    def __init__(self, temperatura:float = 16):
        self.__temperatura =16
        self.temperatura = temperatura


    @property
    def temperatura(self):
        return self.__temperatura

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"


    @temperatura.setter
    def temperatura(self,nova_temp:float):
        if (nova_temp *2) %1 == 0 and 16 <= nova_temp <=30:
                self.__temperatura = nova_temp
        else:
            raise ValueError(f"Inválido. A temperatura precisa ser entre 16 a 30 graus, e valores inteiros ou terminados em .5")