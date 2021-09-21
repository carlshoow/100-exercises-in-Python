def sortear(numeros):
    from random import randint

    for c in range(0,5):
        numeros.append(randint(0,10))
    print(f'Os numeros sorteados foram {numeros}')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares da lista {lista} foi {soma}')


#Programa Principal
numeros = []
sortear(numeros)
somaPar(numeros)
