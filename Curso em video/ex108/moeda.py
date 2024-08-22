def aumento(n=0, taxa=10):
    f = n + n * (taxa/100)
    return f


def diminui(n=0, taxa=10):
    f = n - n * (taxa/100)
    return f


def metade(n=0):
    f = n / 2
    return f


def dobro(n=0):
    f = n * 2
    return f


def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')
