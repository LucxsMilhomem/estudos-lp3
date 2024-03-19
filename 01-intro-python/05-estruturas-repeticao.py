#for, while, break, continue

# operador in

for letra in "Python":
    print(letra)

itens = ["banana", "arroz", "limão"]
alunos = ["Rony Rustico", 'Panpan']

for item in itens:
    print(item)

for i in range(5):
    print(i) # 0, 1, 2, 3, 4

for i in range(0, 11, 2):
    print(i) # 0, 2, 4, 6, 8, 10


# lista = [0, 1, 2, 3..., 100]
# for
# list + rage
lista = list(range(101))

# while
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

# break
# encontre o primeiro número par
numeros = [1, 3 ,4 ,5 ,8 , 11]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break

# Continue
numeros = [3, -1, 3, 0, -2]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

# compreensão de lista
# forma concisa de criar listas em python
numeros = [2, 3, 4, 5, 6]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

quadrados = [numero ** 2 for numero in numeros]

palavra = "pipocaaaaa"
letras = [letra for letra in palavra]
letras = [letra.upper() for letra in palavra]