"""
    常量类 和 静态类 用于全局共享数据，注意区分哪些数据是不应该可修改的
"""

__all__ = ['const', 'static']

class _const:
    """定义常见返回码的常量"""
    SUCCESS = 200
    USING_PROXY = 403
    
    SLEEP = 0.01
    NAME = 'DiYiBanZhuSpider'
    DEBUG = False

    class __ConstError(TypeError):
        """修改常量抛出的错误"""

    def __init__(self):
        """初始化配置"""
        # 默认超时
        

        
    def __setattr__(self, __name: str, __value: any) -> None:
        if __name in self.__dict__:
            raise self.__ConstError(f'修改常量{__name}被阻止')
        
        self.__dict__[__name] = __value

class _static:
    """可修改的全局变量"""
    """默认网络参数"""
    base_url = 'http://www.2diyibanzhu.cc'
    timeout = 3
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Linux; U; Android 10; zh-CN; HLK-AL00 Build/HONORHLK-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.1.8.1098 Mobile Safari/537.36',
    }


const = _const()
static = _static()