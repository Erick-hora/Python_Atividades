pessoa = {}
dados = []
soma = mulheres = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite seu nome: '))
    pessoa['sexo'] = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]

    while pessoa['sexo'] not in 'FM':
        pessoa['sexo'] = str(input('ERRO! Digite seu sexo[M/F]: ')).strip().upper()[0]

    pessoa['idade'] = int(input('Digite sua idade: '))

    if pessoa['sexo'] == 'F':
        mulheres += 1

    soma += pessoa['idade']

    dados.append(pessoa.copy())

    c = ' '
    while c not in 'SN':
        c = str(input('Você gostaria de continuar? [S/N]: ')).strip().upper()[0]

    if c == 'N':
        break

print('-='*30)
print(f'A) Ao todo foram cadastradas {len(dados)} pessoas')
print(f'B) A média entre as idades foi de {soma/len(dados):5.2f}')

if mulheres > 0:
    print('C) As mulheres cadastradas foram: ', end=' ')
    for _pessoa in dados:
        if _pessoa['sexo'] == 'F':
            print(_pessoa['nome'], end=' ')
    print()

print(f'D) A lista de pessoas acima da média é: ')
for _pessoa in dados:
    if _pessoa['idade'] > soma/len(dados):
        print(f'Nome: {_pessoa['nome']}; Sexo: {_pessoa['sexo']}; Idade: {_pessoa['idade']};')
    print()
print('Encerrado...')
