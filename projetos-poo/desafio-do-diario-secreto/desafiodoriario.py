from rich import print

class Diario:
    def __init__(self, senhamestra = "teleflix"):
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

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) < 8 :
            raise ValueError(f"Tente novamente. A senha precisa ter no mínimo 8 caracteres!")
        else:
            self.__senha = nova_senha

