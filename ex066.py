soma = n = 0
while True:
    num = int(input('[999 Para terminar] Digite um numero:'))
    if num == 999:
        break
    soma = num + soma
    n += 1

print('A soma foi de {}, com {} numeros digitados'.format(soma, n))