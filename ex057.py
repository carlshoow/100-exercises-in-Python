s = str(input('Digite o seu sexo [M/F]:')).strip().upper()[0]


while (s != 'F') and (s != 'M'):
    s = str(input('Resposta invalida! Digite o seu sexo')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(s))




