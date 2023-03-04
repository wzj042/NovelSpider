"""
    暴露相关爬虫接口
"""
from model import *
from common.logger import logger
from core.novel_spider import novel_spider

class diyibanzhu:

    __cur_novel = None
    
    def __init__(self):
        """
        @TODO:初始化config配置
        """

    

    def get_novel(self, url:str) -> novel:
        """
        传入链接返回小说实体类
        """
        try:
            spider = novel_spider(url)
            _novel = spider.connect()
            if not _novel:
                raise ValueError('获取小说内容失败')
            return spider.parser_novel(_novel)
        except ValueError as e:
            logger.error(repr(e))
        
    
    def get_chpater(self, url:str) -> chapter:
        """
        传入链接返回章节实体类
        """
        try:
            spider = novel_spider(url)
            _novel = spider.connect()
            self.__cur_novel = _novel
            if not _novel:
                raise ValueError('获取该章节失败')
            return spider.parse_chapter()
        except ValueError as e:
            logger.error(repr(e))
        

    def save_novel(self, _novel:novel):
        # @TODO:完善报错避免隐藏TypeError
        if not _novel:
            return
        self.__save_file(_novel.novel_title, str(_novel))

    def save_chapter(self, _chapter:chapter):
        _novel = self.__cur_novel 
        # @TODO:完善报错
        if not _novel or not _chapter:
            return
        self.__save_file(f'{_novel.novel_title}_{_chapter.chpater_name}', str(_chapter))


    def __save_file(self, name : str ='', content : str = ''):
        """
        @TODO:保存小说, 这里注意可以扩展追加更新和单独保存文件等功能

        注意长篇小说获取时可能出问题

        后续需要开发管理则需要保存相关元数据, 还没写配置模块所以默认保存到当前文件夹
        """
        with open(f'{name}.txt', 'wt', encoding='utf-8') as f:
            f.write(content)


        

        
    


