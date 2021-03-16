print('-=-' * 30)
print('    MAIOR E MENOR VALORES     ')
print('-=-' * 30)
print('''Digite 3 números e eu falarei
qual o maior e qual o menor.''')
print('-' * 1)
num1 = int(input('Digite o primeiro número: ').strip())
print('-' * 1)
num2 = int(input('Digite o segundo número: ').strip())
print('-' * 1)
num3 = int(input('Digite o terceiro número: ').strip())
if num1 > num2 and num1 > num3:
    print('O maior número é {}!'.format(num1))
if num2 > num1 and num2 > num3:
    print('O maior número é {}!'.format(num2))
if num3 > num1 and num3 > num2:
    print('O maior número é {}!'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor número é {}!'.format(num1))
if num2 < num1 and num2 < num3: 
    print('O menor número é {}!'.format(num2))
if num3 < num1 and num3 < num2:
    print('O menor número é {}!'.format(num3))
print('-=-' * 30)
