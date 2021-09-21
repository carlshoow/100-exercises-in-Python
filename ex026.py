print('-'*25)
print('TRABALHANDO COM STRINGS\n')

frase = str(input('Digite uma frase ou texto:')).strip()

print('Existe {} letras "a" na frase'.format(frase.lower().count('a')))

print('A letra "a" aparece na {} posicao da string'.format(frase.lower().find('a')+1))

print('A ultima letra "a" esta na posicao {} da string'.format(frase.lower().rfind('a')+1))