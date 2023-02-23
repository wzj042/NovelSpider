import logging

__all__ = ['logger']

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


def get_img_md5(url:str) -> str:
    """返回文件md5"""