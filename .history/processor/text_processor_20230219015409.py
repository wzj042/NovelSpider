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
        self.__word_name_list = []
        self.__word_text_list = []
        self.__word_md5_list = []

        try:
            
            if 'texts' not in words or len(words['texts']) == 0:
                raise ValueError(
                    '原始python字库文件(processor.word_bank.py)似乎已修改内容导致无法加载'
                )

            for word in words['texts']:
                self.__word_name_list.append(word['name'])
                self.__word_text_list.append(word['text'])
                self.__word_md5_list.append(word['md5'])

        except ValueError as e:
            logger.error(repr(e))


    def img_process(self) -> str:
        """正则匹配图片链接并替换链接"""
        pattern  = re.compile('\\w*?\\.png')

        img_list = pattern.findall(self.__solve_text)
        img_set = set(img_list)

        for img_name in img_set:

            img_text = None
            img_md5 = None
            img_index = self.__index_of(self.__word_name_list, img_name)

            if img_index == -1:
                """匹配不到图片id则获取图片md5进行查找"""
                img_md5 = get_img_md5(f'{static.base_url}')
                img_index = self.__index_of(self.__word_md5_list, img_md5)

            if img_index == -1:
                """该图片信息未加入映射字库, 暂时忽略并标记未处理"""
                img_name = f'[{static.base_url}{img_name}]'


            if not img_text:
                img_text = self.__word_text_list[img_index]


            self.__solve_text = self.__solve_text.replace(
                f'<img src="/toimg/data/{img_name}"/>', img_text
            )
        return self.__solve_text
    

    def __index_of(container : list, target):
        """实现indexOf避免抛出错误"""
        if target not in container:
            return -1
        return container.index(target) 


