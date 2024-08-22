l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if l1 != 0 and l2 != 0 and l3 != 0:
    if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
        print('\033[0;33;40mPodem formar um triângulo!\033[m')
    else:
        print('\033[1;35;46mNão podem formar um triângulo!\033[m')

else:
    print('\033[4;31mNenhum dos valores pode ser zero!\033[m')
