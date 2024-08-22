c = ['\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;44m']


def ajuda(_help):
    titulo(f'Acessando o manual do comando \'{biblio}\'', 2)
    print(c[3], end='')
    help(_help)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end=' ')


biblio = ' '
while True:
    titulo('SISTEMA DE HELP PYTHON', 3)
    biblio = str(input('Função ou Biblioteca:')).strip()

    if biblio.upper() == 'FIM':
        break
    else:
        ajuda(biblio)

titulo('Até logo', 1)
