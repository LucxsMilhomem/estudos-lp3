import random

def jogo_de_adivinhacao():
    n_aleatorio = random.randint(1, 100)
    tentativas = 0

    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < n_aleatorio:
            print("Seu palpite está baixo. Tente novamente.")
        elif palpite > n_aleatorio:
            print("Seu palpite está alto. Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {n_aleatorio} em {tentativas} tentativas.")
            break

jogo_de_adivinhacao()