from common.utils import *
from core.novel_spider import novel_spider
from core.url_parser import url_parser

# case 
# novel_spider('http://www.2diyibanzhu.cc/32/32986/').connect()
# novel_spider('http://www.2diyibanzhu.cc/32/32986/755897.html').connect()
# novel_spider('http://www.2diyibanzhu.cc/32/32986/755896_2.html').connect()


"""页面解析测试"""
# # 获取页面保存文件
# resp = get('http://www.2diyibanzhu.cc/32/32986/')
# with open('[case]32-32986.html', 'wt', encoding='utf-8') as f:
#     f.write(resp.text)

import re
from bs4 import BeautifulSoup as bs

from base64 import b64decode

with open('[case]32-32880-754225_5.html', 'rt', encoding='utf-8') as f:
        data = f.read()

try:
    soup = bs(data, 'html.parser')
    need_sorted = re.search("\w{3,}\s\w{2,}='(\w+=?)';", data)
    sorted_arr = None

    """获取章节内容,  一般情况不使用 get_text 避免将图片标签省略"""
    content = soup.find('div', class_='neirong')
    chapter_text = None

    """获取内容分三种, 无图直接neirong get_text, 带图分两种。乱序从chapter获取子节点内容, 顺序从neirong获取子节点内容"""
    if not '/toimg/data/' in data:
        chapter_text = content.get_text()
    
    if not chapter_text:
          
        if need_sorted:
            chapter_text = str(content.find('div'))
            print(chapter_text)
            """需要排序先获取排序数组"""
            b64code = str(b64decode(need_sorted.groups()[0]), encoding='utf-8')
            """转码后转换为整数数组"""
            sorted_arr = list(map(int, b64code.split(',')))
            """加载js后小说内容的祖父标签也变成了id='chapter'"""

        else:
            print('不需要排序')

    elif need_sorted:
        raise ValueError(f'该小说暂时无法正常解析, 可以提交小说链接和报错到github issue中。有空说不定会修')
    

    print(sorted_arr)
    

except (AttributeError, ValueError) as e:
      logger.error(f'解析网页失败{repr(e)}')

# print(title)
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

