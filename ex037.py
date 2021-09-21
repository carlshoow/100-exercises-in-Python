cores = {'amarelo':'\033[4:33m',
         'vermelho':'\033[1;31;40m',
         'limpa':'\033[m',
         'azul':'\033[;36;40m'}
print('\033[1;31m+=+'*4,'{}'.format(cores['limpa']))
print('{}CONVERSOR{}'.format(cores['amarelo'],cores['limpa']))
print('\033[1;31m+=+'*4,'{}'.format(cores['limpa']))

num = int(input('Digite um numero:'))
print('{}Digite{} {}[1]{} {}para converter o numero para BINARIO{}'
      .format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['azul'], cores['limpa']))
print('{}Digite{} {}[2]{} {}para converter o numero para OCTAL{}'
      .format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['azul'], cores['limpa']))
print('{}Digite{} {}[3]{} {}para converter o numero para HEXADECIMAL{}'
      .format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['azul'], cores['limpa']))

esc = int(input('\033[4:33mDigite a sua escolha:\033[m'))

if esc == 1:
    print('{} convertido para BINARIO fica: {}'.format(num,bin(num)[2:]))

elif esc == 2:
    print('{} convertido para OCTAL fica: {}'.format(num,oct(num)[2:]))

elif esc == 3:
    print('{} convertido para HEXADECIMAL fica: {}'.format(num,hex(num)[2:]))

else:
    print('{}ESCOLHA INVALIDA!{}'.format(cores['vermelho'],cores['limpa']))
