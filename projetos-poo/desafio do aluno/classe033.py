from datetime import date
ano_atual = date.today().year

class Aluno:
    def __init__(self, nome,nascimento,curso):
        self._nome = nome
        self._nascimento = nascimento
        self._curso = curso

        self._cursos_oficiais = [
            'ADM',
            'ADS',
            'ENGENHARIA DE SOFTWARE',
            'CIÊNCIA DA COMPUTAÇÃO',
            'ENGENHARIA DE DADOS',
            'INTELIGENCIA ARTIFICIAL'
        ]

    @property
    def cursos(self):
        return self._cursos_oficiais

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,novo_curso):
        curso_formatado = novo_curso.upper().strip()
        if curso_formatado not in self._cursos_oficiais:
            raise ValueError(f"O curso {novo_curso} não está na lista de cursos oficiais.")
        self._curso = curso_formatado

    @property
    def idade(self):
        return ano_atual - self._nascimento

    @idade.setter
    def idade(self,valor):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")

    @property
    def add(self):
        return self.add

    def add(self,novo_curso):
        curso_formatado = novo_curso.upper().strip()
        if curso_formatado not in self.cursos:
            self._cursos_oficiais.append(curso_formatado)
        else:
            raise ValueError(f"Você não pode adicionar ese curso, pois ele já está na lista!")
