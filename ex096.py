def area(l,c):

    a = l*c
    print(f'O terreno {l}m x {c}m tem area de {a:.1f} m2')



print('-'*20)
print('Controle de terrenos')
print('-'*20)
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
area(l,c)
