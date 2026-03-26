dias  = int(input('quantos dia alugados?'))
km = float(input('quantos k33m rodados?'))
diaria = dias*60 
percurso = km * 0.15
custo = diaria + percurso 
print('o total a pagar é de R${:.2f}'.format(custo))
