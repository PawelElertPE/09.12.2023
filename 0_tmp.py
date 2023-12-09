my_string = 'mama.kupila.psa'

splitted_string = my_string.split('.')
print(f'string przed podziałem: {my_string}')
print(f'string po podziale (dzielimy po kropce: {splitted_string}')

print('\nusuwanie znakow')
my_string = "Mama.kupila.psa"
my_string = my_string.replace('.', '')
print(f'string po usunieciu kropki: {my_string}')


print('\nFunkcje')
def after_a(text):
    return text[text.index('a') +1]

my_string = "mama.kupila.psa"
print(after_a(my_string))

print('\nZbiory')
zbior1 = {'.', ',', '(', '\'', '\"'}
zbior2 = set(',.(\'\"')
print(f'zbior1: {zbior1}')
print(f'zbior2: {zbior2}')
