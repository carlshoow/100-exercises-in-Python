lista = [[],[]]
for c in range(0,7):
    aux = int(input(f'Digite {c+1} valor:'))
    if aux % 2 == 0:
        lista[0].append(aux)
    else:
        lista[1].append(aux)
print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')