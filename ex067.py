from time import sleep
while True:
    num = int(input('Quer ver qual tabuada mano? '))
    if num <= 0: break
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
    print(f'{"FIM":-^20}')
sleep(2)
print('\nFim do Programa [TABUADA]...')