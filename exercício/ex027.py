# Solicita o nome completo do usuário
nome_completo = str(input('Digite seu nome completo: ')).strip()

# Divide o nome em uma lista de palavras
nomes = nome_completo.split()

# Exibe o primeiro e o último nome
print(f'primeiro: {nomes[0]}')
print(f'último: {nomes[-1]}')
_________________________________________________
nome = str(input("Digite seu nome completo: ")).strip()
dividido = nome.split()

print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(dividido[0]))
print("Seu ultimo nome é {}".format(dividido[len(dividido)-1]))
