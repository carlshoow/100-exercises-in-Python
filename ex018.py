from math import sin, cos, tan, radians

a = float(input('Digite um angulo :'))

seno = radians(a)
cosseno = radians(a)
tangente = radians(a)

print('O Seno de {} = {:.2f}'.format(a, sin(seno)))
print('O Cosseno de {} = {:.2f}'.format(a, cos(cosseno)))
print('A Tangente de {} = {:.2f}'.format(a, tan(tangente)))
