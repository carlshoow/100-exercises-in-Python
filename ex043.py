peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura em metros:'))

imc = peso / pow(altura,2)

if imc < 18.5:
    print('IMC:{:.2f}, ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC:{:.2f} PESO NORMAL'.format(imc))
elif imc >=25 and imc < 30:
    print('IMC:{:.2f} ACIMA DO PESO'.format(imc))
else:
    print('IMC:{:.2f} OBESIDADE'.format(imc))