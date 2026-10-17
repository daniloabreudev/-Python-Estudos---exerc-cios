from classes import *

def main():
    t = Termostato()
    try:
        t.temperatura = 117.0
    except Exception as e :
        print(f"Houve um problema: {e}")

    print(f"A temperatura atual é {t.ftemperatura}")

if __name__ == "__main__":
    main()