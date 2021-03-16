from math import hypot
n1 = float(input('Insira o valor do cateto adjacente:'))
n2 = float(input('Insira o valor do cateto oposto:'))
h = hypot(n1, n2)
print('Com os catetos adjacentes e opostos sendo respectivamente', end=' ')
print('{} e {}, temos que o valor da hipotenusa é {:.1f}.'.format(n1, n2, h))


