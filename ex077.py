palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON', 'CURSO','GRATIS','ESTUDAR','PRATICAR',
            'TRABALHAR','MERCADO','PROGRAMADOR','EDUCAÇÃO','ÍNDICE')

#Usa-se um for para analisar os elementos da tupla por indice ex: p[1] = 'APRENDER'
for p in palavras:

    print(f'\nNa palavra {p} tem ',end=' ')
#Usa-se outro for para analisar o conteudo de cada indice ex: letra[1] = 'A' de 'APRENDER'
    for letra in p:
        if letra in 'AÃÁÂEÉÈÊÍIÌOÕÓUÚ':
            print(letra,end=' ')
