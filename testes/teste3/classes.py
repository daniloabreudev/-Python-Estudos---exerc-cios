class Aluno:
    def __init__(self,nome , n1, n2):
        self.nome = nome
        self.nota1 = n1
        self.nota2 = n2
        self.situacao = self.calcula_nota()

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def calcula_nota(self):
        if self.media() >=7:
            return  "Aprovado"
        elif self.media() >=5:
            return "Recuperação"
        else:
            return "Reprovado"

    def exibir_resultado(self):
        return f"O aluno {self.nome} tirou média {self.media()} e tem a situação {self.situacao}"