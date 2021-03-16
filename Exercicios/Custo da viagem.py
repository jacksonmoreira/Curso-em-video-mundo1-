# Cabeçalho
print('=-=' * 30)
print('     CUSTO DA VIAGEM     ')
print('=-=' *30)

# Informações
print('''Viagens de até 200km será cobrado R$0,50 por km.
Em viagens mais longas será cobrado R$0,45 por km.''')
print('-' * 15)

# Variáveis
va0 = float(input('Digite a distância da sua viagem: ').strip())
va1 = va0 * 0.50
va2 = va0 * 0.45

# Operações
print('-' * 15)
print('Você está prestes a começar uma viagem de {:.2f}km!'.format(va0))
if va1 <= 200:
    print('E o custo da viagem será de R${:.2f}!'.format(va1))
else:
    print('E o custo da viagem será de R${:.2f}!'.format(va2))
print('=-=' * 30)
