import cloudscraper
import hashlib
import re
# 没想到最后还是得引入requests
from requests.exceptions import ConnectionError

from common.const import const, static
from common.logger import logger

"""常用的模块和方法都从这个模块中暴露出去"""
__all__ = ['const', 'static', 'logger', 'str_is_empty', 'get', 'get_img_md5']

scraper = cloudscraper.create_scraper()

def str_is_empty(inp:str = '') -> bool:
    """校验字符串是否为空, 非字符类型会被强转为str类型"""
    if not inp or len(str(inp).strip()) == 0:
        return True
    return False 

def validate_url(url:str) -> bool:
    """简单校验url合法性"""
    if not re.match(r'^(https?|ftp|file)://.+$', url):
        return False
    return True

def get(url:str = '',  **kwargs):
    """通用get请求, 会校验url, 以及常见的返回码(common/const.py)"""
    resp = None
    try:
        """校验参数"""
        if str_is_empty(url):
            raise ValueError('获取url为空')
        
        if not validate_url(url):
            raise ValueError(f'非法的url=[{url}]')
        
        """传入可变参数默认值"""
        kwargs.setdefault('timeout', static.timeout)
        kwargs.setdefault('headers', static.headers)
        resp = scraper.get(url, **kwargs)
        code = resp.status_code

        """捕获常见错误状态码"""
        if code == const.USING_PROXY:
            resp_headers = resp.headers
            if not resp_headers and 'Server' in resp_headers and resp_headers['Server'] == 'cloudflare':
                raise ConnectionError('被cloudflare拦截导致访问失败, 请检查是否开启了代理')
            
            """
            @TODO:预计处理方式为爬取动态验证页面的源码尝试逆向绕过动态验证
            @TODO:开启代理引发的超时错误还没处理, 暂时设置了较长的timeout绕过
            """

            raise ConnectionError(f'网页需要填写动态验证:\n\n{resp.text}')
            
        
        if code != const.SUCCESS:
            raise ConnectionError(f'访问失败,[{code}] = {resp.text}')
        
    except (ValueError, ConnectionError) as e:
        resp = None
        logger.info(e.args)
        logger.error(repr(e))

    return resp

"""返回文件md5, 链接图片后计算返回内容md5, 用于校验图片与文字是否一致"""
def get_img_md5(url:str = '', **kwargs) -> str:
    resp = get(url, **kwargs)
    md5 = hashlib.md5(resp.content).hexdigest()
    return md5



    


