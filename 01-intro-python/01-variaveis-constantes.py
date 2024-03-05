# Identificadores
# letras, numero, e _
# case sensitive
# palavras reservadas: if, for, class, main
idade=20
Idade=20

#Variaveis em Python
velocidade= 10.5
velocidadeMaior=30

nome="Matheus Ladrão"

# constantes não existe, existe convenção, que é o identificador de uma constante como letra maiuscula
PI=3.1415

'''
comentario
de multiplas
linhas
'''

#def serve para definir função, os parametros terminam no :

def somar(numero1, numero2=2):
    '''
    a função tem que estar alinhada dentro da identação para funcionar

    é uma funçaõ que soma 2 números

    :param numero1: primeiro número
    :param numero2: segundo número
    :return: soma de números
    '''
    return numero1 + numero2

print(somar(10.0))