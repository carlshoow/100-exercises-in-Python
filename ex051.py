
print('='*40)
print('{:^40}'.format('PROGRESSAO ARITMETICA'))
print('='*40)

p1 = int(input('Primeiro termo da PA:'))
r = int(input('A razao da PA:'))

for x in range(1,11):
    print(p1, end=' ')
    p1 += r
    print(' -> ', end=' ')

print('Acabou')






          
