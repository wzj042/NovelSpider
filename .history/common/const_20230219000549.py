import logging

__all__ = ['_const', 'logger']

class _const:

    class __ConstError(TypeError):
        """修改常量抛出的错误"""
        pass
    def __init__(self):
        """初始化配置"""
        
    def __setattr__(self, __name: str, __value: any) -> None:
        if __name in self.__dict__:
            raise self.__ConstError(f'修改常量{__name}被阻止')
        
        self.__dict__[__name] = __value


# 调试日志设置
logger = logging.getLogger('DiyibanzhuSpider')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    fmt=
    '%(asctime)s [line:%(lineno)d] [%(filename)s] %(funcName)s %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

