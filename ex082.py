lista = []
pares = []
impares = []
pos = 0
while True:
    lista.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
while pos < len(lista):
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
        pos += 1
    else:
        impares.append(lista[pos])
        pos +=1


print(f'A lista de numeros foi {lista}')
print(f'A lista com numeros pares {pares}')
print(f'A lista com numeros impares {impares}')