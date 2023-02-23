"""
    小说
"""



class novel:
    author = None
    title = None
    def __init__(self, url:str):
        """判断入参"""
        if len(url.strip()) == 0:
            raise ValueError('输入链接为空')
        
    