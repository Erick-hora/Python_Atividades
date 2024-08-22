import random

print('''Your options: 
[1] - Pedra
[2] - Papel
[3] - Tesoura''')

op = int(input('R: '))

cpu = random.randint(1, 3)

print(cpu)
if not(op != 1 and op != 2 and op != 3):
    if (op == 1 and cpu == 2):
        print('Lose')

    elif (op == 1 and cpu == 3):
        print('Win')

    elif (op == 2 and cpu == 1):
        print('Win')

    elif (op == 2 and cpu == 3):
        print('Lose')

    elif (op == 3 and cpu == 1):
        print('Lose')

    elif (op == 3 and cpu == 2):
        print('Win')

    else:
        print('draw')

else:
    print('Opção inválida')