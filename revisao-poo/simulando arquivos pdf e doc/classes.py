from abc import ABC,abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str, ext:str, tam:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext


    @property
    def extensao(self):
        return self._extensao

    @abstractmethod
    def abrir(self):
        pass

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf','doc','docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise ValueError("o formato não é suportado")

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}'({self.tamanho/1000000} MB)"


class PDF(Arquivo):
    def __init__(self, nome:str, tam:int):
        super().__init__(nome = nome, ext = 'pdf', tam = tam )

    def abrir(self):
        print(f" Abrindo o arquivo {self.nome_completo} no Adobe Reader")


class DOC(Arquivo):
    def __init__(self, nome:str, tam:int):
        super().__init__(nome = nome,ext = 'docx', tam = tam)
    def abrir(self):
        print(f" Abrindo o arquivo {self.nome_completo} no Microssolft Word")



def abrir_arquivo(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Não consegui abrir o arquivo {objeto.nome_completo}")

