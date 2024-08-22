from random import randint
from time import sleep


dicio = {}
print('Valores sorteados: ')

for x in range(4):

    dicio[f'Jogador{x+1}'] = randint(1, 6)
    sleep(1)
    print(f'O jogador{x+1} tirou: {dicio[f"Jogador{x+1}"]}')

print('-='*30)
print('{:-^40}'.format('RANKING'))

ranking = sorted(dicio.items(), key=lambda item: item[1], reverse=True)

for v, i in enumerate(ranking):
    sleep(1)
    print(f'{v+1}° Lugar: {i[0]} com {i[1]}')
