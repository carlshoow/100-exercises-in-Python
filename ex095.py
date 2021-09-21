jogador = {}
gols = []
time = list()

while True:
    jogador['Nome'] = str(input('Nome do Jogador:')).strip()
    qtd = int(input('Jogou quantas partidas? '))
    for c in range(0,qtd):
        gols.append(int(input(f'Quantos gols na partida {c+1}?: ')))
    jogador['Gols'] = gols[:]
    jogador['Aproveitamento'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('Quer continuar [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Apenas S ou N ')

    if resp in 'N':
        break
print('-='*40)
print(f'{"  cod":>4}{"Nome":>14}{"Gols":>15}{"Total":>15}')
for c,jog in enumerate(time):
    print(f'{c:>4}',end='')
    for v in jog.values():
        print(f'{str(v):>15}',end='')
    print()

while True:
    while True:
        opc = int(input('Quer ver o desemepenho de qual jogador? [999 Encerra]'))
        if opc > len(time):
            print('Erro! Jogador nao encontrado!')
        elif opc <= len(time):
            break
    print('\033[1m-=' * 35)
    totp = len(time[opc]["Gols"])
    print(f'\033[mO jogardor {time[opc]["Nome"]} jogou {totp} jogos')
    for c in range(0, totp):
        print(f'  =>  Na partida {c}, fez {time[opc]["Gols"]} gols')
    print(f'\nO aproveitamento de {time[opc]["Nome"]} foi de {time[opc]["Aproveitamento"]} gols')






