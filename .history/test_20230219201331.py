from bs4 import BeautifulSoup as bs

def substring(inp:str, st:str, ed:str) -> str:
    return inp[inp.index(st) + len(st) : inp.index(ed)]

with open('[case]32-32880-754225_5.html', 'rt', encoding='utf-8') as f:
        data = f.read()

soup = bs(data, 'html.parser')

scripts = soup.find_all('script')

ns = None
need_sorted = False

for script in scripts:
    script_text = script.get_text()
    if 'var ns=' in script_text:
        
         break
    
    # if '/js/.'
    print(script['src'])
need_sorted = '/js/a.js' in data


print(need_sorted)