from random import randint
vit = 0

ganhador = ''
while True:
    computador = randint(0, 10)
    jogadorN = int(input('Digite um valor:'))
    jogadorE = str(input('PAR ou IMPAR [P/I]')).strip().upper()[0]
    while jogadorE != 'P' and jogadorE != 'I':
        jogadorE = str(input('PAR ou IMPAR [P/I]')).strip().upper()[0]
    soma = jogadorN + computador

    if (soma) % 2 == 0:
        ganhador = 'P'
        if jogadorE == 'P':
            print('=-='*8)
            print(f'{jogadorN} + {computador} = {soma}\nJogador escolheu PAR e ganhou!\nVamos denovo...')
            vit += 1
        else:
            print('=-=' * 8)
            print(f'{jogadorN} + {computador} = {soma}\nJogador escolheu IMPAR e perdeu!')
            break
    else:
        ganhador = 'I'
        if jogadorE == 'I':
            print('=-=' * 8)
            print(f'{jogadorN} + {computador} = {soma}\nJogador escolheu IMPAR e ganhou!\nVamos denovo...')
            vit += 1
        else:
            print('=-=' * 8)
            print(f'{jogadorN} + {computador} = {soma}\nJogador escolheu PAR e perdeu!')
            break

print('-'*8,'\nGAME OVER...\n'
            'Vitorias consecutivas {}'.format(vit))


