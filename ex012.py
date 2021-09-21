prod = float(input('Digite o valor do produto:'))

desconto = prod * (5/100)
prod = prod - desconto

print('-'*30)
print('O produto teve um desconto 5%. Desconto de R${:.2f} Valor final de R${:.2f}'.format(desconto,prod))
