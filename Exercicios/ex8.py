def contar_palavras(frase):
    palavras = frase.lower().split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

while True:
    texto = input("Digite uma frase (ou 'sair' para encerrar): ")
    if texto.lower() == 'sair':
        break
    resultado = contar_palavras(texto)
    print("Contagem de palavras:", resultado)
