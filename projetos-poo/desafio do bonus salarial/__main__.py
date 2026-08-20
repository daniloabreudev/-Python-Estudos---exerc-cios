from classes import *

def main():
    a = Desenvolvedor("Alex",2300)
    b = Designer("Ana",2345)
    c = Desenvolvedor("Danilo",5000)

    fazer_calculo(a)
    fazer_calculo(b)
    fazer_calculo(c)

    print(a.calcular_bonus())
    print(b)
    print(c)

if __name__ == "__main__":
    main()