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
    
    def parse(self):
        """
        校验url是否携带参数, 调用后可获取base_url(协议 + 域名),首页,章节页等参数

        返回例如('http://www.2diyibanzhu.cc/', 'http://', 'cc', '32/32986/755896', '32986/', '_2.html', '_2')
        """
        try:
            pattern = re.compile("((https?://)(\w+\.?)+/)((\d+/)+\d+)((_?\d)?\.html)?")
            result = pattern.search(self.__url)

            if not result :
                raise ValueError(
                    f'入参[{self.__url}]不是合法的带参纯数字链接, 格式参照http://www.2diyibanzhu.cc/32/32986/755896_2.html')
            
            self.base_url = result.group(1)
            
            """传入链接包括章节页面"""
            self.chapter_url = None
            if result.group(6):
                self.chapter_url = f'{result.group(4)}.html'
                self.novel_url = result.group(4).split('/')[:1]
                print('novelurl', self.novel_url)
            return result.groups()

        except ValueError as e:
            logger.error(repr(e))