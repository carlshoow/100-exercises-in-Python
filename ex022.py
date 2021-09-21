cores = {'amarelo':'\033[4:33m',
         'vermelho':'\033[31m',
         'limpa':'\033[m',
         'azul':'\033[34m'}

print('-'*25)
print('{}TRABALHANDO COM STRINGS{}\n'.format(cores['azul'],cores['limpa']))


nome = str(input('Digite seu nome completo:'))

print('{}Em maiusculas:{} {} '.format(cores['vermelho'], cores['limpa'],nome.upper()))
print('{}Em minusculas:{} {}'.format(cores['amarelo'],cores['limpa'],nome.lower()))

div = nome.split()
print('Nome dividido sem espacos {}{}{}'.format(cores['azul'],div,cores['limpa']))

print('Total {} sem espaços'.format(len("".join(div))) )

print('{} tem {} letras'.format(div[0],len(div[0])))


