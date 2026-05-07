# Solicita o nome completo do usuário
nome_completo = str(input('Digite seu nome completo: ')).strip()

# Divide o nome em uma lista de palavras
nomes = nome_completo.split()

# Exibe o primeiro e o último nome
print(f'primeiro: {nomes[0]}')
print(f'último: {nomes[-1]}')
