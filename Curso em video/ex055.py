m = 0
n = 1000

for x in range(5):
    peso = float(input('Digite o seu peso: '))

    if (peso > m):
        m = peso
    elif (peso < n):
        n = peso

print(f'O menor e o maior peso registrados foram de {n:.0f} e {m:.0f} respectivamente')