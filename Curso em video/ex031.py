km = float(input('Digite a distância de sua viagem: '))

preco = km * 0.5 if km <= 200 else km * 0.45

print('\033[0;32mVocê está prestes a iniciar uma viagem de {}km'.format(km))
print('\033[0;35mO preço da sua passagem será de R${:.2f}'.format(preco))

