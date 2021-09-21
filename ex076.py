produtos = ('Feijao', 6.55, 'Arroz', 8.75, 'Leite', 2.75, 'Iogurte', 4.55,'Tomate', 2.25, 'Cebola', 4.20)
print('='*50)
print(f'{"Supermercado Tenditudo":^45}')
print('='*50)
for cont in range(0,len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<30}',end=" ")
    else:
        print(f'R${produtos[cont]:>7.2f}')