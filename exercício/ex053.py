soma_idade = 0
maior_idade_homem = 0
nome_velho = ""
tot_mulher_20 = 0
reais_homens = 0

for c in range(1, 5):
    print(f"----- {c}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().lower()
    
    # Acumula a idade para a média posterior
    soma_idade += idade
    
    # Verifica o homem mais velho
    if sexo == "m":
        reais_homens += 1
        if reais_homens == 1 or idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome
            
    # Verifica mulheres com menos de 20 anos
    if sexo == "f" and idade < 20:
        tot_mulher_20 += 1

# Cálculo da média fora do laço
media = soma_idade / 4

print(f"\nA média de idade do grupo é de {media:.1f} anos.")

if reais_homens > 0:
    print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.")
else:
    print("Não foram cadastrados homens no grupo.")

print(f"Ao todo são {tot_mulher_20} mulheres com menos de 20 anos.")
