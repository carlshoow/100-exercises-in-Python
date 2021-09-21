maisVelho = 0
media = 0
mulher20 = 0

for c in range(1,5):
    print('='*8,'{}o. Pessoa'.format(c),'='*8)
    nome = str(input('Nome:'.format(c)))
    idade = int(input('Idade:'.format(c)))
    sexo = str(input('Sexo [M/F]:'.format(c)))
    media += idade

    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

media = media / 4

print('A média de idade do grupo é {:.1f} anos\n'
      'O homem mais velho tem {} anos e se chama {}\n'
      'O total de mulheres com menos de 20 anos é {}'
      .format(media, maisVelho, nomeVelho, mulher20 ))
