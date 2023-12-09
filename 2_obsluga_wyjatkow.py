# slownik_imion = {
#     'Jan': 'John',
#     'Maria': 'Marry',
#     'Jacek': 'Jack'
#
# }

x = input("podaj liczy do dzielenia: ").split()
try:

    result = int(x[0]) / int(x[1])
except IndexError:
    result = int(x[0])
except ZeroDivisionError:
    result = 1
except ValueError:
    result = 0
else:
    print(f'udalo sie - tworze plik z logami')


print(result)

print(type(x))

#IndexError:
#ZeroDivisionError:

