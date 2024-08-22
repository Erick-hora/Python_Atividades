numero = int(input('Digite um número entre 0 e 9999: '))

print(f'Milhar: {numero // 1000 % 10}')
print(f'Centena: {numero // 100 % 10}')
print(f'Dezena: {numero // 10 % 10}')
print(f'Unidade: {numero // 1 % 10}')
