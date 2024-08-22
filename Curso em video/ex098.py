
from time import sleep


def contador(ini, fim, passo):
    print('-='*30)
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print(f'Contando de {ini} até {fim} de {passo} em {passo}')
    sleep(2)
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += passo
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= passo



    print('FIM')


contador(1, 10, 1)
contador(10, 0, -2)
print('-='*30)
print('Agora é a sua vez de personalizar: ')
i = int(input('Em qual número devemos iniciar? '))
f = int(input('Qual o final da contagem? '))
p = int(input('Qual o passo da contagem? '))
contador(i, f, p)
