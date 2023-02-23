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

    def __init__(self, solve_text = '') -> None:
        self.__solve_text = solve_text
        self.__text_list = []
        self.__text_img_list = []
        self.__text_md5_list = []

        # 初始化匹配文本列表
        for word in words['texts']:
            self.__text_list.append(word['text'])
            self.__text_list.append(word['name'])
            self.__text_list.append(word['md5'])

    # 正则替换图片标签
    def img_process(self) -> str:
        
        self.__solve_text = '乐'
        return self.__solve_text


logger.info('start')