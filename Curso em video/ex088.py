jogos_feitos = []
numeros = []

from random import randint
from time import sleep

print('-='*15)
print(f'{"MEGA SENA":^30} ')
print('-='*15)
qtd_jogos= int(input('Quantos jogos que que eu sortei? '))

for jogos in range(qtd_jogos):

    for num in range(6):

        num_sorteado = randint(1, 60)

        while num_sorteado in numeros:

            num_sorteado = randint(1, 60)

        numeros.append(num_sorteado)

    numeros.sort()
    jogos_feitos.append(numeros[:])
    numeros.clear()

print('\nSorteando...\n')
for pos, jogos in enumerate(jogos_feitos):
    sleep(2)
    print(f'{pos+1}º Jogos: {jogos}')
