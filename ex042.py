r1 = int(input('Digite o primeiro segmento de reta:'))
r2 = int(input('Digite o segundo segmento de reta:'))
r3 = int(input('Digite o terceiro segmento de reta:'))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('As retas formam um triangulo!')

    if r1 == r2 and r2 == r3:
        print('TRIANGULO EQUILATERO')
    elif (r1 != r2 and r1 != r3):
        print('TRIANGULO ESCALENO')
    else:
        print('TRIANGULO ISOCELES')
else:
    print('As retas nao formam um triangulo!')



