soma = 0
cont = 0
for c in range(0,501,3):
        if c % 2 == 1:
            soma += c
            cont += 1

print('A soma dos {} valores é {}'.format(soma,cont))
