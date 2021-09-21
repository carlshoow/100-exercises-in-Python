from datetime import date
atual = date.today().year

nasc = int(input('Digite ano de nascimento:'))

idade = atual - nasc
print('IDADE \033[4:33m{}\033[m ANOS'.format(idade))
if 0 < idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')

elif idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')

elif idade <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')

elif idade <= 25:
    print('CLASSIFICAÇÃO: SENIOR')

else:
    print('CLASSIFICAÇÃO: MASTER')