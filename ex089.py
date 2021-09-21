alunos = list()
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1+nota2) / 2
    alunos.append([nome,[nota1,nota2],media])
    resp = str(input('Continua[S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*20)
print(f'{"No.":<4}{"Nome":<10}{"Média":<24}')
for pos, al in enumerate(alunos):
    print(f'{pos:<4}{al[0]:<10}{al[2]:<25}')
while True:
    esc = int(input('Deseja ver as notas de qual aluno? [999 Encerra]'))
    if esc == 999:
        print('Encerrando...')
        break
    print(f'As notas do aluno {alunos[esc][0]} foram {alunos[esc][1]}')





