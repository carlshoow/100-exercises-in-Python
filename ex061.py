pTermo = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razao da PA:'))
termo = pTermo
cont = 1
total = 0
aux = 10
tott = 0
while aux != 0:
    total = aux + total
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += r
        cont +=1
        tott += 1
    print('PAUSA')
    aux = int(input('Quer ver mais quantos termos? '))


print('Fim! {} termos de uma PA'.format(tott))