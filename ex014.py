from time import sleep

print('-'*20)
cores = {'amarelo':'\033[4:33m',
         'vermelho':'\033[31m',
         'limpa':'\033[m',
         'azul':'\033[34m'}

print('{}CONVERSOR DE TEMPERATURAS{}\n'.format(cores['amarelo'], cores['limpa']))

tempC = float(input('{}Digite uma temperatura em {}Celsius{}:'.format(cores['azul'],cores['vermelho'], cores['limpa'])))

fah = tempC * 1.8 + 32

print('CONVERTENDO...')
sleep(1)
print('{:.1f}ºC são {:.1f}ºF'.format(tempC, fah))