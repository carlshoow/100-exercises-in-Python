from random import randint



comp = randint(0,10)
dicas = 0
tent = 0
acertou = False
while not acertou:

    esc = int(input('Pensei em um numero de \033[31m0 - 10\033[m \n'
                    'Qual o seu palpite?'))
    tent += 1
    if esc == comp:
        acertou = True
    else:
        if esc < comp:
            print('\nMaior... Tente outra vez')
        else:
            print('\nMenos..., Tente outra vez')

print('\nParabens voce acertou! Eu pensei no numero {}'.format(comp))
print('Voce precisou de {} tentativas para acertar'.format(tent))