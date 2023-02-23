
from common.utils import *
from core.url_parser import url_parser

class novel_spider:

    def __init__(self, url:str = ''):
        """传入url后使用parse方法获取作者author,标题title,章节信息列表chapters"""
        self.__url = url

    def connect(self):
        """测试链接, 解析页面元素从目录页中获取相关信息"""
        try:
            parser = url_parser(self.__url)
            novel_url = f'{parser.base_url}{parser.novel_url}'
            resp = get(novel_url)
            
            logger.info(resp)
        except ValueError as e:
            logger.error(repr(e))