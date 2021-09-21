expressão = str(input('Digite uma expressão:'))

parenteses = []

for simbolo in expressão:

    if simbolo == '(':
        parenteses.append('(')
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('Expressão Valida')
else:
    print('Expressão invalida')
