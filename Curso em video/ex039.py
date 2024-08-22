from datetime import date
ano = int(input('Ano de nascimento: '))

atual = date.today().year

if (atual - ano > 18):
    print(f'Você perecisa se alistar desde {atual - ano - 18} anos')
    print(f'Seu alistamento foi em {atual - (atual - ano - 18)}')

elif (atual - ano < 18):
    print(f'Ainda faltam {18 - (atual - ano)} anos para se alistar')
    print(f'Seu alistamento será {atual + (18 - (atual - ano))}')

else:
    print(f'Você deve se alistar imediantamente')
