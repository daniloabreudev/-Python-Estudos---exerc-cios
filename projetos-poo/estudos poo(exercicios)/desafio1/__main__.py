from random import randint


escolha_pc = randint(1,100)
tentativas = 4

while True:
    minha_escolha = int(input("Escolha um número de 0 a 100: "))
    if escolha_pc == minha_escolha:
        print(f"Parabéns! Você venceu!!")
        break
    else:
        if tentativas > 0:
            tentativas -=1
            if escolha_pc < minha_escolha:
                print(f"Tente um número Menor! Ainda restam {tentativas+1} tentativas ")
            else:
                print(f"Tente um número Maior! Ainda restam {tentativas+1} tentativas")
        else:
            print(f"Game Over! Suas tentativas se esgotaram! ")
            print(f"Até o próximo Jogo!")
            break
