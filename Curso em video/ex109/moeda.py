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


def moeda(n=0, _moeda='R$'):
    return f'{_moeda} {n:.2f}'.replace('.', ',')
