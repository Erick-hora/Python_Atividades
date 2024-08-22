from time import sleep
from random import randint


def sortea():
    print('-='*40)
    print('Sorteando 5 valores: ', end=' ')
    for x in range(5):
        sleep(0.5)
        numeros.append(randint(1, 10))
        print(numeros[x], end=' ')
    print('Pronto!')


def somando(lista):
    print('-=' * 40)
    print(f'Somando o valores pares de {lista}, temos: ', end=' ')
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(soma)


numeros = list()
sortea()
somando(numeros)
