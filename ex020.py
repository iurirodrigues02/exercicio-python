import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
aluno5 = str(input('Digite o nome do quinto aluno: '))

apresentação = [aluno1, aluno2, aluno3, aluno4, aluno5]

print('A ordem de apresentação será {}'.format(random.sample(apresentação, 5)))