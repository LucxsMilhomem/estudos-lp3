# Tipos de dados

# 1. Númerico
# int, float, complex

# int
idade=10
temperatura=-30

# Float
altura=178.80

# 2. Boolean
pau=True
noRego=False

#Multilinha
frase="""Pato
morreu
engasgado
de pão
"""

# interpolação de string
# f-strings
nome="Calleri"
idade=27
frase=f"Olá {nome}. Você tem {idade} anos"
print(frase)

# Acesso um caractere da String
nome = "thiago Kloppini"

print(nome[:])

print(nome.capitalize())

habilidades = []
habilidades= ["o James", "Eu quero uma salada de fruta", "Que Habilidade"]

print(habilidades[2])

habilidades.append("Ankara Luciano")

print(habilidades)

habilidades.insert(3, "Cortou pra esquerda, WELLINGTON RATOOO")

print(habilidades)

'''
habilidades.clear()
print(habilidades)
'''

for habilidade in habilidades:
    print(habilidade)

#Tupla, não pode ser alterada
opcoes= ("Vitória", "Derrota", "Empate")

for opcao in opcoes:
    print(opcao)


# set é um conjunto que não permite elementos duplicados

habilidades = {"passe de trivela", "rolinho", "carretilha"}

habilidades.add("chapeu")

print(habilidades)

nome="Ferreira"
idade=25
habilidades={"passe de trivela", "rolinho", "carretilha"}
empregado=True

candidato = {
    "nome":nome,
    "idade": idade,
    "habilidades":habilidade,
    "empregado":True
}

