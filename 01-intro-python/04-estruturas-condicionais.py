#if
idade=20

# if condição
#   codigo
#   codigo
#   codigo

# if
if idade >=18:
    print("Maior de idade")

# if/else

if idade >=18:
    print("Maior de idade")
else:
    print("Menor de de idade")

# if/elif/else

if idade <= 12:
    print("criança")
elif idade <= 17:
    print("adolescente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")


# if aninhado
email = "corotinho@gmail.com"
senha = "pepsiBlack"

if email == "corotinho@gmail.com":
    if senha == "pepsiBlack":
        print("acesso liberado")
    else:
        print("acesso negado")
else:
    print("acesso negado")


if email == "corotinho@gmail.com" and senha == "pepsiBlack":
    print("acesso liberado")
else:
    print("acesso negado")


dia = 4

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-Feira")
elif dia == 3:
    print("Terça-Feira")
elif dia == 4:
    print("Quarta-Feira")
elif dia == 5:
    print("Quinta-Feira")
elif dia == 6:
    print("Sexta-Feira")
else:
    print("Sabado")


dias = {
    1: "Domingo",
    2: "Segunda-Feira",
    3: "Terça-Feira",
    4: "Quarta-Feira",
    5: "Quinta-Feira",
    6: "Sexta-Feira",
    7: "Sabado"
}

if dia in dias:
    print(dias[dia])


match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sabado")