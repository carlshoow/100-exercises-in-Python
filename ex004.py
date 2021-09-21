valor = input('Digite algo:')

print('Variavel do tipo {}'.format(type(valor)))
print('A variavel é maiuscula?',valor.isupper())
print('O que foi digitado é letra? ',valor.isalpha())
print('O que voce digitou é numero? ',valor.isnumeric())
print('O que voce digitou é letra e numero?', valor.isalnum())
print('O que voce digitou é minuscula? ',valor.islower())
