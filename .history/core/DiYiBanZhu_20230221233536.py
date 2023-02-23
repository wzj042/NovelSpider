"""
    暴露相关爬虫接口
"""
from model import *
from core.novel_spider import novel_spider

class diyibanzhu:

    def __init__(self):
        """初始化config配置"""

    

    def parse_novel(self, url:str) -> novel:
        """传入链接返回小说实体类"""

        
    
    def parse_chpater(self, url:str) -> chapter:
        """传入链接返回章节实体类"""

    def save_file(self, model):
        """保存小说或章节, 这里注意可以扩展追加更新和单独保存文件等功能"""

        
    


