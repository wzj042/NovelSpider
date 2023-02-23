"""
    小说
"""

class novel:
    base_url = None
    novel_url = None
    novel_author = None
    novel_title = None
    word_count = 0
    page_count = 0

    def __init__(self, **kwargs):
        """传入链接获取目录页，得到小说参数接着选择获取章节还是整本获取"""
        for k in kwargs:
            print(k, kwargs[v])


    
    