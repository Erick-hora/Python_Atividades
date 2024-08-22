frase = str(input('Digite uma frase: ')).strip().lower().split()

frase1 = ''.join(frase)
frase2 = frase1[::-1]

if (frase1 == frase2):
    print('Palindromo!')
else:
    print('Não é palindromo')