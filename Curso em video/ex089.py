alu = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('PRIMEIRA NOTA: '))
    nota2 = float(input('SEGUNDA NOTA: '))
    media = (nota1 + nota2)/2

    alu.append([nome, [nota1, nota2], media])

    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if (c == 'N'):
        break

print('-='*30)
print('{:<4} {:^10} {:>8}'.format('NO.', 'NOME', 'NOTA'))
print('-'*25)


for v, b in enumerate(alu):
    print(f'{v:<4} {b[0]:^12} {b[2]:>6.1f}')
print('-'*45)

res = 0

while res != 999:
    res = int(input('Mostar nota de qual aluno? [999 para]: '))

    for v, b in enumerate(alu):
        if (v == res):
            print(f'A nota de {b[0]} foram {b[1]}')
