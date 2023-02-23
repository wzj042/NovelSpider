import logging

from const import _const as const

__all__ = ['logger', 'const']



def get_img_md5(url:str) -> str:
    """返回文件md5"""