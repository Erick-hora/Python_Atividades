def area():
    print(f"{'Controle De Terrenos':^30}")
    print('-' * 30)
    largura = float(input("Qual a largura do terreno(m): "))
    comprimento = float(input("Qual a altura do terreno(m): "))
    areaa = largura * comprimento
    print(f'A área do terreno de {largura:.1f} x {comprimento:.1f} = {areaa:.1f}m².')


area()
