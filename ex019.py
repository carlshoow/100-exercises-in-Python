import random

a1 = str(input('Digite o nome do 1 aluno:'))
a2 = str(input('Digite o nome do 2 aluno:'))
a3 = str(input('Digite o nome do 3 aluno:'))
a4 = str(input('Digite o nome do 4 aluno:'))

sorteado = random.choice((a1,a2,a3,a4))

print('O sorteado para limpar o quadro foi {}'.format(sorteado))

