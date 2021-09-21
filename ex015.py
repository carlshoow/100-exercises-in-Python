d = int(input('Digite quantos dias o carro foi alugado:'))
km = float(input('Digite quantos km rodados:'))

vP = (d * 60) + (km * 0.15)

print('Voce rodou {}km durante {} dias, Portanto valor a pagar sera de R${:.2f}'.format(km, d, vP))