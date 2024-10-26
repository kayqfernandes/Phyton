import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 1000)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação")
    print("Tente Adivinha o numero de 1 a 1000")

    while True:
        palpite = int(input("palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("O número é maior")
        
        elif palpite > numero_secreto:
            print("O número é menor")
        
        else:
            print(f"Parabéns Você adivinhou o {numero_secreto} com {tentativas}")

            break

jogo_adivinhacao()