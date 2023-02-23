import url_parser
from common.utils import *

class novel_parser:

    def __init__(self, url:str = ''):
        """传入url后使用parse方法获取作者author,标题title,章节信息列表chapters"""
        self.__url = url

    def connect(self):
        """测试链接, 解析页面元素"""
        try:
            parser = url_parser(self.__url)
            logger.info(parser)
        except ValueError as e:
            logger.error(repr(e))