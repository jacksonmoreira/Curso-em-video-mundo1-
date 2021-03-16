n1 = float(input('Insira o salário do funcionário para ser calculado o aumento. R$:'))
n = n1 + (n1 * 15 / 100)
print('O salário do funcionário passará de R${} para R${} com um reajuste salarial de 15%.'.format(n1, n))
