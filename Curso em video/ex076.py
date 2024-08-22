precos = ('Lapis', 1.20, 'Caneta', 2.30, 'Marca texto', 4.59, 'Bandeja', 9.99, 'Carrinho', 120.34)

print('-'*40)
print('{:^40}'.format('LOJA TABULAR'))
print('-'*40)

for itens in range(0, len(precos)):
    if itens % 2 == 0:
        print('{:.<30}R$'.format(precos[itens]), end=' ')

    else:
        print('{:>7.2f}'.format(precos[itens]))
print('-'*40)
