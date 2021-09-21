tot20 = 0
tot18 = 0
totH = 0

while True:
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]')).upper().strip()[0]
    print('-=-'*8)
    if idade >= 18:
        tot18 += 1
    if sexo in 'Mm':
        totH +=1
    if sexo in 'Ff' and idade < 20:
            tot20 += 1

    resp = str(input('Quer continuar[S/N]:')).strip().upper()[0]
    if resp in 'Nn':
        break

print(f'{tot18} pessoas acima de 18 anos\n'
      f'{totH} homens foram cadastrados\n'
      f'{tot20} mulheres abaixo de 20 anos')