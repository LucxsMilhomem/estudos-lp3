def simulador_eleicoes():
    candidatos = ["Candidato 1", "Candidato 2", "Candidato 3"]
    votos = [0, 0, 0]
    
    print("Escolha seu candidato:")
    print("1. Candidato 1")
    print("2. Candidato 2")
    print("3. Candidato 3")
    print("0. Encerrar a votação")

    while True:
        
        voto = input("Digite o número correspondente ao candidato (ou 0 para encerrar): ")

        if voto == '0':
            break
        elif voto in ['1', '2', '3']:
            indice = int(voto) - 1
            votos[indice] += 1
            print("Voto registrado para", candidatos[indice])
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 3 ou 0 para encerrar a votação.")

    print("\nResultado da votação:")
    for i in range(len(candidatos)):
        print(candidatos[i], ":", votos[i], "votos")

    vencedor = candidatos[votos.index(max(votos))]
    print("\nO vencedor é:", vencedor)

simulador_eleicoes()