# Libs
from random import randint

# Cabeçalho
print('#' * 29)
print('     JOGO DA ADIVINHAÇÃO     ')
print('#' * 29)

# Informações
print('-' * 15)
print('''Esse é o jogo da adivinhação, eu vou
pensar em um número inteiro de 0 a 5, mas,
você terá que adivinhar em que número eu pensei.
VAMOS LÁ?''')
print('-' * 15)

# Variáveis
print('Começando jogo...')
num1 = int(input('Digite o número em que eu estou pensando: ').strip())
ale = randint(0, 5)

# Operações
print('Vocẽ acha que eu estava pensando no número {}, vamos ver se você está correto.'.format(num1))
print('-' * 15)
print('O número em que eu estava pensando é {}.'.format(ale))
print('-' * 15)
if num1 == ale:
    print('PARABÉNS, você adivinhou o número que eu estava pensando!')
else:
    print('Errou, esse não era o número em que eu estava pensando!')
    print('Tente novamente, quem sabe você acerta.')
print('#' * 29)
print('---FIM DE JOGO---')
print('#' * 29)
