def voto(nasc=0):
    """
    Programa que analisa data de nascimento e retorna se pode ou não votar
    :param nasc: Nascimento passado como parametro
    :return: Retorna um print com a analise
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade > 180:
        return f'Ano de nascimento INVALIDO!'
    print('~~'*20)
    if idade == 16 or idade == 17 or idade >= 70:
        return f'Idade {idade} anos. VOTO Opcional!'
    if idade < 16:
        return f'Idade {idade} anos. VOTO Negado!'
    if idade >= 18 < 70:
        return f'Idade {idade} anos. VOTO Obrigatório!'


#Programa Principal
nascimento = int(input('Digite a data de nascimento:'))
print(voto(nascimento))

