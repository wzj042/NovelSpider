"""
    常量类
"""

__all__ = ['const']

class _const:
    USING_PROXY = 403
    class __ConstError(TypeError):
        """修改常量抛出的错误"""

    def __init__(self):
        """初始化配置"""
        # 默认超时
        self.timeout = 15
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Linux; U; Android 10; zh-CN; HLK-AL00 Build/HONORHLK-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.1.8.1098 Mobile Safari/537.36',

        }

        
    def __setattr__(self, __name: str, __value: any) -> None:
        if __name in self.__dict__:
            raise self.__ConstError(f'修改常量{__name}被阻止')
        
        self.__dict__[__name] = __value


const = _const()
