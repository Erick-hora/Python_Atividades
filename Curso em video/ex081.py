n = []
while True:
    n.append(int(input('Digite um valor: ')))

    c = ' '

    while c not in 'SN':
        c = str(input('Você quer continuar [N/S]: ')).strip().upper()[0]

    if c == 'N':
        break

n.sort(reverse=True)
print('-='*40)
print(f'\nVocê digitou {len(n)} valores')
print(f'Os valores digitados em ordem decrescente são: {n}')

if (5 in n):
    print('O valor 5 foi detectado')
else:
    print('O valor 5 não foi detectado')
