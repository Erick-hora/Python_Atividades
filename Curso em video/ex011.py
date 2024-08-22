largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura

print(f'A sua parede possui a largura de {largura:.2f} e a altura de {altura:.2f}, sendo assim a área é de '
      f'{area:.2f}m² e, portanto, será utilizada {area/2:.2f} litros de tinta')

