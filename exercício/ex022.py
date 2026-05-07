nome = str(input('Digite seu nome completo')).strip()
dividido = nome.split()

print('Analisando seu nome...')
print('seu nome em maísculas é{}'.format(nome.upper()))
print('seu nome em maísculo é{}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count('')))
print('seu primeiro nome é {} e ele tem {}letras'.format(dividido[0], len(dividido[0])))
