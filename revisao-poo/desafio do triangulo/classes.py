class Retangulo:
    def __init__(self,base:float = 1, altura:float = 1):

        self.__altura = None
        self.__base = None


    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self,base:float):
        if base > 0:
            self.__base = base
        else:
            raise ValueError("Valor inválido para Base")

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self,altura:float):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("Valor inválido para altura")

    def medidas(self):
        return f'Base: {self.base}\nAltura: {self.altura}\nMedidas: {self.altura*self.base:.1f}'




