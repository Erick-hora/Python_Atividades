n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

res = ''

while res != '5':
    print('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR 
    ''')
    res = str(input('>>')).strip()

    if(res == '1'):

        print(f'A soma entre {n1} e {n2} é {n1 + n2}')

    elif(res == '2'):

        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')

    elif(res == '3'):

        if(n1 > n2):
            print(f'O maior número entre {n1} e {n2} é {n1}')
        elif(n2 > n1):
            print(f'O maior número entre {n1} e {n2} é {n2}')
        else:
            print('Os dois valores são iguais')

    elif(res == '4'):

        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

    elif(res == '5'):
        
        print('')

    else:

        print('Opção inválida!')

print('Obrigado pela preferência!')
