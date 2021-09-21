lista = []
resp = ''
while True:
    num = int(input('Digite um valor:'))
    if num not in lista:
        lista.append(num)
        print('Numero adicionado...')
    elif num in lista:
        print('Valor duplicado... Nao vou adicionar')

    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(sorted(lista))