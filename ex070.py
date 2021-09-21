print('-=-' * 13)
print(f'{"LOJA SUPER BARATAO":^30}')
print('-=-' * 13)
caro1000 = valorTotal = cont = 0


while True:
    prod = str(input('Produto:'))
    val = float(input('Valor Produto R$ '))
    cont +=1
    valorTotal += val
    if cont == 1 or val < barato:
        barato = val
        nomeB = prod
    if val >= 1000:
        caro1000 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nQuer continuar [S/N]: ')).strip().upper()
    print()
    if resp in 'Nn': break

print(f'{"FIM DO PROGRAMA":-^20}')
print(f'O valor total da sua compra foi de R${valorTotal:.2f}\n'
      f'O produto mais barato foi {nomeB} que custa R$ {barato}\n'
      f'{caro1000} produtos custaram acima de R$1000')

