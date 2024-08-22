from random import randint
from time import sleep

n = randint(0, 5)
print('-='*30)
print('Estou pensando em um número entre 0 a 5 tente adivinhar')
print('-='*30)
chu = (int(input('\nDigite o seu chute entre 0 e 5: ')))
print('Processando...')
sleep(2)
if chu == n:
    print('\033[0;32mMeus parabéns, você acertou')
else:
    print('\033[0;31mInfelizmente não foi desta vez, eu havi pensado no {} e não no {}'.format(n, chu))

