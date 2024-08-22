soma = 0
cont = 0

num = 0

while num != 999:
    num = int(input('Digite um número [999 faz parar]: '))

    if (num != 999):
        soma += num
        cont += 1

print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
