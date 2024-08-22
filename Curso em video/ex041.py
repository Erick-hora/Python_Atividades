from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento '))
id  = atual - ano

print(f'A idade do atleta é {id} e portanto sua classificação é :')

if (id <= 9):
    print('Mirim')
elif (14 >= id):
    print('Infántil')
elif (19 >= id):
    print('Junior')
elif (25 >= id):
    print('Senior')
else:
    print('Master')
