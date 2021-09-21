print('-'*25)
print('TRABALHANDO COM STRINGS\n')

nome = str(input('Digite nome completo:'))

lista = nome.split()
print('Primeiro nome é {}\nUltimo nome é {}'.format(lista[0],lista[len(lista) - 1]))
