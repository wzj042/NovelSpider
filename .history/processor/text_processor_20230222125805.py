import re
from processor.word_bank import words
from common.utils import *
"""
    处理文本的 图片标签, 广告文本
"""

__all__ = ['text_processor']

class text_processor :

    def __init__(self, solve_text : str, **kwargs) -> None:
        """文本处理器, 处理图片标签, 推广和多余格式"""
        self.__solve_text = solve_text

        """初始化字库(word_bank.py)相关列表"""
        self.__word_name_list = []
        self.__word_text_list = []
        self.__word_md5_list = []

        try:
            
            if str_is_empty(solve_text):
                raise ValueError('空参数输入')

            if 'texts' not in words or len(words['texts']) == 0:
                raise ValueError(
                    '原始python字库文件(processor.word_bank.py)内容错误导致无法替换图片标签'
                )

            for word in words['texts']:
                self.__word_name_list.append(word['name'])
                self.__word_text_list.append(word['text'])
                self.__word_md5_list.append(word['md5'])

        except ValueError as e:
            logger.error(repr(e))


    def __img_process(self):
        """正则匹配图片链接并替换链接"""
        text = self.__solve_text
        pattern  = re.compile('\\w*?\\.png')

        img_list = pattern.findall(text)
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
                img_text = f'[{static.base_url}{img_name}]'


            if not img_text:
                img_text = self.__word_text_list[img_index]

            """或许可以改成正则, 太懒了"""
            text = re.sub(
                f'<img\s*src="/toimg/data/{img_name}"\s*/>', 
                img_text,
                text
            )
        self.__solve_text = text
    
    def __format_processor(self):
        text = self.__solve_text
        """换行format"""
        text = re.sub('(<br/>)+', '\n\n', text)
        self.__solve_text = text
    
    def get_text(self) -> str:
        text = self.__solve_text
        return text

    def __index_of(self, container : iter, target):
        """实现indexOf避免抛出错误"""
        if target not in container:
            return -1
        return container.index(target) 


