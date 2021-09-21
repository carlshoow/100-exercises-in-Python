def contador(i, f, p):
    from time import sleep
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='',flush=False)
            cont += p
            sleep(0.5)
        print()
        print('-'*30)
    else:
        if i > f:
            cont = i
        while cont >= f:
            print(f'{cont} ', end='',flush=False)
            cont -= p
            sleep(0.5)
        print()
        print('-'*30)

#PROGRAMA PRINCIPAL
contador(0, 10, 1)
contador(10, 0, 1)
print('Agora é sua vez de definir o contador!')
inicio = int(input('Inicio:'))
fim = int(input('Fim'))
passo = int(input('Passo:'))
contador(inicio,fim,passo)
print()
