time20 = ('Palmeiras','Cruzeiro','Grêmio','Santos','Corinthians',
          'Flamengo','Atlético Mineiro','Athletico Paranaense','Internacional','Chapecoense',\
         'Botafogo','São Paulo','Fluminense','Vasco da Gama','Bahia',\
          'Sport','Vitória','Ponte Preta','América','Coritiba')

print(f'\033[1m\nOs times do brasileirao 2019 são {time20}\n')
print('=-='*200)
print(f'\033[1mOs cinco primeiros são {time20[:5]}\n')
print('=-='*200)
print(f'\033[1mOs quatro ultimos são {time20[16:20]}\n')
print('=-='*200)
print(f'\033[1mOs times do brasileirao em ordem Alfabetica {sorted(time20)}\n')
print('=-='*200)

print(f'\033[1mChapecó esta na {time20.index("Chapecoense") + 1} posição\n')
print('=-='*200)