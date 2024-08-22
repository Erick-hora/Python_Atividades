def analisador(*num, sit=False):
    dicio = dict()
    dicio['total'] = len(num)
    dicio['maior'] = max(num)
    dicio['menor'] = min(num)
    dicio['media'] = sum(num) / dicio['total']

    if sit:
        if dicio['media'] > 7:
            dicio['situação'] = 'Boa'
        elif dicio['media'] > 5:
            dicio['situação'] = 'Aceitável'
        else:
            dicio['situação'] = 'Péssima'
    return dicio


a = analisador(4, 5, 6, 7, 8, 8, 9, sit=True)
print(a)
