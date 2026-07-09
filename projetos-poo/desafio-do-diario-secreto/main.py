from logging import exception

from desafiodoriario import Diario

def main():
    meudiario = Diario()
    meudiario.escrever("Essa é a primeira mensagem")
    meudiario.escrever("Segunda mensagem")

    try:
        meudiario.ler("ceV!@")
    except exception as e:
        print(f"ERRO: {e}")


if __name__ == "__main__":
    main()