from time import sleep
n1 = int(input('\nDigite um valor:'))
n2 = int(input('Digite outro valor:'))


sair = False

while not sair:

    print('\n{:=^25}'.format('MENU'))
    print('\n[1] para fazer a soma\n'
          '[2] para multiplicar\n'
          '[3] para ver o maior\n'
          '[4] para novos valores\n'
          '[5] para sair')
    esc = int(input('>>>Digite sua escolha:'))

    if esc == 1:
        print('A soma {} + {} = {}'.format(n1, n2, n1+n2))
    elif esc == 2:
        print('A multiplicação {} x {} = {}'.format(n1,n2, n1*n2))
    elif esc == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    elif esc == 4:

        n1 = int(input('\nDigite um valor:'))
        n2 = int(input('Digite outro valor:'))

    elif esc == 5:
        sair = True


    else:
        print('Escolha invalida')
sleep(2)
print('Fim do programa!')