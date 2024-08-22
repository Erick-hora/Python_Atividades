# Minhas listas
pessoas = []
dados = []
maior = menor = 0

# prendendo o usuário no loop
while True:

    # pegando os dados
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite seu peso: ')))

    # passando meus dados para minha lista pessoas
    pessoas.append(dados[:])

    # Limpando minha lista para próxima vez que for pegar os dados
    dados.clear()

    # Criando variável continuar vazia
    continuar = ' '

    # Enquanto continuar não foir S ou N
    while continuar not in 'SN':

        # perguntando se a pessoas quer continuar
        continuar = str(input('Gostaria de continuar [S/N]: ')).strip().upper()[0]

    # Se a respota for N, ele pula o código
    if continuar == 'N':
        break
    # Caso seja S, ele volta o loop

# printando quantas pessoas cadastramos
print(f'A quantidade de pessoas cadastradas foram {len(pessoas)}')

# Pegando meus dados dentro da lista pessoas
for x in pessoas:
    # Se estivermos no primeiro dado
    if x == pessoas[0]:
        # Setamos o valores de maior e menor como o peso desta pessoa
        menor = x[1]
        maior = x[1]

    # Caso não seja mais a primeira
    else:
        # V irá checar cada dado
        for v in x:
            # Se o dado for igual ao peso da pessoas
            if v == x[1]:

                # Se o peso desta pessoa for menor que o peso menor
                if v < menor:
                    # Atribuimos o peso desta pessoa como menor
                    menor = v

                # Se o peso desta pessoa for maior que o peso maior
                if v > maior:
                    # ATribuimos o peso desta pessoa como maior
                    maior = v

# Informando qual foi o maior peso
print(f'O maior peso foi de {maior}Kg. peso de ', end='')

# Passando pelos meus dados dentro da lista pessoas
for x in pessoas:

    # Checando se meu dado é igual a maior e printando a pessoa que possui aquele peso
    if maior in x:

        print(f'[{x[0]}]', end=' ')

# Informando qual foi o menor peso
print(f'\nO menor peso foi de {menor}Kg. peso de ', end='')

# Passando pelos meus dados dentro da lista pessoas
for x in pessoas:

    # Se nos meus dados possui o menor peso, informo que esta pessoa está entre as mais leves
    if menor in x:
        print(f'[{x[0]}]', end=' ')
