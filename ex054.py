from datetime import date
maior = 0
menor = 0
atual = date.today().year

for c in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}o. pessoa:'.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} Pessoas atingiram a maioridade\n'
      '{} Pessoas não atingiram a maioridade'.format(maior, menor))
