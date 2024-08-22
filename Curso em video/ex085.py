# Criando minha lista com duas listas vazias
lista = [[], []]

# Pedindo sete valores
for x in range(1, 8):

    # Pedindo para digitar um valor
    valor = int(input(f'Digite o {x}° valor: '))

    # Se o valor for divisivel por 2 de forma exata
    if valor % 2 == 0:
        # Colocamos na primeira lista
        lista[0].append(valor)

    # Senão
    else:
        # colocamos na segunda lista
        lista[1].append(valor)

# Colocando as listas em ordem crescente
lista[0].sort()
lista[1].sort()

# Informando os valores pares (primeira lista) e impares (segunda lista)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')
