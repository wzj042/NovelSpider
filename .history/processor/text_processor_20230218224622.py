import re
from processor.word_bank import words
from common.utils import *
"""
    处理文本的 图片标签, 广告文本
    @TODO : 加上异常检测输出log
"""

__all__ = ['text_processor']
DEBUG = True

class text_processor :

    def __init__(self, solve_text : str) -> None:
        self.__solve_text = solve_text

        """初始化字库(word_bank.py)列表"""
        self.__word_name_list = []
        self.__word_img_list = []
        self.__word_md5_list = []

        for word in words['texts']:
            self.__word_text_list.append(word['text'])
            self.__word_name_list.append(word['name'])
            self.__word_md5_list.append(word['md5'])

    def img_process(self) -> str:
        """正则匹配图片链接并替换链接"""
        pattern  = re.compile('\\w*?\\.png')
        img_list = pattern.findall(self.__solve_text)
        img_set = set(img_list)
        for img in img_set:
            
            # 匹配到相应的图片id
            if self.__index_of(self.__word_img_list, img) != -1:
                """替换匹配图片id"""

            self.__solve_text = '乐'
        return self.__solve_text
    
    def __index_of(container : list, target):
        if target not in container:
            return -1
        return container.index(target) 


