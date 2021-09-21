print('-'*15)
print(f'{"Banco America":^16}')
print('-'*15)
saque = float(input('Quanto deseja sacar? '))
total = saque
totced = 0
ced = 50

while True:
    while total >= ced:
            total -= ced
            totced += 1

    print(f'Total de {totced} de R${ced}')
    if total >= 40:
        ced = 20
    elif total >= 20:
        ced = 20
    elif total >= 10:
        ced = 10
    elif total >= 1:
        ced = 1
    else:
        ced = 0
        break
    totced = 0



