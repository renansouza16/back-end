from random import randint
from time import sleep

print('''Suas opções:
[0] pedra
[1] papel
[2] Tesoura''')

jogada = int(input("Qual é a sua jogada? "))
jogadapc = randint(0, 2)
itens = ("Pedra", "Papel", "Tesoura")

print("jo")
sleep(1)
print("ken")
sleep(1)
print("po !!!")
sleep(1)
print("-=-" * 10)

print(f'''computador jogou {itens[jogadapc]}
jogador jogou {itens[jogada]}''')

print("-=-" * 10)

if jogadapc == 0 and jogada == 2 or jogadapc == 1 and jogada == 0 or jogadapc == 2 and jogada == 1:
    print("Computador vence")
elif jogada == 0 and jogadapc == 2 or jogada == 1 and jogadapc == 0 or jogada == 2 and jogadapc == 1:
    print("Jogador vence")
else:
    print("empate")
