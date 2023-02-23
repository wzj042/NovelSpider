"""
    小说
"""

class novel:
    
    __url_parser = None
    novel_author = None
    novel_title = None
    word_count = 0
    page_count = 0

    def __init__(self, **kwargs):
        """传入链接获取目录页，得到小说参数接着选择获取章节还是整本获取"""
        for key, value in kwargs.items():
            self.__dict__[key] = value
        
        
    def __str__(self) -> str:
        return f"""url_parser={self.__url_parser}, 
        novel_title={self.novel_title}]
        """
        pass


    
    