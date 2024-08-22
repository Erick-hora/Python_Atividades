'''
Este código sorteia uma lista na ordem que os alunos realizaram as apresentações
'''
from random import shuffle
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))

alunos = [al1, al2, al3, al4]

shuffle(alunos)

print('A ordem decidida foi: {}'.format(alunos))

