"""
    暴露相关爬虫接口
"""
from model import *
from core.novel_spider import novel_spider

class diyibanzhu:

    def __init__(self):
        """初始化config配置"""

    

    def get_novel(self, url:str) -> novel:
        """传入链接返回小说实体类"""
        spider = novel_spider(url)
        _novel = spider.connect()
        """parse_novel -> get_chapter_list -> parse_chapter -> get_page_list -> parse_page"""

        return spider.connect()
        
    
    def get_chpater(self, url:str) -> chapter:
        """传入链接返回章节实体类"""
        spider = novel_spider(url)
        _novel = spider.connect()
        _chapter = chapter(url)
        if _novel:
           """可访问目录，直接测试访问章节链接""" 
           spider.parse_chapter(_chapter)

    def save_file(self, model):
        """保存小说或章节, 这里注意可以扩展追加更新和单独保存文件等功能"""

        
    


