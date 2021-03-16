from random import random
n1 = str(input('Insira o nome do aluno: '))
n2 = str(input('Insira o nome do aluno: '))
n3 = str(input('Insira o nome do aluno: '))
n4 = str(input('Insira o nome do aluno: '))
li = [n1, n2, n3, n4]
print('O SORTEADO FOI {}.'.format(random(li)))
