import math

ang = float(input("Digite o ângulo que você deseja: "))

# Os valores têm que ser em radianos, então usamos o math.radians
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print("O ângulo de {} tem seno de {:.2f}".format(ang, seno))
print("O ângulo de {} tem cosseno de {:.2f}".format(ang, cose))
print("O ângulo de {} tem tangente de {:.2f}".format(ang, tang))
