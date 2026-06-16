from classes import *

def main():
    p1 = Guerreiro("Picaxu",1000)
    p2 = Mago("Gandalf",2000)

    p1.atacar(p2,340)
    p2.atacar(p1,323)
    p1.curar()
    p2.curar()


if __name__ == "__main__":
    main()