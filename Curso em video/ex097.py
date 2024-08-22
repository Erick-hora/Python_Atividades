def escreva(texto):
    tam = len(texto) + 4
    print('~'*tam)
    print(f'{texto:^{tam}}')
    print('~' * tam)


def pedido():
    txt = str(input('Digite seu texto: '))
    escreva(txt)


pedido()
pedido()
pedido()
