n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2
print(f'A media de alguém que tirou {n1} e {n2} é {m}')

if (m >= 7):
    print('Aprovado!')

elif (7 > m >= 5 ):
    print('Recuperação')

else:
    print('Reprovado!')
