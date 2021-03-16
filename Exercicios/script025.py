import math
an = float(input('Digite o valor do ângulo:'))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('Com o ângulo {}°, temos seno, cosseno e tangente'.format(an), end=' ')
print('respectivamente no valor de {}, {:.2f}, {:.2f}.'.format(an, se, co, ta))










