from common.utils import *
"""错误捕获测试"""

# def str_is_empty(inp:str = '') -> bool:
#     """校验字符串是否为空, 非字符类型会被强转为str类型"""
#     if not inp or len(str(inp).strip()) == 0:
#         return True
#     return False 

# def judge_input(inp:str = ''):
#     try:
#         print('inp', inp)
#         if str_is_empty(inp):
#             raise ValueError('empty input')
#         print('after', inp)
#     except ValueError as e:
#         print(repr(e))
# # 抛出后执行

# # case
# try:
#     print(judge_input())
#     print(judge_input(None))
#     print(judge_input(False))
#     print(judge_input(1))
#     print(judge_input(0))
#     print(judge_input(0.8))
#     print(judge_input("abc"))
# except (ValueError) as e:
#     print(repr(e))
"""解析链接测试"""
import re
class url_parser:
    def __init__(self, url:str):
        """解析并校验url返回url参数元组

        非法url或错误的参数
        目录结构会抛出ValueError"""
        self.__url = url
        print(self.get_url_par())
    
    def get_url_par(self) -> tuple:
        """
        校验url是否携带参数, 返回参数元组

        返回例如('http://www.2diyibanzhu.cc/', 'http://', 'cc', '32/32986/755896', '32986/', '_2.html', '_2')
        """
        try:
            pattern = re.compile("((https?://)(\w+\.?)+/)((\d+/)+\d+)((_?\d)?\.html)?")
            result = pattern.search(self.__url)

            if not result:
                raise ValueError(
                    f'入参[{self.__url}]不是合法的带参纯数字链接, 格式参照http://www.2diyibanzhu.cc/32/32986/755896_2.html')
            
            print('g3',result.group(3))
            return result.groups()

        except ValueError as e:
            logger.error(repr(e))
        
        

        
        



# case 
url_parser('http://www.2diyibanzhu.cc/32/32986/')
url_parser('http://www.2diyibanzhu.cc/32/32986/755897.html')
url_parser('http://www.2diyibanzhu.cc/32/32986/755896_2.html')



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

