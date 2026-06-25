print("=" * 11 + " LOJAS SANTOS " + "=" * 11)
preco = float(input("Preço das compras: "))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

pagamento = int(input("Qual é a opção? "))

if pagamento == 1:
    desconto = preco - (preco * 0.1)
    print("Sua compra com o desconto à vista fica R${:.2f}".format(desconto))
elif pagamento == 2:
    desconto = preco - (preco * 0.05)
    print("Sua compra à vista no cartão fica R${:.2f}".format(desconto))
elif pagamento == 3:
    cartao = preco / 2
    print("Sua compra parcelada no cartão fica 2x de R${:.2f}".format(cartao))
elif pagamento == 4:
    parcela = int(input("Digite o número de parcelas: "))
    total_com_juros = preco + (preco * 0.2)
    valor_parcela = total_com_juros / parcela
    print("Sua compra será feita em {} parcelas de R${:.2f} COM JUROS.".format(parcela, valor_parcela))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total_com_juros))
else:
    print("Opção inválida de pagamento. Tente novamente.")
