# Criando uma lista com 3 listas vazias que será nossa matriz 3x3
matriz = [[], [], []]

# Pedindo três dados
for x in range(3):
    # Pedindo para passar os 3 dados 3 vezes
    for j in range(3):
        # Em cada lista adiconamos 3 valos e informamos a posição de acordo com X e J
        matriz[x].append(int(input(f'Digite um valor para [{x}, {j}]: ')))

# Dando espaço para apresentação da matriz
print('-='*35)

# Passando pela coluna da minha matriz
for x in range(3):
    # Passando pela linha da minha matriz
    for j in range(3):
        # Imprimindo o valor conforme a posição na coluna e linha
        print(f'[{matriz[x][j]:^5}]', end=' ' if j < 2 else '\n')
