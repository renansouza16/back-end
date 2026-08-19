sexo = input('Informe seus dados [M/F]: ').strip().lower()[:1]

while sexo not in 'mf' or sexo == '':
    sexo = input('Dados inconsistentes. Informe novamente: ').strip().lower()[:1]

print(f'O seu sexo é {sexo.upper()}')
