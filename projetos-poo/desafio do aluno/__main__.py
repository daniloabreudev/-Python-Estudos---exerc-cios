from classe033 import *

def main():
    a1 = Aluno("Ana",2000,'ADM')
    print(f"Sua idade atual é {a1.idade} anos.")
    a1.add('moda')
    a1.curso = "moda"
    print(a1.__dict__)
    try:
        a1.idade = 23  # Tenta fazer a alteração proibida
    except PermissionError as e:
        print(f"OPERAÇÃO BLOQUEADA: {e}")

if __name__ == "__main__":
    main()