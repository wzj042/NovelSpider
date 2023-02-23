import cloudscraper
from common.const import const
from common.logger import logger

__all__ = ['const','logger','get_img_md5']

scraper = cloudscraper.create_scraper()

def get(url:str,  **kwargs):
    resp = None
    try:
        # 参数校验
        if len(url.strip()) == 0:
            raise ValueError(f'获取url为空')
        
        # 传入可变参数默认值
        kwargs.setdefault('timeout', const.timeout)
        kwargs.setdefault('headers', const.headers)
        resp = scraper.get(url, **kwargs)
        code = resp.status_code

        if code == const.USING_PROXY:
            raise ConnectionError('访问失败, 请检查是否开启了代理')
        
        if code != const.SUCCESS:
            raise ConnectionError(f'访问失败,[{code}] = {resp.text}')
        
        return resp
    except (ValueError, ConnectionError) as e:
        print(resp.status_code)
        
        logger.error(repr(e))

    return resp

def get_img_md5(url:str, **kwargs) -> str:
    """返回文件md5"""
    resp = get(url, kwargs=kwargs)

    


