print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
n = int(input('Digite quantos termos você quer: '))

x = 0
x1 = 1
c = 2

print('~'*30)
print(f'{x} -> ', end='')
print(f'{x1} ->', end='')

while c < n:

    x2 = x1 + x
    print(f' {x2} ->', end='')

    x = x1
    x1 = x2

    c += 1

print(' FIM \n' + '~'*30)
