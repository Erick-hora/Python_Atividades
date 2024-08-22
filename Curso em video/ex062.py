a1 = int(input('Digite o primeiro termo: '))
q = int(input('Digite a razão: '))

x = 0
n = 0

while x < 10 + n:
    print(a1 + q * x)
    x += 1

    if (x == 10 + n):
        n += int(input('Quantos mais gostaria de mostrar: '))
