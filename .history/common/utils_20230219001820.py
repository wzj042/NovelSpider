
from common.const import const
from common.logger import logger

__all__ = ['const','logger','get_img_md5']



def get_img_md5(url:str) -> str:
    """返回文件md5"""
    try:
        if len(url.strip()) == 0:
            raise ValueError(f'获取图片url为空')
    except ValueError as e:
        logger.error(repr(e))