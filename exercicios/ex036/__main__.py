from crud import *
def exibir_menu():
    print(("\n" + "=" * 30))
    print(f"    SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Atualizar pessoas")
    print("4 - Excluir pessoa")
    print("5 - Busca por nome")
    print("0 - Sair")
    print("=" * 30)


def main():
    if not criar_banco():
        print("Algum problema aconteceu ao criar o banco")
        raise SystemExit

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:").strip()

        match opcao:
            case "1": #Cadastrar pessoa
                if not cadastrar_pessoa():
                    print("\n[ERRO] não foi possível cadastrar a pessoa")
            case "2": #LIstar pessoas
                if not listar_pessoas():
                    print(f"\n[ERRO] Não foi possível mostrar a listagem")
            case "3": #Atualizar pessoas
                if not atualizar_pessoa():
                    print(f"\n[ERRO] não foi possível atualizar o cadastro")
            case "4": #Excluir pessoas
                if not excluir_pessoa():
                    print(f"\n[ERRO] Não foi possível excluir a pessoa")
            case "5": #Busca por nome
                if not buscar_pessoa_por_nome():
                    print(f"\n[ERRO] Não foi possível buscar os dados")
            case "0": # Sair
                print("\nEncerrando o sistema...")
                break
            case _:
                print("\n[ERRO] Opção inválida! EEscolha um valor entre 0 e 5!")
        input("Pressione ENTER para continuar")

if __name__ == "__main__":
    main()


