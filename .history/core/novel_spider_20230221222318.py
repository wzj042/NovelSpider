
import re
from bs4 import BeautifulSoup
from common.utils import *
from core.url_parser import url_parser

class novel_spider:

    def __init__(self, url:str = ''):
        """传入url后使用parse方法获取作者author,标题title,章节信息列表chapters"""
        self.__url = url

    def connect(self) -> tuple:
        """测试链接, 解析页面元素从目录页中获取相关信息"""
        try:
            parser = url_parser(self.__url)
            novel_url = f'{parser.base_url}{parser.novel_url}'
            resp = get(novel_url)
            self.__resp_text = resp.text
            if resp:
                try:
                    soup = BeautifulSoup(self.__resp_text, 'html.parser')

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
                    
                    return (novel_title, novel_author, word_count, page_count) 

                except AttributeError as e:
                    logger.error(f'解析网页失败{repr(e)}')
            
        except ValueError as e:
            logger.error(repr(e))