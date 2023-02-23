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


with open('[case]32-32986.html', 'rt', encoding='utf-8') as f:
        data = f.read()

try:
    soup = bs(data, 'html.parser')

    novel_title =  soup.h1.get_text()
    """作者，字数"""
    info_text = soup.find('p', class_='info').get_text()
    pattern = re.compile(r'[\u4e00-\u9fa5]{2,}：')

    infos = pattern.sub('', info_text).split('\n')[1:]
    novel_author = info_text[0]
    word_count = info_text[2]
    
    """目录页数"""
    end_page_href = soup.find('a', class_='endPage').attrs['href']
    pattern = re.compile('_(\d)/')
    page_count = int(pattern.search(end_page_href).groups()[0])
    
except AttributeError as e:
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

