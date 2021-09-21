cores = {'amarelo':'\033[4:33m',
         'vermelho':'\033[1;31;40m',
         'limpa':'\033[m',
         'azul':'\033[;36;40m'}
print('\033[1;31m+=+'*8,'{}'.format(cores['limpa']))
print('{}SIMULADOR DE EMPRESTIMO{}'.format(cores['amarelo'],cores['limpa']))
print('\033[1;31m+=+'*8,'{}'.format(cores['limpa']))

vCasa = float(input('Digite o valor da casa:'))
sal = float(input('Digite o seu salario:'))
par = int(input('Digite em quantos anos ira pagar:'))

valPar = (vCasa / par) / 12

if valPar > (sal * 30/100):
    print('\033[1;31;40mEMPRESTIMO NEGADO!\033[m')

else:
    print('\033[1;33;40mEMPRESTIMO APROVADO!\033[m')


