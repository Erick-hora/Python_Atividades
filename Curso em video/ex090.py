aluno = {'nome': '', 'media': 0, 'situação': ''}

aluno['nome'] = str(input('Informe o nome: '))
aluno['media'] = float(input('Informe a sua nota: '))

if (aluno['media'] >= 7):
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'Nome da aluno: {aluno["nome"]}')
print(f'Sua media foi: {aluno["media"]}')
print(f'Sua media foi: {aluno["situação"]}')
