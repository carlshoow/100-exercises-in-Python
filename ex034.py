salario = float(input('Digite o salario:'))

if salario > 1250:
    salario = salario + (salario * 10/100)
    print('Salario tera reajuste de 10%, ficando entao R${}'.format(salario))

else:
   salario = salario + (salario * 15 / 100)
   print('Salario tera reajuste de 15%, ficando entao R${}'.format(salario))