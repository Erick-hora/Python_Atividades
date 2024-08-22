def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mPor favor digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mPor favor digite um número Real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um número inteiro: ')
num1 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {num} e o real foi {num1}')

