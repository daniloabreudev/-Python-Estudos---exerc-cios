from classes import *

def main():
    meudiario = Diario()
    meudiario.escrever("This is mensseger First")
    meudiario.escrever("This is mensseger Second")
    meudiario.senha= 'arroz'

    try:
        meudiario.ler("arroz")
    except Exception as e:
        print(f"ERRO: {e}")




if __name__ == "__main__":
    main()