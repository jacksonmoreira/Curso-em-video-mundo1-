frase = str(input('Escreva uma frase: ')).strip().upper()
print('-' * 45)
print('A letra "a" se repete {} vezes na sua frase.'.format(frase.count('A')))
print('Posiçao em que a letra "a" aparece pela primeira vez {}.'.format(frase.find('A') + 1))
print('Posição em que a letra "a" aparece pela última vez {}.'.format(frase.rfind('A') + 1))
print('-' * 45)

