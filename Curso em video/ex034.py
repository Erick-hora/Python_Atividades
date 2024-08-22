sal = float(input('Digite seu salário: '))

if (sal >= 1250):
    print(f'\033[0;33mSeu novo salário será de R${sal + (sal/100 * 10):.2f}')
else:
    print(f'\033[0;33mSeu novo salpario será de R${sal + (sal/100 * 15):.2f}')
