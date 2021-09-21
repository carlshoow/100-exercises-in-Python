l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))

custo = (l * a) / 2

print('Serao necessarios {:.2f} latas de tinta para pintar a parede de {:.2f}m2'.format(custo, l*a))
