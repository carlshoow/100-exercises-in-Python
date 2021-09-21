lista = []
resp = ''
while True:
    lista.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break

lista.sort(reverse=True)
print('=-='*10)
print(f'Foram digitados {len(lista)} numeros')
print(f'A lista em ordem decrescente foi {lista}')
print('O valor 5 foi digitado' if 5 in lista else 'O valor 5 nao esta na lista')

