cores = {'amarelo':'\033[4:33m',
         'vermelho':'\033[1;31;40m',
         'limpa':'\033[m',
         'azul':'\033[;36;40m'}
print('\033[1;31m+=+'*10,'{}'.format(cores['limpa']))
print('{}LOJA CITUBO PISCINAS E BOMBAS{}'.format(cores['amarelo'],cores['limpa']))
print('\033[1;31m+=+'*10,'{}'.format(cores['limpa']))

prod = float(input('Digite o valor do produto:'))
print('\033[1;33m+=+'*10,'{}'.format(cores['limpa']))
print('ESCOLHA A FORMA DE PAGAMENTO')
print('\033[;36m[1]\033[m A VISTA DINHEIRO/CHEQUE\n'
      '\033[;36m[2]\033[m A VISTA NO CARTAO\n'
      '\033[;36m[3]\033[m A PRAZO NO CARTAO\n')


esc = int(input('Qual a forma de \033[;36mPAGAMENTO\033[m?'))

if esc == 1:
    desconto = prod * 10/100

    print('Voce tera 10% de desconto, valor final do produto R${}'.format(prod - desconto))
elif esc == 2:
    desconto = prod * 5/100
    print('Voce tera 5% de desconto, valor final do produto R${}'.format(prod - desconto))

elif esc == 3:
    esc = int(input('Em quantas parcelas ira pagar?'))
    if esc <= 2:
        print('Valor a pagar de R${} em 2x parcelas de R${}'.format(prod, prod/2))
    else:
        juros = prod + (prod * 20/100)
        print('Voce ira pagar um adicional de 20% juros\n'
              'Valor final do produto R${}, \n'
              'Valor das Parcelas R${}, Total de parcelas:{}'.format(juros, juros/esc, esc))
else:
    print('OPCÃO INVALIDA!')




