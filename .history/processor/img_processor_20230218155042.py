from processor.word_bank import words
"""
    将输入文本中的图片链接替换成相应文本返回
"""

__all__ = ['processor']

class processor :
    def __init__(self, solve_text = '') -> None:
        self.__solve_text = solve_text
        pass
    def process(self) -> str:
        self.__solve_text = '乐' + self.__solve_text
        return self.__solve_text

