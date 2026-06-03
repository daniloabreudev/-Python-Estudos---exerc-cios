from funcionarios import *


def main():
    f1 = Mensalista("Amanda", 10000)
    f1.calc_sal()
    f1.analisar_sal()
    f2 = Horista("paulo",12,200)
    f2.calc_sal()
    f2.analisar_sal()


if __name__ == "__main__":
    main()