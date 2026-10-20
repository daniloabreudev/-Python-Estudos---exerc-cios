from classes import *

def main():

    p1 = Credito(230)
    p2 = Pix(234)
    p3 = Boleto(900)

    finalizar_compra(p1)
    finalizar_compra(p2)
    finalizar_compra(p3)



if __name__ == '__main__':
    main()