colocados = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
             'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminse', 'Sport Recife', 'Ec Vitória',
             'Coritiba', 'Avai', 'Ponte Preta', 'Atlético-GO')




print('-='*40)
print(f'Lista dos 20 melhores times: {colocados}')
print('-='*40)
print(f'Lista dos 5 melhores times: {colocados[:5]}')
print('-='*40)
print(f'Os últimos 4 colocados: {colocados[-4:]}')
print('-='*40)
print(f'A ordem alfabética dos times é: {sorted(colocados)}')
print('-='*40)
print(f'E o chapecoense está na {colocados.index('Chapecoense') + 1}° posição')
print('-='*40)
