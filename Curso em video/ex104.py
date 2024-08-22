def leiaInt(txt):
    while True:
        r = str(input(txt))
        if r.strip().isnumeric():
            r = int(r)
            return r
        print('\033[0;31mERRO, O valor digitado não é um número!\033[m')


n = leiaInt('Digite um número: ')
print(n)
