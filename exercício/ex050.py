primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Fórmula correta do 10º termo: primeiro + (10 - 1) * razao
decimo = primeiro + 9 * razao 

# Somamos a razão no argumento final do range para que o décimo termo seja incluído
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('Acabou')
