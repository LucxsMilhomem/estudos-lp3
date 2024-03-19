#operadores aritiméticos 
# +, -, /, *, %, **

nota1 = 10.0
nota2 = 6.0
nota3 = 5.5

media = (nota1 + nota2 + nota3) / 3

# 10 elevado ao quadrado (2)
numero = 10
elevado_quadrado = numero * numero
elevado_quadrado = numero ** 2

print('Maria')
print(2 + 3)
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

print(True or True) #True
print(True or False) #True
print(False or True) #True 
print(False or False) #False

verdade = True and True 

#permite a entrada no sistema 
#usuario não bloqueado E
#usuario é um funcionario E
#hora entre 8h e 18h 
# ---
#caso for admin pde acessar de qualquer forma 

usuario_bloquado = False
usuario_funcionario = True 
hora = 17 
usuario_admin = False 

funcionario_ativo = usuario_funcionario and not usuario_bloquado
horario_comercial = hora >=8 and hora <=18

def dentro_horario_comercial(hora):
    return hora >=8 and hora <=18

if (funcionario_ativo and dentro_horario_comercial) or usuario_admin:
    print("acesso liberado")
else: 
    print("acesso nao liberado")

nota1=10.0
nota2=5.5

if nota1>nota2:
    print("Aluno foi melhor na prova 1")
else:
    print("Aluno foi melhor na nota 2, ou teve a mesma nota nas 2")

a = [1,2,3]
b = [1,2,3]
print(a==b) # mesmos valores, true

print(a is b) # False

c = b
print(c is b) # True

opcoes = ("sim", "não", "talvez")
opcao = input("Digite uma opção")

if opcao in opcoes:
    print("ok")
else:
    print("invalido")