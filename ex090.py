dic = {}
dic['nome'] = str(input('Nome do aluno:'))
dic['media'] = float(input('Média do aluno:'))
if dic['media'] >= 7:
    dic['situação'] = 'Aprovado'
elif 5 >= dic['media'] < 7:
    dic['situação'] = 'Em Recuperação'
else:
    dic['situação'] = 'Reprovado'

print('-='*14)
for k, v in dic.items():
    print(f'  -  {k} é {v}')