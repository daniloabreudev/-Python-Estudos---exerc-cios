from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str, tam:int|float):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = txt

    def converter(self) -> float:
        return  self.tamanho / 1000000

    @abstractmethod
    def abrir(self) -> None:
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'doc', 'docx']


class Doc(Arquivo):

    def abrir(self) -> None:
        print(f"Abrindo o arquivo '{self.nome}.docx' ({self.converter():.2f}MB) no Microssoft Word")


class Pdf(Arquivo):

    def abrir(self):
        print (f"Abrindo o arquivo '{self.nome}.pdf' ({self.converter():.2f}MB) no Adobe Reader")


#Ducking  Tiping

def abrir_arquivo(objeto: object) -> None:
    try:
        objeto.abrir()
    except AttributeError:
        print(f"Nâo consegui abrir o arquivo: o objeto {objeto.__class__.__name__} não implementa 'abrir' ")