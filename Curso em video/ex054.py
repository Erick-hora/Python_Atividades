m = 0
n = 0

for x in range(7):
    id = int(input('Digite a idade do grupo de 7 pessoas: '))

    if (id >= 18):
        m += 1
    else:
        n += 1

print(f'O Grupo possui {n} menores e {m} mais de maiores')
