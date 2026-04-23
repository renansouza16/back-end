catop = float(input("Cateto oposto: "))
catad = float(input("Cateto adjacente: "))
# Eleva os catetos ao quadrado, soma-os e tira a raiz quadrada (elevando a 0.5)
hi = (catop**2 + catad**2)**0.5
print("A hipotenusa vai medir {:.2f}".format(hi))

from math import hypot
catop = float (input("Cateto oposto"))
catad = float (input("cateto adjacentes"))
hi = hypot(catop,catad)
print  ("A hipotenusa vai medir {}".format(hi))
