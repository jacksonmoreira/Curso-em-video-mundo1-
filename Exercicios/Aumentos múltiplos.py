print('-=-' * 30)
print('     AUMENTOS MÚLTIPLOS     ')
print('-=-' * 30)
print('''Digite o seu salário e eu calcularei seu aumento.
Aumento de 10% para salários superiores a R$1250,00.
Aumento de 15% para salários inferiores ou iguais a R$1250,00. ''')
print('-' * 1)
sal0 = float(input('Digite o valor do seu salário! R$: '))
sals = sal0 * 10 / 100
sali = sal0 * 15 / 100
sa1 = sal0 + sals   
sa2 = sal0 + sali
if sal0 > 1250:
    print('O valor do aumento no seu salário de R${:.2f} foi de R${:.2f}!'.format(sal0, sals))
    print('Totalizando R${:.2f}!'.format(sa1))
if sal0 <= 1250:
    print('O valor do aumento no seu salário de R${:.2f} foi de R${:.2f}!'.format(sal0, sali))
    print('Totalizando R${:.2f}!'.format(sa2))
