from bs4 import BeautifulSoup as bs

with open('[case]32-32880-754225_5.html', 'rt', encoding='utf-8') as f:
        data = f.read()

soup = bs(data, 'html.parser')
need_sorted = '/js/a.js' in data


print(need_sorted)