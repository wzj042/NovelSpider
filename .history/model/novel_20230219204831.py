"""
    小说
"""
import re


class novel:
    author = None
    title = None

    def __init__(self, url:str):

        """判断入参, 获取参数"""
        if len(url.strip()) == 0:
            raise ValueError('输入链接为空')
        
        self.__match_param(url)


    def __match_param(self, url:str):
        """
        匹配小说链接中的分类，id 将页面选择"_%d"的内容忽略掉
        """
        pattern = re.compile(r'(http://|https://)?([^/]*)').search(url)
        base_url = pattern.group()
        novel_arr = url[pattern.span()[1] + 1:].split('/')

        print('base_url', base_url)
        print('novel_arr', novel_arr)

    