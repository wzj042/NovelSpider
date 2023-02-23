import cloudscraper
from processor.text_processor import text_processor
from common.utils import *


# # 输出文档
# with open('[case](32-32880-754225)无图正序.html', 'wt', encoding='utf-8') as f:
#     f.write(resp.text)

# with open('[case](32-32880-754225_2)乱序带图.html', 'rt', encoding='utf-8') as f:
#     data = f.read()
#     # logger.info(text_processor(solve_text = data).img_process())

#     """@TODO 编写爬虫模块 测试正序获取内容"""

#     with open('temp.html', 'wt', encoding='utf-8') as f:
#         f.write(text_processor(solve_text = data).img_process())

def substring (inp:str, st:str, ed:str) -> str:
    try:
        return inp[inp.index(st) + len(st) : inp.index(ed)] 
    except ValueError as e:
        logger.error(repr(e))
    return None

if __name__ == '__main__':
    """每次加载时设置baseurl"""
    # r = get('http://www.2diyibanzhu.cc/32/32880/754225_3.html')

    with open('[case]32-32880-754225_3.html', 'rt', encoding='utf-8') as f:
        data = f.read()

    content = substring(data, '<div class="neirong">', '</div>')
    print(content)
    

    
    
