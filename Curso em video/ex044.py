print('=' * 5, 'Lojas Erick', '=' * 5)
preco = float(input('Qual o valor das compras? '))
des = 0
parc = 0

print('''[1] Dinheiro/Cheque
[2] Cartão
[3] 2x Cartão
[4] 3x ou + Cartão
''')

op = str(input('Qual a opção de pagamento: '))

if not(op != '1' and op != '2' and op != '3' and op != '4'):
    if (op == '1'):

        des = 0.1
        print(f'O preço a ser pago pelas compras era de {preco} e ficou de {preco - (preco * des)}')

    elif (op == '2'):

        des = 0.05
        print(f'O preço a ser pago pelas compras era de {preco} e ficou de {preco - (preco * des)}')

    elif (op == '3'):

        parc = 2

        print(f'O preço a ser pago pelas compras é de {preco} e o preço das parcelas serão de {preco/2}')

    elif (op == '4'):

        parc = int(input('Quantas parcelas serão? '))
        des = 0.2
        print(f'O preço a ser pago pelas compras era de {preco} e ficou de {preco + (preco * des)} com os juros e o valor dar parcelas serão {(preco + (preco * des))/parc}')

else:
    print('Opção inválida')
