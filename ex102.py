def fatorial(num, show=False):
    """
    Calculo de fatorial
    :param num: Valor a ser realizado o fatorial
    :param show: (Opcional) Se True, mostra na tela ex: 6x5x4x3x2x1
    :return: retorna o calculo do fatorial na variavel (f)
    """
    f = 1
    while num > 0:
        if show:
            if num == 1:
                print(f'{num} = ', end='')
            else:
                print(f'{num} x ', end='')
        f = f * num
        num -= 1
    return f


# PROGRAMA PRINCIPAL
print(fatorial(8, True))
