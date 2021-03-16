n1 = int(input('Quantos dias alugados:'))
n2 = int(input('Quantos KM rodados:'))
x = (n1 * 60)
y = (n2 * 0.15)
print('Com {} dias alugados e {}Km percorridos, o preço final será R${:.2f}.'.format(n1, n2, x + y))




