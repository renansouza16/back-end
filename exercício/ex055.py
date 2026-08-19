sexo = input('Informe seus dados [m/f]: ').strip().lower()[:1]
while sexo not in ['m', 'f'] or not sexo:
    print('Dados inconsistentes!')
    sexo = input('Informe novamente [m/f]: ').strip().lower()[:1]

print(f'O seu sexo é {sexo}')
