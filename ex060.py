from math import factorial

fat = int(input('Digite um numero para calcular o fatorial:'))
#USANDO MODULO
'''print('(usando math) O fatorial de {} é {}'.format(fat, factorial(fat)))
'''

print('Calculando o fatorial de {}! = '.format(fat), end='')
#USANDO WHILE
'''f = 1
cont = fat
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f = f*cont
    cont -= 1
print(f)
'''
#USANDO FOR
f = 1
cont = fat
for c in range(cont, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c

print(f)
