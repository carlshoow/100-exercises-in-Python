jogador = {}
jogador["Nome"] = str(input('Digite o nome do Jogador:'))
qtdPartidas = int(input('Digite quantas partidas jogou:'))
gols = []
for c in range(0, qtdPartidas):
    g = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(g)
jogador["Gols"] = gols[:]
jogador["Aproveitamento"] = sum(gols)
print('\033[1m-='*35)
print(jogador)
print('\033[1m-='*35)
for k,v in jogador.items():
    print(f'\033[mO campo {k} tem valor {v}')
print('\033[1m-='*35)
print(f'\033[mO jogardor {jogador["Nome"]} jogou {qtdPartidas} jogos')
for c in range(0,qtdPartidas):
    print(f'  =>  Na partida {c}, fez {jogador["Gols"][c]} gols')
print(f'\nO aproveitamento de {jogador["Nome"]} foi de {jogador["Aproveitamento"]} gols')

