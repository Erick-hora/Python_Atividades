nome = str(input('Digite seu nome: ').replace(' ', '')).strip().upper()
print(f'Seu nome possui {nome.count('A')} letras A')
print(f'A primeira aparece na {nome.find('A') + 1} posição')
print(f'A última aparece na {nome.rfind('A') + 1} posição')
