from random import choice
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
al5 = str(input('Quinto aluno: '))

alunos = [al1, al2, al3, al4, al5]

print('O aluno escolhido foi: {}'.format(choice(alunos)))
