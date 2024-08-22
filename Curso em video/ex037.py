num = int(input('Digite um número inteiro: '))
print('''Digite uma das bases para conversão
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opcao = str(input('Digite sua opção: '))

if (opcao == '1'):
    print(f'O número {num} convertido para BINARIO é {bin(num)[2:]}')
elif (opcao == '2'):
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')
elif (opcao == '3'):
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida! Tente novamente.')