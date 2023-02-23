from processor.word_bank import words
"""
    将输入文本中的图片链接替换成相应文本返回
"""

__all__ = ['img_processor']
DEBUG = True

class processor :

    def __init__(self, solve_text = '') -> None:
        self.__solve_text = solve_text

    # 替换文本中的img标签，保留未捕获的原味
    def img_process(self) -> str:
        if DEBUG:
            # 测试时将替换后的文本使用中括号标记

        self.__solve_text = '乐' + self.__solve_text
        return self.__solve_text

