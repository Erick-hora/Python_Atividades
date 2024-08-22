s = 0
for x in range(0, 6):
    n = int(input('Digite o número: '))

    if ((n % 2) == 0):
        s += n

print(f'A soma dos números pares é: {s}')
