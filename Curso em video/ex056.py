media = 0
velho = ''
id_velho = 0
femea_nova = 0

for people in range(1, 5):
    print('-'*10+ f' {people}ºPessoa ' + '-'*10)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()[0]

    if (idade > id_velho and sexo == 'M'):
        velho = nome
        id_velho = idade

    if (sexo == 'F' and idade < 20):
        femea_nova += 1

    media += idade

media /= 4

print('A media da idade das pessoas do grupo é {}'.format(media))
print(f'O homem mais velho é {velho} e tem {id_velho} anos')
print(f'A quantiade de mulheres com menos de 20 anos é de {femea_nova}')
