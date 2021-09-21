from datetime import date
ano = int(input('Que ano deseja calcular?\nPressione 0 para calcular ano atual:'))
if ano == 0:
    ano = date.today().year
if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
     print('{} ANO BISSEXTO!'.format(ano))

else:
    print('{} ANO NÃO É BISSEXTO'.format(ano))


