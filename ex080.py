lista = []
for c in range(0,5):
    valor = int(input('Digite um valor:'))

    if c == 0:
        lista.append(valor)
        print('Valor inserido na Ultima posição')
    elif valor > lista[-1]:
        lista.append(valor)
        print('Valor inserido na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if lista[pos] > valor:
                lista.insert(pos, valor)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1

print('-'*8)
print(lista)




