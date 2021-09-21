menorP = 0
maiorP = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}o. pessoa:'.format(c)))
    if c == 1:
        menorP = peso
        maiorP = peso
    else:
        if peso >= maiorP:
            maiorP = peso
        if peso <= menorP:
            menorP = peso

print('O maior peso foi:{}\n'
      'O menor peso foi:{}'.format(maiorP,menorP))

