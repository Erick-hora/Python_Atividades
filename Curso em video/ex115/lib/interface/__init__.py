def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mPor favor digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for op in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{op}\033[m')
        c += 1
    print(linha())
    resp = leiaint('\033[0;32mDigite sua opção: \033[m')
    return resp