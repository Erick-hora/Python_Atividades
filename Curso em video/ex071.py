print('-'*40)
print('{: ^40}'.format('BANCO E&R'))
print('-'*40)

cin = 0
vin = 0
co = 0
um = 0


while True:

    valor = int(input('Digite o valor que deseja sacar: '))

    if ((valor // 50) >= 1):

        cin = valor // 50
        print(f'A quantiade em notas de 50 é {cin}')

        valor -= 50 * (valor // 50)

        if (valor == 0):

            break

    if ((valor // 20) >= 1):

        vin = valor // 20
        print(f'A quantiade em notas de 20 é {vin}')

        valor -= 20 * (valor // 20)

        if (valor == 0):

            break

    if ((valor // 10) >= 1):

        co = valor // 10
        print(f'A quantiade em notas de 5 é {co}')

        valor -= 10 * (valor // 10)

        if (valor == 0):

            break

    if ((valor/1) == valor):

        um = valor/1
        print(f'A quantiade em notas de 1 é {um:.0f}')

        valor -= 1 * (valor / 1)

        break
