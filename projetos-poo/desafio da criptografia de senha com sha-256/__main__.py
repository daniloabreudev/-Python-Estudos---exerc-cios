from criptografia import Credencial

def main():
    c = Credencial()
    c.senha = 'teste123'
    print(c.senha)

    c.validar('teste123')


if __name__ == "__main__":
    main()