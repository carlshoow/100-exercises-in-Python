pessoa = {}
grupo =[]
mediaIdade = 0
#INICIO DE CADASTRO
while True:
    #CADASTRO DE UMA PESSOA
    pessoa["NOME"] = str(input('Nome:')).strip()
    while True:
        pessoa["SEXO"] = str(input('Sexo[M/F]')).strip().upper()[0]
        if pessoa["SEXO"] in 'MF':
            break
        print('Erro! Digite apenas [M] ou [F]')

    pessoa["IDADE"] = int(input('Idade:'))
    mediaIdade += pessoa["IDADE"]

    #ALOCAÇÃO DE UMA PESSOA EM UMA LISTA
    grupo.append(pessoa.copy())

    while True:
        resp = str(input('Continua?[S/N]')).strip().upper()
        if resp in 'SN':
            break
        print('Erro! Digite apenas [S] ou [N]')
#FIM CADASTRO
    if resp in "N":
        break
mediaIdade = mediaIdade / len(grupo)    #CALCULO DE IDADE MÉDIA DE PESSOAS CADASTRADAS

#INICIO DE RESULTADOS NA TELA
print('-='*30)
print(f'A) Foram cadastradas {len(grupo)} pessoas')
print(f'B) A média de idade foi {mediaIdade:.2f}')
print(f'C) As mulheres cadastradas foram ',end='')
for p in grupo:
    if p["SEXO"] in "F":
        print(f'{mulheres[c]} ', end='')
print()
print(f'D) As pessoas acima da idade média do grupo foram ')
for p in grupo:
    if p["IDADE"] >= mediaIdade:
        for k,v in c.items():
            print(f'    => {k}: {v:}; ',end='')
        print()