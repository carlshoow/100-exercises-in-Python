cont = 'S'
media = tot = 0
while cont != 'N':
    num = int(input('Digite um numero:'))
    media+= num
    tot += 1
    if tot == 1:
        menor = num
        maior = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    cont = str(input('Quer continuar? [S/N]')).strip().upper()
    if cont != 'S' and cont != 'N':
        while cont != 'S' and cont != 'N':
            cont = str(input('Resposta invalida!Responda [S/N]'))
media = media / tot
print('Voce digitou {} numeros\n'
      'A média foi {:.2f}\n'
      'O menor foi {}\n'
      'O maior foi {}'.format(tot,media,menor,maior))

