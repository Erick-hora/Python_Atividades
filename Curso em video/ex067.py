while True:
    n = int(input('Gostaria de ver qual tabúada: '))
    x = 1

    if (n < 0):
        break

    while x <= 10:
        print(f'{n} x {x} = {n*x}')
        x += 1
