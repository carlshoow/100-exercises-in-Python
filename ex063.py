
soma = n = 0
num = int(input('[999 Para terminar] Digite um numero:'))

while num != 999:
    soma = num + soma
    n += 1
    num = int(input('[999 Para terminar] Digite um numero:'))
print('A soma foi de {}, com {} numeros digitados'.format(soma, n))