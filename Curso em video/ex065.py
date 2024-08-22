soma = menor = maior = cont = 0

continuar = 'S'

while continuar != 'N':

    num = int(input('Digite um número: '))

    if (cont == 0):
        maior = num
        menor = num
    else:
        if(num < menor):
            menor = num

        if(num > maior):
            maior = num


    soma += num
    cont += 1

    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

print(f'Você digitou {cont} números e a media foi {soma/cont}')
print(f'O maior número foi {maior} e o menor número foi {menor}')
