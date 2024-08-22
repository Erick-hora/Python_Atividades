from ex108 import moeda
num = float(input('Digite um número: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O aumento de 10% do valor {moeda.moeda(num)} é {moeda.aumento(num)}')
print(f'O desconto de 10% do valor {moeda.moeda(num)} é {moeda.moeda(moeda.diminui(num))}')
