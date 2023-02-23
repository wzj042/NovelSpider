"""解析链接测试"""
from common.logger import logger
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

            if not result :
                raise ValueError(
                    f'入参[{self.__url}]不是合法的带参纯数字链接, 格式参照http://www.2diyibanzhu.cc/32/32986/755896_2.html')
            
            return result.groups()

        except ValueError as e:
            logger.error(repr(e))