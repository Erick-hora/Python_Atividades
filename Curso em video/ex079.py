n = []

while True:
    a = int(input('Digite um valor: '))

    if a not in n:
        print('Número adicionado a lista com sucesso...')
        n.append(a)

    else:
        print('Não é possível adicionar números repetidos')

    c = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]

    while c not in 'SN':
        c = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]

    if c == 'N':
        break
print('=-'*30)
print(f'Os números digitados foram: {sorted(n)}')
