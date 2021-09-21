l1 = int(input('Digite o primeiro seguimento de reta:'))
l2 = int(input('Digite o segundo seguimento de reta'))
l3 = int(input('Digite o terceiro seguimento  de reta:'))

if (l1 < l2+l3) and (l2 < l1+l3) and (l3 < l2+l1):
    print('É UM TRIANGULO')
else:
    print('Não é um triangulo')