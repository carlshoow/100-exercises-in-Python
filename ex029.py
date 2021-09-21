v = int(input('Qual a velocidade do carro:'))

if v > 80:
    multa = (v - 80) * 7.00
    print('Voce passou da velocidade permitida. Tera de pagar uma multa de R${:.2f}'.format(multa))

print('Tenha um bom dia!')

