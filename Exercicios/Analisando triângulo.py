print('=-=' * 30)
print('     ANALISADOR DE TRIÂNGULOS     ')
print('=-=' * 30)
print('''Digite o valor de três segmentos
e eu falarei se é possível formar um triângulo com eles!''')
print('-' * 1)
seg1 = float(input('Insira o valor do primeiro segmento: '))
seg2 = float(input('Insira o valor do segundo segmento: '))
seg3 = float(input('Insira o valor do terceiro segmento: '))
if seg1 >= seg2 + seg3 or seg2 >= seg1 + seg3 or seg3 >= seg1 + seg2:
    print('Não é possível formar um triângulo!')
else:
    print('É possível formar um triângulo!')
