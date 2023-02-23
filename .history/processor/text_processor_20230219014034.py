import re
from processor.word_bank import words
from common.utils import *
"""
    处理文本的 图片标签, 广告文本
"""

__all__ = ['text_processor']

class text_processor :

    def __init__(self, solve_text : str) -> None:
        self.__solve_text = solve_text

        """初始化字库(word_bank.py)相关列表"""
        self.__word_text_list = []
        self.__word_name_list = []
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
        for img_name in img_set:

            img_name = None
            img_md5 = None
            img_index = self.__index_of(self.__word_img_list, img_name)

            if img_index == -1:
                """匹配不到图片id则获取图片md5进行查找"""
                img_md5 = get_img_md5(f'{static.base_url}')
            

            self.__solve_text = '乐'
        return self.__solve_text
    

    def __index_of(container : list, target):
        """实现indexOf避免抛出错误"""
        if target not in container:
            return -1
        return container.index(target) 


