cores = {'amarelo':'\033[4:33m',
         'vermelho':'\033[1;31;40m',
         'limpa':'\033[m',
         'azul':'\033[;36;40m'}
print('\033[1;31m+=+'*10,'{}'.format(cores['limpa']))
print('{}MOSTRAR O MAIOR DE 2 NUMEROS{}'.format(cores['amarelo'],cores['limpa']))
print('\033[1;31m+=+'*10,'{}'.format(cores['limpa']))

num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))

if num1 > num2:
    print('{}{}{} é o {}MAIOR{}!'.format(cores['azul'], num1, cores['limpa'], cores['amarelo'],cores['limpa']))
elif num2 > num1:
    print('{}{}{} é o {}MAIOR!{}'.format(cores['azul'], num2, cores['limpa'],cores['amarelo'], cores['limpa']))
else:
    print('{}{} = {}{}, {}VALORES IGUAIS{}'.format(cores['vermelho'], num1, num2, cores['limpa'], cores['amarelo'], cores['limpa']))