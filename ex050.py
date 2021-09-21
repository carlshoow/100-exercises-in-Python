soma = 0

for c in range(1, 7):
    num = int(input('Digite [{}] valor:'.format(c)))
    if num % 2 == 0:
        soma += num

print('A soma dos numeros pares é: {}'.format(soma))