from bs4 import BeautifulSoup as bs

with open('[case]32-32880-754225_5.html', 'rt', encoding='utf-8') as f:
        data = f.read()

soup = bs(data, 'html.parser')

scripts = soup.find_all('script').get_text()
print(scripts)

