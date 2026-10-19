from abc import ABC, abstractmethod
from datetime import datetime
ano_atual = datetime.now().year


class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int ):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= ano_atual:
            self._nascimento = ano
        else:
            raise ValueError (f"Ano {ano} é inválido")

    @property
    def idade(self):
        return ano_atual - self._nascimento

    @idade.setter
    def idade(self, ano):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento.")



class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'Eng.Software','TI']
    cursos_oficiais = [curso.upper() for curso in cursos_oficiais]

    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso.upper()

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")

    def add_curso(self, curso:str):
        curso = curso.upper().strip()

        if curso not in Aluno.cursos_oficiais and len(curso) > 2:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError ("Esse curso já está incluso")



