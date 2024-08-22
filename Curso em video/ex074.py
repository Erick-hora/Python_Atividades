from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

maior = menor = 0

print('Os valores aleatorios encontrados foram: ', end='')

for numero in numeros:

    print(f'{numero}', end=' ')

print(f'\nDos valores sorteados o maior é {max(numeros)}')
print(f'Dos valores sorteados o menor é {min(numeros)}')
