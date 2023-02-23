"""
    暴露相关爬虫接口
"""
from model.novel import novel

class diyibanzhu:

    def __init__(self):
        """初始化config配置"""

    def get_novel(self, url:str) -> novel:
        book = novel(str)

        return book

