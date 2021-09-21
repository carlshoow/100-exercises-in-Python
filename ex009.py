print('='*10,' CONVERSOR DE MOEDA ','='*10)
print('-'*50)
real = float(input('Digite quantos reais deseja converter:'))
print('-'*50)
dolar = real / 5.17


print('\nCONVERTENDO...')
print('R${:.2f} convertidos em dolar são U${:.2f}'.format(real,dolar))

