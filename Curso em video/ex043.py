print('='*52)
print('='*18 + ' IMC CALCULATOR ' + '='*18)

alt = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / alt ** 2

print(f'O seu imc é de: {imc:.0f}')

if (imc < 18.5):
    print('Abaixo do peso')
elif (25 > imc >= 18.5):
    print('Peso ideal')
elif (30 > imc >= 25):
    print('Sobrepeso')
elif (40 > imc >= 30):
    print('Obesidade')
else:
    print('Obesidade mórbida')
