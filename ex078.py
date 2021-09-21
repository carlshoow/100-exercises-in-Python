numeros = []
for c in range(0, 5):
    numeros.append(int(input('Digite um valor:')))
maior = max(numeros)
menor = min(numeros)

print(f'Você digitou :{numeros}')
print(f'O maior foi {maior} nas posições ', end='')
#Percorrer a lista e se existir valores duplicados vai dar print na posiçao
for pos, valor in enumerate(numeros):
    if valor == maior:
        print(f'{pos}...',end=' ')

print(f'\nO menor foi {menor} nas posições ', end='')
#Percorrer a lista e se existir valores duplicados vai dar print na posiçao
for pos, valor in enumerate(numeros):
    if valor == menor:
        print(f'{pos}...',end=' ')