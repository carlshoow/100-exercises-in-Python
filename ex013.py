print('-'*20)
print('Reajuste de Salario\n')
salario = float(input('Digite seu Salario:'))

novo = salario + (salario * (15/100))

print('-'*20)
print('Novo Salario Reajustado\n')
print('Seu reajuste foi de R${:.2f}, Novo Salario R${:.2f}'.format((salario*(15/100)), novo))


