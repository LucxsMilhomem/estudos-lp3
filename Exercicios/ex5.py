def verifica_palindromo(texto):
    texto = texto.lower()
    return texto == texto[::-1]

palavra_frase = input("Digite uma palavra ou frase: ")
if verifica_palindromo(palavra_frase):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")