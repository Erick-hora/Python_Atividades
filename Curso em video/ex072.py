vinte = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


num = int(input('Digite um número entre 0 e 20: '))

while num > 20 or num < 0:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou {vinte[num]}')
