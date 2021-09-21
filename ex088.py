from random import randint
from time import sleep

print('=' * 35)
print(f'\033[1m{"JOGOS DA MEGA SENA":^30}\033[m')
print('=' * 35)
# Declaração de listas, lista maisJogos é o maximo de numeros que vou querer
jogos = []
maisJogos = [1, 2, 3, 4, 5, 6]

# Inicialização de quantas linhas na matriz vou querer
qtdJogos = int(input('Quantos jogos irá fazer?'))
for c in range(0, qtdJogos):
    jogos.append(maisJogos[:])

for l in range(0, 6):
    for c in range(0, qtdJogos):
        num = randint(1, 60)
        while num in jogos[c]:
            num = randint(1,60)
        jogos[c][l] = num


print('=' * 35)
print(f'SORTEANDO {qtdJogos} JOGO(s)')
for pos, c in enumerate(jogos):
    c.sort()
    print(f'{pos+1}o. jogo: {c}')
    sleep(0.75)
print(f'{"BOA SORTE!":-^35}')