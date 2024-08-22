import random

from time import sleep

tentativa = 1

chute = -1
numero = random.randint(0, 10)

while chute != numero:
    chute = int(input('\nChute um valor de 0 a 10: '))

    sleep(1)

    if (numero > chute):
        print(f'Maior,  tente mais uma vez...')
        tentativa += 1

    elif (numero < chute):
        print(f'Menor, tente mais uma vez...')
        tentativa += 1

print(f'Parabéns, seu chute foi {chute} e o número foi {numero}')
print('Você usou {} tentativas'.format(tentativa))
