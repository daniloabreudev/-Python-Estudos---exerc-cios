from rich import print

class Termostato:
    def __init__(self,temperatura = 16):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,graus):
        if 16<= graus <=30 and (graus % 0.5 == 0):
            self.__temperatura = graus
        else:
            print(f"O [green] termostato[/] só aceita valores em [blue]16°[/] e [blue]30°[/] graus,de meio em meio grau! EX: 18.5. valores como 18.4 não são aceitos")