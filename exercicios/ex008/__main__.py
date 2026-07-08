from contabancaria import *
def main():
    c1 = ContaBancaria(111,"maria",5000)
    c1.depositar(345)
    c1.sacar(234)
    print(c1)


if __name__=="__main__":
    main()