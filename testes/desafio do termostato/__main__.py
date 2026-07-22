from termostato import Termostato

def main():
    t = Termostato()
    t.temperatura = 32
    t.temperatura = 23.50
    print(f"A temperatura atual é {t.temperatura}")
    print(t.ftemperatura)


if __name__ == "__main__":
    main()