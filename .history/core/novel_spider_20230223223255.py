
import re
from base64 import b64decode
from bs4 import BeautifulSoup
from common.utils import *
from core.url_parser import url_parser
from processor.text_processor import text_processor
from model import *

class novel_spider:

    __url_parser = None

    def __init__(self, url:str = ''):
        """
        传入url后使用parse方法获取作者author,标题title,章节信息列表chapters
        """
        self.__url = url

    def connect(self) -> novel:
        """测试链接, 解析页面元素从目录页中获取相关信息"""
        try:
            if not self.__url_parser:
                self.__url_parser = url_parser(self.__url)

            parser = self.__url_parser 
            novel_url = f'{parser.base_url}{parser.novel_url}'

            logger.info('测试链接...')
            resp = get(novel_url)

            if resp:
                logger.info('解析小说...')
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
                    
                    print(self.get_chapter_list(resp.text))
                    return novel(
                        url_parser = self.__url_parser,
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

    def get_chapter_list(self, content:str = '') :
        """
            从页面内容获取章节url
        """
        try:
            soup = BeautifulSoup(content, 'html.parser')
            chapter_list_text = str(soup.find_all('ul', class_='list')[1])
            result = re.search('href="(.*)"', chapter_list_text, re.M)

            if result:
                """"""
                return result.group()
            else:
                raise ValueError('页面结构可能发生变动, 爬取目录失败')
            
        except ValueError as e:
            logger.error(repr(e))

    
    def __get_div_text(self, text:str) -> str:
        """
        通用标签解内容提取, 页面结构未更新前大概不会有问题罢
        """ 
        try:
            div_prefix = re.search('(class="\w+")\s(id="\w+">)', text)
            div_suffix = re.search('(</div>)+(\n)?(</div>)', text)
            if div_prefix and div_suffix:
                text = text[div_prefix.end() : div_suffix.start()]
            if str_is_empty(text):
                raise ValueError('该小说解析错误, 可能因为网站变动或案例不足。可提交该链接到issue')
        except ValueError as e:
            logger.error(repr(e))
        return text

    def parse_chapter(self, _chapter:chapter = None) -> chapter:
        """
        从parser或传入的chapeter_url中获取章节
        """
        try:
            logger.info('解析章节...')

            if not _chapter:
                """未传入chapter则从parser中取链接, 还没有则报错"""
                parser = self.__url_parser

                if not parser.chapter_url:
                    raise ValueError('该小说没有章节可以解析')
                
                chapter_url = f'{parser.base_url}{parser.chapter_url}'
                _chapter = chapter(chapter_url)


            cur_index = 1
            chapter_url = _chapter.chapter_url

            while cur_index <= _chapter.page_cnt:
                logger.info(f'解析章节第{cur_index}页')
                page_url = chapter_url.replace('.html',f'_{cur_index}.html')
                self.__parse_page(_chapter, page_url = page_url)
                cur_index += 1
            
            return _chapter
            

        except (ValueError, AttributeError) as e:
            logger.error(repr(e))

    def __parse_page(self, _chapter:chapter = None, page_url:str = ''):
        """
        爬取小说单页内容
        """
        try:
            resp = get(page_url)
            if resp:
                
                try:
                    soup = BeautifulSoup(resp.text, 'html.parser')

                    
                    all_page = soup.find('center', class_='chapterPages')
                    if all_page is None:
                        all_page = 1
                    else:
                        all_page = all_page.get_text().split('】【')
                        all_page = int(all_page[len(all_page) - 1][:-1])

                    _chapter.page_cnt = all_page

                    """解析小说页面分卷名，章节内容"""

                    need_sorted = re.search("\w{3,}\s\w{2,}='(\w+=?)';", resp.text)
                    sorted_arr = None

                    """获取章节内容,  一般情况不使用 get_text 避免将图片标签省略"""
                    content = soup.find('div', class_='neirong')
                    chapter_text = self.__get_div_text(str(content))

                    if need_sorted:
                        """需要排序先获取排序数组"""
                        b64code = str(b64decode(need_sorted.groups()[0]), encoding='utf-8')
                        """转码后转换为整数数组"""
                        sorted_arr = list(map(int, b64code.split(',')))

                        chapter_text = re.sub('\\[(.*?)\\]', '', chapter_text)
                        offset = sorted_arr[0]
                        """这里"""
                        paragraphs = re.split('<br\s?/?><br\s?/?>', chapter_text)

                        chapter_text = ''
                        for i in range(1, len(paragraphs) + 1):
                            chapter_text += paragraphs[sorted_arr[i] - offset] + '\n\n'
    

                    """替换图片标签"""
                    chapter_text = text_processor(solve_text = chapter_text,
                                                  img_process = True, 
                                                  format_process = True, 
                                                  ad_process = True,
                                                  ).get_text()
                    
                    _chapter.chapter_text += chapter_text


                except (AttributeError, IndexError) as e:
                    logger.error(f'解析网页失败{repr(e)}')
            
            """从chapter中获取页面解析, 合并输出内容"""
        except ValueError as e:
            logger.error(repr(e))