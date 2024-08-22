co = float(input("Digite o cateto oposto: "))
ca = float(input('Digite o cateto adjacente: '))

hi = (ca ** 2 + co ** 2)
print('A hipotenusa dos catetos é: {:.2f}'.format(hi ** (1/2)))
