from classes import *

def main():
    equipe = [
        Desenvolvedor("Ana",12000),
        Gerente("Danilo",15000),
        Designer("Eduardo",10000),
    ]

    equipe[0].salario = 14000

    for funcionario in equipe:
        print(funcionario)


if __name__ == "__main__":
    main()