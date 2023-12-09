# program sprawdza, ile jest słów, ile różnych słow i ile razy słowa się powtarzają

with open ('u2.txt', 'r', encoding = 'utf8') as file1:
    content = file1.read(5)
print(type(content))
print(len(content))

content = content.split()
print(f'tekst po splicie: {content}')




