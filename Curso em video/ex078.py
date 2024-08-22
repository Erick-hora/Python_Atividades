n = []
maior = menor = 0


for x in range(5):
    n.append(int(input(f'Digite um valor para a Posição {x}: ')))

    if x == 0:

        menor = n[x]
        maior = n[x]

    else:

        if n[x] < menor:

            menor = n[x]

        if n[x] > maior:

            maior = n[x]

print(f'Os valores digitados foram {n}')

print(f'O maior dos valores foi {maior} e está nas posições', end=' ')
for i, v in enumerate(n):
    if v == maior:
        print('{:.>5}'.format(i), end=' ')

print(f'\nO maior dos valores foi {menor} e está nas posições', end=' ')
for i, v in enumerate(n):
    if v == menor:
        print('{:.>5}'.format(i), end=' ')
