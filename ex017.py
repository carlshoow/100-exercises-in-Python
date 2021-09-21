from math import hypot

cA = float(input('Digite o comprimento do Cateto Adjacente:'))
cO = float(input('Digite o comprimento do Cateto Oposto:'))

hip = hypot(cA, cO)
print('O comprimento da hipotenusa é de {:.2f}'.format(hip))
