matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = meio = terc = 0
for x in range(3):
    for j in range(3):
        matriz[x][j] = int(input(f'Digite um valor para [{x}, {j}]: '))

print('-='*35)
for x in range(3):
    for j in range(3):

        if (matriz[x][j] % 2) == 0:
            par += matriz[x][j]

        if (x == 1):
            meio += matriz[x][j]

        if (j == 2):
            terc += matriz[x][j]


        print(f'[{matriz[x][j]:^5}]', end=' ')
    print()

print(f'A soma dos números pares é: {par}')
print(f'A soma dos valores da segunda linha é {meio}')
print(f'A soma de valores da terceira coluna é {terc}')

