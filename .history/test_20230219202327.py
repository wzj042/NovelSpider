from bs4 import BeautifulSoup as bs

def substring(inp:str, st:str, ed:str) -> str:
    return inp[inp.index(st) + len(st) : inp.index(ed)]

with open('[case]32-32880-754225_5.html', 'rt', encoding='utf-8') as f:
        data = f.read()

soup = bs(data, 'html.parser')

scripts = soup.find_all('script')

# need_sorted -> str(base64 arr)
ns = None
ns_prefix = "var ns='"

# 确认该页内容是否乱序
for script in scripts:
    script_text = script.get_text()
    if ns_prefix in script_text:
        ns = script_text[script_text.index(ns_prefix) + len(ns_prefix) :-2]
        break
    
print(ns)
chapter_text = str(soup.find('div', class_='neirong'))
print(chapter_text)

