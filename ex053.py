p = str(input('Digite alguma coisa:')).strip().upper()
palavra = p.split()
junta = "".join(palavra)
inverso = ''
for c in range(len(junta)-1,-1,-1):
    inverso += junta[c]

print('O inverso de {} é {}'.format(inverso, junta))
if inverso == junta:
    print('Formam um Palindromo!')
else:
    print('Não forma palindromo')



