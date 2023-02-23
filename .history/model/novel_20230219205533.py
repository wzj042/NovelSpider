"""
    小说
"""
import re
from common.utils import *

class novel:
    author = None
    title = None

    def __init__(self, url:str):

        """判断入参, 获取参数"""
        if len(url.strip()) == 0:
            raise ValueError('输入链接为空')
        
        """@TODO 编写获取章节和完整小说的不同方法"""


    
    