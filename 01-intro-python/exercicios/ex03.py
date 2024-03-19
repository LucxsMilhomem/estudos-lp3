ValorInicial = float(input("Digite o valor da compra "))
ValorFinal = ValorInicial

if ValorInicial >= 10.00 and ValorInicial <= 99.99:
    ValorFinal = ValorInicial-(ValorInicial*0.05)

if ValorInicial >= 100.00 and ValorInicial <= 499.99:
    ValorFinal = ValorInicial-(ValorInicial*0.10)

if ValorInicial >= 500.00:
    ValorFinal = ValorInicial-(ValorInicial*0.15)

print("Valor do Produto", ValorInicial, "\nValor final com Desconto:", ValorFinal)