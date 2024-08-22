formula = []
exp = str(input('Digite sua expressão: '))

for simb in exp:

    if (simb == '('):

        formula.append(simb)

    elif (simb == ')'):

        if (len(formula) > 0):

            formula.pop()

        else:

            formula.append(')')
            break

if (len(formula) == 0):

    print('Sua expressão está correta!')

else:

    print('Sua expressão está incorreta!')


