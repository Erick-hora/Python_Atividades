from time import sleep


def maior(*num):
    print('-='*40)
    print('Analisando o números fornecidos... ')
    for x in num:
        sleep(0.5)
        print(x, end=' ')
    print(f'Foram fornecidos ao todo {len(num)} valores')
    print(f'O maior número fornecido foi: {max(num)}')

maior(1, 2, 6 ,5 ,6, 7,8, 8)
maior(99, 2 ,5, 7, 8)
