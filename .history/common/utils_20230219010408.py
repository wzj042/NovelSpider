import cloudscraper
from common.const import const
from common.logger import logger

__all__ = ['const','logger','get_img_md5']

scraper = cloudscraper.create_scraper()


def get_img_md5(url:str, **kwargs) -> str:
    """返回文件md5"""
    try:
        # 参数校验
        if len(url.strip()) == 0:
            raise ValueError(f'获取图片url为空')
        
        # 传入可变参数默认值
        kwargs.setdefault('timeout', const.timeout)
        kwargs.setdefault('headers', const.headers)
        return scraper.get(url, **kwargs)
    
    except (ValueError, ConnectionError) as e:
        logger.error(repr(e))

    return None
    


