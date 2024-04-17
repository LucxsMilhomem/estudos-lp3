def converter_nota(pontuacao):
    if pontuacao >= 90:
        return 'A'
    elif pontuacao >= 80:
        return 'B'
    elif pontuacao >= 70:
        return 'C'
    elif pontuacao >= 60:
        return 'D'
    else:
        return 'F'
    
    
while True:
    try:
        pontuacao = int(input("Digite a pontuação (0 a 100): "))
        if pontuacao > 0 and pontuacao < 100:
            nota = converter_nota(pontuacao)
            print(f"A nota correspondente à pontuação {pontuacao} é: {nota}")
            break
        else:
            print("Por favor, insira uma pontuação válida entre 0 e 100.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")