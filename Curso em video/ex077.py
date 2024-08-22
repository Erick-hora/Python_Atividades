words = ('Aprender', 'Correr', 'Andar', 'Saltitar', 'Programar', 'Cantarolar', 'Desejar')

for word in words:
    print(f'\nA palavra {word.upper()} possui as vogais: ', end='')

    for vog in word:
        if vog.lower() in 'aeiou ':
            print(vog.lower(), end=' ')

print('\n')
