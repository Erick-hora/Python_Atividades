n1 = int(input('Digite um número: '))
r = n1
f = 1
print(f'{n1}! = ', end='')

while r > 0:
    print(f'{r} ', end='')
    print(f'X ' if r > 1 else '= ', end='')
    f *= r
    r -= 1
print(f'{f}')
