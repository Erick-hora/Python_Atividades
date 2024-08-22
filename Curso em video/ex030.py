number = int(input('Digite um número qualquer: '))

if number % 2 == 0:
    print(f'\033[0;32m{number} é um número PAR')
else:
    print(f'\033[0;31m{number} é um número IMPAR')
