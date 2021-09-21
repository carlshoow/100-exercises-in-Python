from random import randint
from time import sleep
sort = randint(0,5)

print('-+-'*10)
print('JOGO DA ADIVINHAÇÃO')
print('-+-'*10)
print()

num = int(input('Pensei em um numero entre 0 e 5. Tente adivinhar:'))

print('PROCESSANDO...')
sleep(3)
sort = randint(0,5)
if num == sort:
    print('PARABENS, VOCE ACERTOU. EU PENSEI EM {}'.format(sort))
else:
    print('QUE PENA, VOCE PERDEU. O NUMERO QUE PENSEI FOI {}'.format(sort))
