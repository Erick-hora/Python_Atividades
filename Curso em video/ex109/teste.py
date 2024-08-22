from ex109 import moeda
num = float(input('Digite um número: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O aumento de 10% do valor {moeda.moeda(num)} é {moeda.aumento(num, 10, True)}')
print(f'O desconto de 10% do valor {moeda.moeda(num)} é {moeda.diminui(num, 10, True)}')
