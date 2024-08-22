l1 = float(input('Digite o primeir lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if (l1 != 0 and l2 != 0 and l3 != 0):

    if (l1 +  l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2):

        if (l1 == l2 and l2 == l3 and l1 == l3):

            print('O triângulo é equilatero')

        elif (l1 == l2 or l1 == l3 or l2 == l3):

            print('O trinângulo é isoceles')

        else:
            print('O triângulo é escaleno')

    else:
        print('Um dos valores é maior que a soma dos outros dois lados')

else:
    print('Um dos valores digitados foi zero!')
    