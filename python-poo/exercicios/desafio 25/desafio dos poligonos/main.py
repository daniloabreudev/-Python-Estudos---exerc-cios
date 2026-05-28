from rich import print
from poligono import  Quadrado,Circulo

def main():
    q = Quadrado(20)

    print(f"Um quadrado de lado {q.lado}cm tem perímetro de {q.perimetro()}mm2 ")
    print(f"UM quadrado de lado {q.lado}cm tem area de {q.area()}mm2 ")

    c = Circulo(12)
    print(f"Um círculo de raio {c.raio}cm tem perimetro de {c.perimetro():.1f}Cm ")
    print(f"Um circulo de raio {c.raio}cm tem area de {c.area():.1f}cm2 ")

if __name__ == "__main__":
    main()