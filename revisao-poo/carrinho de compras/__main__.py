from classes import *
def main():
    p1 = Produto("Caderno",23)
    p2 = Produto("Lápis",24)
    p3 = Produto("MOuser",34)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1+p1
    c1 = c1+p3
    print(c1)


if __name__ == '__main__':
    main()