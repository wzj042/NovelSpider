"""
    小说
"""
from model.chapter import chapter

class novel:
    
    """novel_menu_text 不显式声明的传入目录页的网页源码"""
    
    novel_title = None
    novel_author = None
    word_count = 0
    page_count = 0
    chapters = []

    def __init__(self, **kwargs):
        """传入链接获取目录页，得到小说参数接着选择获取章节还是整本获取"""
        for key, value in kwargs.items():
            self.__dict__[key] = value
        
    
        
    def __str__(self) -> str:
        return f"""url_parser = {self.url_parser}, 
        novel_title = {self.novel_title}],
        novel_author = {self.novel_author}],
        word_count = {self.word_count}],
        page_count = {self.page_count}],
        """
        pass


    
    