def maior(* lst):
    print('~~'*15)
    print('Analisando os valores passados...')
    print(f'Foram passados {len(lst)} valores')
    if len(lst) > 0:
        for c in range(0,len(lst)):
            print(f'{lst[c]} ',end='')

        for c in range(0,len(lst)):
            if c == 0:
                maior = lst[c]
            else:
                if lst[c] > maior:
                    maior = lst[c]
        print(f'\nO maior valor foi {maior}')
    else:
        print('O maior valor foi 0')

#Programa principal
maior(0,4,5,7,1)
maior(0,4,3,7,8,3)
maior(5,3,8,9,11,2,3)
maior()


