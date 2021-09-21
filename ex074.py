from random import randint
tupla = tuple()
for c in range(0,15):
    tupla += randint(0,100),

print(f'O valores gerados foi {tupla}')
print(f'O maior foi {max(tupla)}')
print(f'O menor foi {min(tupla)}')