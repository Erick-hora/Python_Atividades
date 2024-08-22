
def votar(ano):
    from datetime import datetime
    d = ''
    idade = datetime.now().year - ano
    c = (f'Com {idade} anos o voto é: ')

    if idade < 16:
        d = ('Negado')

    elif idade >= 18 and idade < 65:
        d = ('Obrigatirio')

    else:
        d = ('Opcional')

    return c + d


a = int(input('Em que ano você nasceu?: '))
print(votar(a))
