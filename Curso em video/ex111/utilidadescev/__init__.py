def aumento(n=0, taxa=10, _format=False):
    f = n + n * (taxa/100)
    return f if _format is False else moeda(f)


def diminui(n=0, taxa=10, _format=False):
    f = n - n * (taxa/100)
    return f if _format is False else moeda(f)


def metade(n=0, _format=False):
    f = n / 2
    return f if _format is False else moeda(f)


def dobro(n=0, _format=False):
    f = n * 2
    return f if _format is False else moeda(f)


def moeda(n=0., _moeda='R$'):
    return f'{_moeda} {n:.2f}'.replace('.', ',')


def resumo(n=0, t=10, d=10):
    print('-'*35)
    print("RESUMO".center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Aumento de {t}%: \t{aumento(n, t, True)}')
    print(f'Desconto de {d}%: \t{diminui(n, d, True)}')
    print('-'*35)
