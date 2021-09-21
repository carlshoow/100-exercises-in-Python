matriz = [[1,2,3],[4,5,6],[7,8,9]]
somaPar = soma3C = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor[{l}][{c}]:'))

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            soma3C += matriz[l][c]
        if l == 1:
            if c == 0:
                maior2L = matriz[1][c]
            else:
                if matriz[1][c] > maior2L:
                    maior2L = matriz[1][c]
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]',end=' ')
    print()

print('-='*30)
print(f'A soma dos pares é {somaPar}')
print(f'A soma da terceira coluna é {soma3C}')
print(f'O maior da segunda linha é {maior2L}')
