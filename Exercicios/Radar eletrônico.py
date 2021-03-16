print('=-' * 25)
print('     RADAR ELETRÔNICO     ')
print('-=' * 25)
print('''Limite máximo de velocidade: 80km/h.
Multa de R$7,00 por cada km  acima do limite.''')
print('-' * 15)
vel = int(input('Informe a velocidade atual o carro: '))
mul = (vel - 80) * 7
print('ANALISANDO...')
if vel > 80:
    print('Velocidade acima do limite, você será mutado em R${},00!'.format(mul))
else:
    print('Dirija com cuidado, tenha um bom dia!')
