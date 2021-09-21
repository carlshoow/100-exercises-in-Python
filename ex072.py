ext = 'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', \
      'Seis', 'Sete', 'Oito', 'Nove', 'Dez', \
      'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', \
      'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
resp = ' '
while resp not in 'Nn':

    while True:
        valor = int(input('Digite um valor de 0 - 20:'))
        if 0 <= valor <= 20:
            break
        else:print('Tente novamente...', end=' ')
    print(f'O numero {valor} por extenso é {ext[valor]}')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

print('FIM DO PROGRAMA!')