
"""错误捕获测试"""

def str_is_empty(inp:str = '') -> bool:
    """校验字符串是否为空, 非字符类型会被强转为str类型"""
    if not inp or len(str(inp).strip()) == 0:
        return True
    return False 

def judge_input(inp:str = ''):
    print('inp', inp)
    if str_is_empty(inp):
        raise ValueError('empty input')
    print('after', inp)
# 抛出后执行

# case
try:
    print(str_is_empty())
    print(str_is_empty(None))
    print(str_is_empty(False))
    print(str_is_empty(1))
    print(str_is_empty(0))
    print(str_is_empty(0.8))
    print(str_is_empty("abc"))
except (ValueError) as e:
    print(repr(e))
"""解析链接测试"""
# import re
# from common.utils import *

# class url_parser:
#     def __init__(self, url:str):
#         """解析并校验url,非法url或缺失目录结构会抛出ValueError"""
#         self.__url = url
#         self.__parse()
    
#     def __parse(self):
        
#         """"判空"""
        
        
#         """检验是否url链接"""
#         pattern = re.compile(
#             "(http(s)?:\/\/)+([^/]*)")
#         result = pattern.search(self.__url)
#         if not result:
#             logger.warning(f'入参[{self.__url}]不是合法的url链接, 检查是否携带了协议头(http://)')
#             return
        
#         text = result.group()
#         print('group', text)
#         span0 = result.span(0)
#         print('span(0)', text[span0[0] : span0[1]])

        
# try:
#     url_parser('http://www.2diyibanzhu.cc/shuku/0-postdate-0-2.html')
#     url_parser('bbb.2diyibanzhu.cc')
#     print('raise after')
#     praser = url_parser('')
#     url_parser('www.2diyibanzhu.cc')
#     url_parser('http://www.2diyibanzhu.cc')
#     url_parser('http://www.2diyibanzhu.cc/shuku/0-postdate-0-2.html')
#     # parser = url_parser('http://www.2diyibanzhu.cc/shuku/0-postdate-0-2.html')
#     # parser = url_parser('http://www.2diyibanzhu.cc/32/32986/')
#     # parser = url_parser('http://www.2diyibanzhu.cc/32/32986/755897.html')
#     # parser = url_parser('http://www.2diyibanzhu.cc/32/32986/755896_2.html')
    
# except ValueError as e:
#     print(repr(e))


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

