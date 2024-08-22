def ficha(nome="<Desconhecido>", gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


n = str(input('Informe o nome do jogador: ')).strip()
g = str(input('Informe quantos gols o jogador fez: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
