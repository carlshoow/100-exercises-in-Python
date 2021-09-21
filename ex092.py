from datetime import date
atual = date.today().year
cadastro = {}
cadastro['NOME'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
cartrab = int(input('Carteira de trabalho [0 para sem carteira]:'))

if cartrab > 0:
    cadastro['IDADE'] = idade
    cadastro['CTPS'] = cartrab
    cadastro['CONTRATAÇÃO'] = int(input('Ano de contratação:'))
    cadastro['SALARIO'] = float(input('Salario: R$ '))
    cadastro['APOSENTADORIA'] = (cadastro['CONTRATAÇÃO'] - nasc) + 35
else:
   cadastro['IDADE'] = idade
   cadastro['CTPS'] = 0

for k, v in cadastro.items():
        print(f'   - {k} tem o valor {v}')
