nome = ' '
mil = total = menor = 0

print('~'*40)
print('{: ^40}'.format('LOJA BARATÃO'))
print('~'*40)

while True:

    nome1 = str(input('Nome produto: '))
    valor = float(input('Preço: '))

    if (total == 0):

        menor = valor

    else:

        if (menor > valor):

            nome = nome1
            menor = valor

    if (valor > 1000):

        mil += 1

    total += valor

    c = ' '

    while c not in 'SN':

        c = str(input('Deseja continuar [N/S]')).strip().upper()

    if (c == 'N'):

        break

print('{:-^40}'.format('FIM DO PROGRAMAmaca'))
print(f'O total da compra foi: {total:.2f}')
print(f'Temos {mil} que custa mais de 1000.00')
print(f'O produto mais barato foi {nome} que custou {menor:.2f}')
