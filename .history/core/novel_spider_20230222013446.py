
import re
from bs4 import BeautifulSoup
from common.utils import *
from core.url_parser import url_parser
from model import *

class novel_spider:

    __url_parser = None

    def __init__(self, url:str = ''):
        """传入url后使用parse方法获取作者author,标题title,章节信息列表chapters"""
        self.__url = url

    def connect(self) -> novel:
        """测试链接, 解析页面元素从目录页中获取相关信息"""
        try:
            self.__url_parser = url_parser(self.__url)
            novel_url = f'{self.__url_parser.base_url}{self.__url_parser.novel_url}'
            logger.info('开始测试链接...')
            resp = get(novel_url)
            if resp:
                
                logger.info('开始解析小说...')
                try:
                    soup = BeautifulSoup(resp.text, 'html.parser')

                    novel_title =  soup.h1.get_text()
                    """作者，字数"""
                    info_text = soup.find('p', class_='info').get_text()
                    pattern = re.compile(r'[\u4e00-\u9fa5]{2,}：')

                    infos = pattern.sub('', info_text).split('\n')[1:]
                    novel_author = infos[0]
                    word_count = infos[2]
                    
                    """目录页数"""
                    end_page_href = soup.find('a', class_='endPage').attrs['href']
                    pattern = re.compile('_(\d)/')
                    page_count = int(pattern.search(end_page_href).groups()[0])
                    
                    return novel(
                        url_parser = parser,
                        novel_menu_text = resp.text,
                        novel_title = novel_title, 
                        novel_author = novel_author, 
                        word_count = word_count, 
                        page_count = page_count,
                    )

                except AttributeError as e:
                    logger.error(f'解析网页失败{repr(e)}')
            
        except ValueError as e:
            logger.error(repr(e))

    def parse_page(self, novel:novel = None) -> str:
        """爬取小说单页内容"""
        try:
            parser = novel.url_parser
            if parser.
        except ValueError as e:
            logger.error(repr(e))