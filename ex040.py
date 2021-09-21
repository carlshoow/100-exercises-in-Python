nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2

if 7 <= media <= 10:
    print('APROVADO! Sua media foi {:.1f}'.format(media))
elif 7 > media >= 5:
    print('RECUPERAÇÃO! Sua media foi {:.1f}'.format(media))
else:
    print('REPROVADO! Sua media foi {:.1f}'.format(media))

