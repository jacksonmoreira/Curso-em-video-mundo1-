from datetime import date
print('-=-' * 30)
print('     ANO BISSEXTO      ')
print('-=-' * 30)
print('''Digite um ano qualquer
e eu irei dizer se ele é bissexto ou não.''')
print('-' * 15)
ano0 = int(input('Que ano quer analisar? Coloque 0 para saber o ano atual: '))
if ano0 == 0:
    ano0 = date.today().year
if ano0 % 4 == 0 and ano0 % 100 != 0 or ano0 % 400 == 0:
    print('O ano {} é bissexto!'.format(ano0))
else:
    print('O ano {} não é bissexto!'.format(ano0))
print('-=-' * 30)
