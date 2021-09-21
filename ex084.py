cadastro = []
dado = []
resp = ''

while True:
    dado.append(str(input('Nome:')))
    dado.append(float(input('Peso:')))
    cadastro.append(dado[:])
    dado.clear()
    resp = str(input('Continua? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break

for pos, pessoa in enumerate(cadastro):
    if pos == 0:
        maiorP = pessoa[1]
        menorP = pessoa[1]
    else:
        if pessoa[1] > maiorP:
            maiorP = pessoa[1]

        if pessoa[1] < menorP:
            menorP = pessoa[1]
print(f'O total de pessoas cadastradas foi de {len(cadastro)}')
print(f'O maior peso foi {maiorP}Kg. Peso de ',end='')

for pos, pessoa in enumerate(cadastro):
    if pessoa[1] == maiorP:
        print(f'[{pessoa[0]}] ', end='')

print(f'\nO menor peso foi {menorP}Kg. Peso de',end='')
for pos, pessoa in enumerate(cadastro):
    if pessoa[1] == menorP:
        print(f'[{pessoa[0]}] ',end=' ')
print()

