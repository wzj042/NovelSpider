"""
    小说
"""
import re
from common.utils import *

class novel:
    base_url = None
    novel_url = None
    novel_author = None
    novel_title = None
    word_count = 0
    page_count = 0

    def __init__(self, url:str):
        """传入链接获取目录页，得到小说参数接着选择获取章节还是整本获取"""



    
    