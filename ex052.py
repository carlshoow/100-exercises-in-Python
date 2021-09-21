num = int(input('Digite um numero:'))
cont = 0
for c in range(1,num+1):

    if num % c == 0:
        print('\033[;31m{}'.format(c),end=' ')
        cont += 1
    else:
        print('\033[;33m{}'.format(c), end=' ')

if cont == 2:
    print('\n\033[m{} é Numero primo pois foi dividido apenas {}x'.format(num,cont))
else:
    print('\n\033[m{} Não é primo pois foi dividido {}x'.format(num,cont))


