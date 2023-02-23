import cloudscraper
import hashlib
from common.const import const, static
from common.logger import logger

"""常用的模块和方法都从这个模块中暴露出去"""
__all__ = ['const', 'static', 'logger', 'get', 'get_img_md5']

scraper = cloudscraper.create_scraper()

def get(url:str,  **kwargs):
    """简单封装get方法给大部分网络请求使用"""
    resp = None
    try:
        # 参数校验
        if len(url.strip()) == 0:
            raise ValueError(f'获取url为空')
        
        # 传入可变参数默认值
        kwargs.setdefault('timeout', static.timeout)
        kwargs.setdefault('headers', static.headers)
        resp = scraper.get(url, **kwargs)
        code = resp.status_code

        # 捕获常见错误状态码
        if code == const.USING_PROXY:
            raise ConnectionError('访问失败, 请检查是否开启了代理')
        
        if code != const.SUCCESS:
            raise ConnectionError(f'访问失败,[{code}] = {resp.text}')
        
        return resp
    except (ValueError, ConnectionError) as e:
        logger.error(repr(e))

    return resp

def get_img_md5(url:str, **kwargs) -> str:
    """返回文件md5, 保存后计算图片md5, 用于校验图片与文字是否一致"""
    resp = get(url, **kwargs)

    with open('temp.png', 'wb') as f:
        f.write(resp.content)
    
    f = open('temp.png', 'rb')
    md5 = hashlib.md5(f.read()).hexdigest()
    f.close()

    return md5

    

    


