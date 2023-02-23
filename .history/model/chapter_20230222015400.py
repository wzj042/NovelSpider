"""
    获取章节分卷所有页面内容
"""


class chapter:
    """目标章节链接"""
    url = None
    text = None
    def __init__(self, url:str = None):
        """保存章节内容"""
        self.url = url