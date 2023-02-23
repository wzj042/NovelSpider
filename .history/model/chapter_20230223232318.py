"""
    获取章节分卷所有页面内容
"""


class chapter:
    """目标章节链接"""
    chapter_url = ''
    """合并处理顺序后的章节文本"""
    chapter_text = ''
    """章节名"""
    chpater_name = ''
    """分页数"""
    page_cnt = 1
    def __init__(self, chapter_url:str = ''):
        """保存和章节链接，章节内容"""
        self.chapter_url = chapter_url

    def __str__(self) -> str:
        return self.chapter_text