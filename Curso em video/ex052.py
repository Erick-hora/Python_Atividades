i = int(input('Digite um número inteiro: '))
s = 0

for x in range(1, i + 1):
    if (i % x == 0):
        s += 1

if (s == 2):
    print('Este é um número primo')
else:
    print('Este número não é primo')
