km = float(input('Quantos km/h está seu veicúlo: '))

if km > 80:
    print('\n''\033[0;31mMULTADO, você excedeu o limite de 80km/h')
    print(f'\033[0;31mVocê deverá pagar uma multa de {(km-80)*7}\n')

print('\033[0;32mTenha um bom dia! Dirija com segurança!')
