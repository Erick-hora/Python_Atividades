valor_da_casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento?'))

print(f'Para pagar uma casa de R${valor_da_casa} em {financiamento} anos a prestação será de {((valor_da_casa / financiamento)/12):.2f}')

if (((valor_da_casa / financiamento)//12) > salario * 0.3):
    print('Empréstimo Negado!!')

else:
    print('Empréstimo Concedido!!')
