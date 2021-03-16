from random import sample
al1 = str(input('Insira o nome do aluno:'))
al2 = str(input('Insira o nome do aluno:'))
al3 = str(input('Insira o nome do aluno:'))
al4 = str(input('Insira o nome do aluno:'))
lis = [al1, al2, al3, al4]
sor = sample(lis, k=4)
print('A ordem dos sorteados foi: {}.'.format(sor))









