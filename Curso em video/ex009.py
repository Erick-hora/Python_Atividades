tabuada = int(input('Digite qual tabuada você quer ver: '))

print('='*15)

for i in range(1, 11):
    print('{} * {} = {}'.format(tabuada, i, tabuada*i), end='')
    print('   |')

print('='*15)
