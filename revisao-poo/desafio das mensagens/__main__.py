from classes import Mensagem, Aviso, Erro


def main():
    # 1. Testando classe base (preto e branco)
    m = Mensagem("Falha geral no sistema", tipo="critico")
    m.mostrar()

    # 2. Testando Aviso (amarelo)
    a = Aviso("Contamos com sua ajuda")
    a.mostrar()

    # 3. Testando Erro (vermelho)
    e = Erro("Conexão perdida com o banco de dados")
    e.mostrar()


if __name__ == '__main__':
    main()