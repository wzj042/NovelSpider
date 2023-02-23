"""
    小说
"""

class novel:
    
    url_parser = None
    novel_title = None
    novel_author = None
    word_count = 0
    page_count = 0

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
        resp_text = {self.resp_text}],
        """
        pass


    
    