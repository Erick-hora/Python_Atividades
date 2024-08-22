nome = str(input('Digite seu nome: ')).strip()

print('Seu nome maiúsculo: {}'.format(nome.upper()))
print(f'Seu nome minúsculo: {nome.lower()}')
print(f'Seu nome possui {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome possui {nome.find(' ')} letras')
