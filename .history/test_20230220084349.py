
"""解析链接测试"""
import re

class url_parser:
    def __init__(self, url:str):
        """"判空"""
        if len(url.strip()) == 0:
            raise ValueError("空参数")
        else:
            self.__url = url
            self.__parse()
    
    def __parse(self):
        """检验是否url链接"""
        pattern = re.compile(
            "(http(s)?:\/\/)+([^/]*)")
        result = pattern.search(self.__url)
        if not result:
            raise ValueError("不是合法的url链接")
        else:
            text = result.group()
            print('group', text)
            span0 = result.span(0)
            print('span(0)', text[span0[0] : span0[1]])

        
try:
    parser = url_parser('www.2diyibanzhu.cc')
    parser = url_parser('http://www.2diyibanzhu.cc')
    parser = url_parser('http://www.2diyibanzhu.cc/shuku/0-postdate-0-2.html')
    parser = url_parser('http://www.2diyibanzhu.cc/32/32986/')
    parser = url_parser('http://www.2diyibanzhu.cc/32/32986/755897.html')
    parser = url_parser('http://www.2diyibanzhu.cc/32/32986/755896_2.html')
    
except Exception as e:
    print(repr(e))


"""页面解析测试"""
# from bs4 import BeautifulSoup as bs

# def substring(inp:str, st:str, ed:str) -> str:
#     return inp[inp.index(st) + len(st) : inp.index(ed)]

# with open('[case]32-32880-754225_5.html', 'rt', encoding='utf-8') as f:
#         data = f.read()

# soup = bs(data, 'html.parser')

# scripts = soup.find_all('script')

# # need_sorted -> str(base64 arr)
# ns = None
# ns_prefix = "var ns='"

# # 确认该页内容是否乱序
# for script in scripts:
#     script_text = script.get_text()
#     if ns_prefix in script_text:
#         ns = script_text[script_text.index(ns_prefix) + len(ns_prefix) :-2]
#         break
    
# print(ns)
# chapter_text = soup.find('div', class_='neirong').get_text()
# print(chapter_text)

