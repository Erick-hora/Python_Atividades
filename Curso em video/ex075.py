n = (int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')))

print(f'O valor 9 foi encontrado {n.count(9)} vezes')

if (3 in n):
    print(f'O valor  3 aparece na {n.index(3)+1}° posição')
else:
    print('O valor 3 não aparece nenhuma vez')

print('Os valores pares digitados: ', end='')

for a in n:

    if ((a % 2) == 0):
        print(f'{a}', end=' ')
