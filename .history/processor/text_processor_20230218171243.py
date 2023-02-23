import re
from processor.word_bank import words

"""
    处理文本的 图片标签, 广告文本
    @TODO : 加上异常检测输出log
"""

__all__ = ['text_processor']
DEBUG = True

class text_processor :

    def __init__(self, solve_text = '') -> None:
        self.__solve_text = solve_text
        self.text_list = []
        self.text_img_list = []
        self.text_md5_list = []

        # 初始化匹配文本列表
        for text in words['texts']:


    # 正则替换图片标签
    def img_process(self) -> str:
        
        self.__solve_text = '乐' + self.__solve_text
        return self.__solve_text

