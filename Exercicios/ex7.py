import random

def escolher_palavra():
    palavras = ['banana', 'laranja', 'abacaxi', 'uva', 'maca', 'morango', 'pera', 'manga', 'cachorro', 'gato', 'elefante', 'leao', 'tigre', 'girafa', 'zebra']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao

palavra = escolher_palavra()
tentativas_restantes = 6
letras_corretas = []
letras_erradas = []

print("A palavra tem", len(palavra), "letras.")

while tentativas_restantes > 0:
    print("\nPalavra:", exibir_palavra(palavra, letras_corretas))
    print("Tentativas restantes:", tentativas_restantes)
    print("Letras erradas:", letras_erradas)

    letra = input("Digite uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra válida.")
        continue

    if letra in letras_corretas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra:
        letras_corretas.append(letra)
        if len(set(letras_corretas)) == len(set(palavra)):
            print("\nParabéns! Você acertou a palavra:", palavra)
            break
            
    else:
        letras_erradas.append(letra)
        tentativas_restantes -= 1

if tentativas_restantes == 0:
    print("\nVocê perdeu! A palavra era:", palavra)

