"""
    暴露相关爬虫接口
"""
from model import *
from core.novel_spider import novel_spider

class diyibanzhu:

    __cur_novel = None
    def __init__(self):
        """
        初始化config配置
        """

    

    def get_novel(self, url:str) -> novel:
        """
        传入链接返回小说实体类
        """
        spider = novel_spider(url)
        _novel = spider.connect()
        return spider.parser_novel(_novel)
        
    
    def get_chpater(self, url:str) -> chapter:
        """
        传入链接返回章节实体类
        """
        spider = novel_spider(url)
        _novel = spider.connect()
        self.__cur_novel = _novel
        if _novel:
           return spider.parse_chapter()

    def save_novel(self, _novel:novel):
        self.__save_file(_novel.novel_title, _novel)

    def save_chapter(self, _chapter:chapter):
        self.__save_file(_novel.novel_title, _novel.chapters[0])

    def save_file(self, name : str ='', content : str = ''):
        """
        保存小说, 这里注意可以扩展追加更新和单独保存文件等功能

        后续需要开发管理则需要保存相关元数据, 还没写配置模块所以默认保存到当前文件夹
        """
        with open(f'{name}.txt', 'wt', ncoding='utf-8') as f:
            f.write(content)


        

        
    


