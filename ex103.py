def ficha(nome='',gols= ''):
    if nome.isalpha():
        if gols.isnumeric():
            return f'O jogador {nome.strip()} marcou {gols.strip()} gol(s) no campeonato!'
        else:
            return f'O jogador {nome.strip()} marcou 0 gol(s) no campeonato!'

    elif gols.isnumeric():
        return f'O jogador <desconhecido> marcou {gols.strip()} gol(s) no campeonato!'
    else:
        return f'O jogador <desconhecido> marcou 0 gol(s) no campeonato!'


nome = str(input('Nome do Jogador:'))
gols = str(input('Marcou quantos gols?:'))
print(ficha(nome,gols))