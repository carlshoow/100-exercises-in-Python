from random import randint
from time import sleep

print('\033[1;36m-='*15,'\033[m')
print('{:=^40}'.format('\033[;;35m PEDRA,PAPEL,TESOURA,JA ! \033[m'))
print('\033[1;36m-='*15,'\033[m')

print('\033[;31m[1]\033[m Para escolher \033[1;31mPEDRA\033[m\n'
      '\033[;31m[2]\033[m Para escolher \033[1;31mPAPEL\033[m\n'
      '\033[;31m[3]\033[m Para escolher \033[1;31mTESOURA\033[m')

esc = int(input('Digite sua \033[1;31mESCOLHA:\033[m'))
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!')
sleep(2)
print('')

itens = ['PEDRA','PAPEL','TESOURA']

comp = randint(1,3)

if esc == comp:
    print('Deu empate, ninguem ganhou!')

#COMPARAÇAO DE PEDRA
elif (esc == 1 and comp == 2):
    print('Voce perdeu!')
elif (esc == 1 and comp == 3):
    print('Voce ganhou!')
#COMPARAÇAO PAPEL
elif (esc == 2 and comp == 3):
    print('Voce perdeu!')
elif (esc == 2 and comp == 1):
    print('Voce ganhou!')

#COMPARAÇAO TESOURA
elif (esc == 3 and comp == 1):
    print('Voce perdeu!')
elif (esc == 3 and comp == 2):
    print('Voce ganhou!')
else:
    print('Escolha Invalida!')

print('Jogador jogou {} e o Computador {}'.format(itens[esc-1], itens[comp-1]))



