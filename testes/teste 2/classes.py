
class Avaliacao():
    def __init__(self,nome:str, disciplina:str, nota:float = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = 0
        self.nota = nota

    @property
    def nota (self):
        return self._nota


    @nota.setter
    def nota(self,nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
        else:
            print(f"A nota não pode ser maior que 10 ou menor que 0. Tente novamente")