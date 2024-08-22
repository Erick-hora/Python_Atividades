s = 0
i = 0
for x in range(1, 501):
    if ((x % 2) != 0 and (x % 3) == 0):
        i += 1
        s += x
print(f'A soma dos {i} número impares entre 500 é {s}')
