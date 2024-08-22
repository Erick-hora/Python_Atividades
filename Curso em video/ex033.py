a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

m = a
n = a
#verificando menor
if b < a and b < c:
    n = b
if c < a and c < b:
    n = c
#verificando maior
if b > a and b > c:
    m = b
if c > a and c > b:
    m = c

print(f'\033[0;31mO maior número digitado foi: {m}')
print(f'\033[0;33mO menor número digitado foi: {n}')
