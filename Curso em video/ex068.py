from random import randint
print('-'*40)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-'*40)

v = 0

while True:
    n = int(input('Digite um número: '))
    p = ' '

    while p not in 'IP':
        p = str(input('PAR OU IMPAR[P/I]: ')).strip().upper()[0]

    cpu = randint(0, 11)

    print(f'Vcoê jogou {n} e o computador jogou {cpu}. Total deu {n + cpu}', end='')

    if ((cpu + n) % 2 == 0):
        print('  que é PAR')

        if (p == 'P'):
            print('\nVocê VENCEU!')
            print('Vamos jogar novamente...')
            v += 1
        else:
            break

    else:
        print(' que é IMPAR')

        if (p == 'I'):
            print('\nVocê VENCEU!')
            print('Vamos jogar novamente...')
            v += 1
        else:
            break

if (v > 1):

    print(f'Você venceu {v} vezes consecutivas')
