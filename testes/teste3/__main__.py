from classes import *

def main():
    while True:
        nome = str(input("NOME: "))
        nota1 = float(input("NOTA1: "))
        nota2 = float(input("NOTA 2: "))
        Aluno(nome, nota1, nota2)

        continuar = str(input("Deseja continuar?")).upper().strip()[1]
        if continuar == 'N':
            break



if __name__ == "__main__":
    main()