num0 = int(input('Digite um número: '))
num2 = num0 // 1 % 10
num3 = num0 // 10 % 10
num4 = num0 // 100 % 10
num5 = num0 // 1000 % 10
print('-' * 35)
print('Analisando o número {}...'.format(num0))
print('Unidade: {}.'.format(num2))
print('Dezena: {}.'.format(num3))
print('Centena: {}.'.format(num4))
print('Milhar: {}.'.format(num5))
print('Número analisado com sucesso!')
print('-' * 35)

