jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
jogador['gols'] = []
jogador['total'] = 0
for x in range(total):
    gols = int(input(f'Quantos gols na {x + 1}° partida: '))
    jogador['total'] += gols
    jogador['gols'].append(gols)
print('-='*40)
print(jogador)
print('-='*40)
print(f'O campo nome possui o valor de: {jogador['Nome']}')
print(f'O campo gols possui o valor de: {jogador['gols']}')
print(f'O campo partidas tem o valor de: {total}')
print('-='*40)
print(f'O jogador {jogador['Nome']} jogou {total} partidas')

for v, k in enumerate(jogador['gols']):
    print(f'Na {v+1}° partida, {jogador['Nome']} fez {k} gols')
print(f'Foi um total de {jogador['total']}')
