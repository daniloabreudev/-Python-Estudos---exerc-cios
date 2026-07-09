from rich import print

class Diario:
    def __init__(self, senhamestra = "ceV!@"):
        self.__segredos = []
        self.__senha = senhamestra.strip()


    def escrever (self,msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self,senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você nao pode ler o diário!")
        else:
            print(f"Diário liberado!")
            for segredo in self.__segredos:
                print(f"- {segredo}")

    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver a senha")


