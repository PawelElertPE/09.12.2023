# program sprawdza, ile jest słów, ile różnych słow i ile razy słowa się powtarzają

from functions import *

content = read_file('u2.txt')

content = clear_text(content)
print(f'liczba slow: {no_of_words(content)}')
print(f'liczba roznych slow: {no_of_unique_words(content)}')
print((f'Powtorzenia {words_repeat(content)}'))







