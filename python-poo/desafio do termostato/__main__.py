from termostato import Termostato

def main():
    t1 = Termostato()
    t1.temperatura = 29.8
    print(f"TEMPERATURA ATUAL: {t1.temperatura} graus celsius")

if __name__== "__main__":
    main()