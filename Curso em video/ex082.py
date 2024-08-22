lista = []
par = []
impar = []
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    if (numero % 2) == 0:

        par.append(numero)

    else:

        impar.append(numero)

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]



    if continuar == 'N':

        break

print(f'\nOs valores digitados foram: {lista}')
print(f'Os valores pares foram: {par}')
print(f'Os valores impares foram: {impar}')
