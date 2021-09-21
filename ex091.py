from random import randint
from time import sleep
from operator import itemgetter
D = {'jogador1':randint(1,6),
     'jogador2':randint(1,6),
     'jogador3':randint(1,6),
     'jogador4':randint(1,6)}
aux = list()
for k, v in D.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado.')

print('-='*20)
print(f'{"==RANKING DOS JOGADORES==":^35}')

aux = sorted(D.items(), key=itemgetter(1), reverse=True)
pos = 1
for k, v in enumerate(aux):
    print(f'   {k+1}o. Lugar : {v[0]} com {v[1]}')

