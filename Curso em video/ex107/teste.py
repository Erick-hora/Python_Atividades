from ex107 import moeda
num = float(input('Digite um número: R$'))
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O aumento de 10% do valor R${num} é R${moeda.aumento(num)}')
print(f'O desconto de 10% do valor R${num} é R${moeda.diminui(num)}')
