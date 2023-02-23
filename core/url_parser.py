from common.logger import logger
import re



class url_parser:

    base_url = None
    chapter_url = None
    novel_url = None

    def __init__(self, url:str):
        """解析并校验url返回url参数元组"""
        self.__url = url
        self.__parse()
    
    def __parse(self):
        """
        校验url是否携带参数, 调用后可获取base_url(协议 + 域名),novel_url首页,chapter_url章节页等参数
        """
        try:
            logger.info('开始解析链接...')
            """返回例如('http://www.2diyibanzhu.cc/', 'http://', 'cc', '32/32986/755896', '32986/', '_2.html', '_2')"""
            pattern = re.compile("((https?://)(\w+\.?)+/)((\d+/)+\d+)((_?\d)?\.html)?")
            result = pattern.search(self.__url)

            if not result :
                raise ValueError(
                    f'入参[{self.__url}]不是合法的带参纯数字链接, 格式参照http://www.2diyibanzhu.cc/32/32986/755896_2.html')
            
            self.base_url = result.group(1)
            
            """传入链接包括章节页面"""
            self.chapter_url = None
            """将32/32986/755896 转换为32/32986/, 避免本身只传入二层的目录所以不用lastindex直接从第三层截取"""
            self.novel_url = f'{"/".join(result.group(4).split("/")[:2])}/'

            if result.group(6):
                """取出章节首页，取出小说页面"""
                self.chapter_url = f'{result.group(4)}.html'
            
        except ValueError as e:
            logger.error(repr(e))

    def __str__(self) -> str:
        return f'[base_url:{self.base_url}, chapter_url:{self.chapter_url}, novel_url:{self.novel_url}]'
        