casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Salário do comprador: R$"))
financiamento = int(input("Quantos anos de financiamento? "))

# Calcula o valor da prestação mensal
prestacao = casa / (financiamento * 12)

# Regra: prestação não pode exceder 30% do salário
limite = salario * 0.3

if prestacao <= limite:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}. Empréstimo aprovado!".format(casa, financiamento, prestacao))
else:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}. Empréstimo negado!".format(casa, financiamento, prestacao))
