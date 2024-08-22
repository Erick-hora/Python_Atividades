people = men = woman = 0

while True:
    print('~'*40)
    print('CADASTRAR PESSOA')
    print('~' * 40)

    idade = int(input('Infome sua idade: '))
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

    while sexo not in 'FM':
        sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

    print('~' * 40)

    if (idade > 18):
        people += 1

    if (sexo == 'M'):

        men += 1

    if (idade < 20 and sexo == 'F'):
        woman += 1

    c = str(input('Deseja continuar [N/S]')).strip().upper()

    while c not in 'NS':
        c = str(input('Deseja continuar [N/S]')).strip().upper()

    if (c == 'N'):
        break

print(f'A quantidade de pessoas com mais de 18 anos é {people}')
print(f'A quantidade de homens é {men}')
print(f'A quantidade de mulheres com menos de 20 anos é {woman}')
