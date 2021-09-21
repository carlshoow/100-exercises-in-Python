
qtdFibo = int(input('Digite quantos elementos de fibo deseja ver:'))

n1 = 0
n2 = 1
c = 3
if qtdFibo != 0:
    print(n1,'->',n2,end=' ')

while c <= qtdFibo:
    fibo = n1 + n2
    print('->',fibo,end=' ')
    n1 = n2
    n2 = fibo

    c += 1
print('FIM')