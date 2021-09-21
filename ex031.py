km = int(input('Digite a distancia da viagem em km:'))

if km >= 200:
    pagar = km * 0.45
    print('Voce ira pagar um total de {:.2f}'.format(pagar))

else:
    pagar = km * 0.50
    print('Voce ira pagar um total de {:.2f}'.format(pagar))

print('BOA VIAGEM...')
