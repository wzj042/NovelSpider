"""
    获取章节分卷所有页面内容
"""


class chapter:
    """目标章节链接"""
    url = None
    """合并处理顺序后的章节文本"""
    text = None
    def __init__(self, url:str = None):
        """保存和章节链接，章节内容"""
        self.url = url

    def __str__(self) -> str:
        s = ''
        for key,value in self.__dict__.items():
            s += f'{key} = {value}, '
        return s