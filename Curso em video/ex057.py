sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é o seu sexo? ')).strip().upper()

    if (sexo != 'M' and sexo != 'F'):
        print('Valor incorreto, digite novamente')
print('O sexo digitado foi {}'.format(sexo))
