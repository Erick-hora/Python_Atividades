ano = int(input('Digite o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[0;34mEste é um ano bissexto!')
else:
    print('\033[0;31mEste não é um ano bissexto!')