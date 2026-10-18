
class Diario:
    def __init__(self, senha = "Cev$"):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, msg:str):
        if isinstance(msg, str) and len(msg)>0:
            self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha incorreta. Você não pode ler")
        else:
            print(f"Diário Liberado")
            for seg in self.__segredos:
                print(f"- {seg}")

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha")

    @senha.setter
    def senha(self, new_senha):
        if isinstance(new_senha, str) and len(new_senha)>0:
            self.__senha = new_senha.strip()
        else:
            print(f"Você não pode usar essa senha. Tente novamente")
