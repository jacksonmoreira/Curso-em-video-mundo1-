# Cabeçalho
print('-=-' * 25)
print('    PAR OU ÍMPAR    ')
print('-=-' * 25)

# Informações
print('''Digite um número inteiro
e eu falarei se ele é par ou ímpar.''')

# Variáveis
print('-' * 25)
num = int(input('Digite qualquer número: '))
print('-' * 25)

# Operações
print('O seu número é {}, e ele é:'.format(num))
if num % 2 == 0:
    print('O seu número é par!')
else:
    print('O seu número é ímpar!')
