numeros = (int(input('Digite o primeiro valor:')),
           int(input('Digite o primeiro valor:')),
           int(input('Digite o primeiro valor:')),
           int(input('Digite o primeiro valor:')),)

print('O numero 9 aparece {} vezes'.format(numeros.count(9)))
if 3 in numeros:
    print(f'O numero 3 aparece na posição {numeros.index(3)+1}')
else:
    print('O numero 3 nao foi digitado!')

print('Numeros pares foram ',end='')
for c in numeros:
    if c % 2 == 0:
        print(c,end=' ')
