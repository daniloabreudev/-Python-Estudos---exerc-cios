from classes import *

def mains():
    a = Aluno("José", 2000, "Ti")
    a.nascimento = 1980
    a.add_curso("moda")

    b = Aluno("Maria", 1998, "adm")

    print(a.cursos_oficiais)
    print(a.__dict__)
    print(b.cursos_oficiais)
    print(b.__dict__)


if __name__ == "__main__":
    mains()