"""
    常量类
"""

__all__ = ['const']

class _const:

    class __ConstError(TypeError):
        """修改常量抛出的错误"""

    def __init__(self):
        """初始化配置"""
        # 默认超时
        self.timeout = 15
        self.headers = {

        }
        
    def __setattr__(self, __name: str, __value: any) -> None:
        if __name in self.__dict__:
            raise self.__ConstError(f'修改常量{__name}被阻止')
        
        self.__dict__[__name] = __value


const = _const()
