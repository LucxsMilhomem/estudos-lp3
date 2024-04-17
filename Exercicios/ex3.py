from unidecode import unidecode


def contar_vog_con(frase):
    vogais = 0
    consoantes = 0
    
    frase = unidecode(frase.lower())
    
    vogais_lista = ['a', 'e', 'i', 'o', 'u']
    
    for char in frase:
        if char.isalpha():
            if char in vogais_lista:
                vogais += 1
            else:
                consoantes += 1
    return vogais, consoantes

frase = input("Digite uma frase: ")

num_vogais, num_consoantes = contar_vog_con(frase)

print("Número de vogais:", num_vogais)
print("Número de consoantes:", num_consoantes)