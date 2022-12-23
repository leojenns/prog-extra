

SD = {
    'jan' : [4,5,6],
    'kees': [8,3,9],
    'piet': [5.5,7,3.2],
    'Tamzid': [8,8,8,8,8,8]
}

for naam in SD:
    total = 0
    for grade in SD[naam]:
        total += grade  # total = total + grade
    print(f'cijfer van {naam} = {total/len(SD[naam])}')

