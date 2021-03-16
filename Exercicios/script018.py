n1 = float(input('Largura da parede:'))
n2 = float(input('Altura da parede:'))
a = n1 * n2
t = a / 2
print('As dimensões da parede são {}x{}, e sua área é {}m²'.format(n1, n2, a))
print('-' * 15)
print('Você precisará de {} litros de tinta para pintar a parede.'.format(t))



