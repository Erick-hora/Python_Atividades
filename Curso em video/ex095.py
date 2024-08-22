dados = []
pessoa = {}
gols = []

while True:
    pessoa.clear()
    gols.clear()

    pessoa['nome'] = str(input('Informe o nome do jogador: '))
    part = int(input('informe Quantas partidas ele jogou: '))
    for x in range(part):
        print("    ", end="")
        gols.append(int(input(f'Quantos gols na {x+1}° partida? ')))

    pessoa['gols'] = gols[:]
    pessoa['total'] = sum(gols)

    dados.append(pessoa.copy())

    while True:
        c = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]

        if c in 'SN':
            break

    if c == 'N':
        break

print('-='*40)

print('Cod.', end=" ")

for i in pessoa.keys():
    print(f'{i:<15}', end="")
print()
print('-'*50)

for v, k in enumerate(dados):
    print(f'{v:<3}', end='')
    for x in k.values():
        print(f'{str(x):<17}', end='')
    print()
print('-'*50)

while True:
    busca = int(input("Qual jogador gostaria de checar? [999 faz parar]: "))

    if busca == 999:
        break

    if busca >= len(dados):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' --- LEVANTAMENTO DO RELÁTORIO DO JOGADOR {dados[busca]["nome"]} --- ')

        for x, j in enumerate(dados[busca]["gols"]):
            print(f'NA {x+1}° partida ele marcou {j}')
        print()
