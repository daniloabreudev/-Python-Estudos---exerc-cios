from ex009 import  Avaliacao
from rich import print,inspect

def main():
    av1 = Avaliacao("pedro","Matemática",9.6)
    av1.set_nota(7)
    print(f"{av1.nome} tirou {av1._nota} na disciplina de {av1.disciplina}")

if __name__ == "__main__":
    main()