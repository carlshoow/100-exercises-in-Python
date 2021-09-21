from datetime import date

cores = {'amarelo':'\033[4:33m',
         'vermelho':'\033[1;31;40m',
         'limpa':'\033[m',
         'azul':'\033[;36;40m'}
print('\033[1;31m+=+'*10,'{}'.format(cores['limpa']))
print('{}ALISTAMENTO MILITAR{}'.format(cores['amarelo'],cores['limpa']))
print('\033[1;31m+=+'*10,'{}'.format(cores['limpa']))


nasc = int(input('Digite em que ano você nasceu:'))
idade = date.today().year - nasc

if idade == 18:
    print('Voce tem {} anos e deve se alistar imediatamente!'.format(idade))

elif idade < 18:
    print('Voce tem {} anos, ano de alistamento sera em {} anos, {}'.format(idade, 18 - idade, date.today().year + (18 - idade)))

else:
    print('Voce tem {} anos e deveria ter se alistado há {} anos, em {}'.format(idade, idade - 18, date.today().year - (idade - 18)))


