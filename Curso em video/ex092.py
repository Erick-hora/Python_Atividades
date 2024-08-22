from datetime import datetime
dicio = dict()
dicio["nome"] = str(input("NOME: "))
ano = int(input("ANO DE NASCIMENTO: "))
dicio["idade"] = datetime.now().year - ano
dicio["carteira"] = int(input("NÚMERO DA CARTEIRA [0 NÃO TEM]: "))
if dicio["carteira"] != 0:
    dicio["ano da contratação"] = int(input("ANO DA CONTRATAÇÃO: "))
    dicio["contratação"] = dicio["idade"] + ((dicio["ano da contratação"] + 35) - datetime.now().year)
    dicio["salário"] = float(input("SALÁRIO: "))
print('-='*30)
for v, k in dicio.items():
    print(f'  -  {v} possui valor: {k}')
