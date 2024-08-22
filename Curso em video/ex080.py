n = []
for x in range(5):

    a = int(input('Digite um valor: '))

    if (x == 0 or a > n[-1]):
        n.append(a)
        print('O valor foi adicionado ao final da lista')

    else:
        pos = 0
        while pos < len(n):
            if (a <= n[pos]):
                n.insert(pos, a)
                print(f'O valor foi adicionado na {pos} posição')
                break
            pos += 1
print('Os valores digitados foram {}'.format(n))
