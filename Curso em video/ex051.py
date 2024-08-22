n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for x in range(n1, n1 + r * 10, r):
    print(f'{x} -> ', end='')
print('Acabou')
