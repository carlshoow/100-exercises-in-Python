mat = [[],[],[]]
aux = []
for c in range(0,3):
    for j in range(0,3):
        mat[c].append(int(input(f'Digite um valor [{c},{j}]')))
print('-='*30)
for a in range(0,3):
    for b in range(0,3):
        print(f'[{mat[a][b]:^4}]',end=' ')
    print()

