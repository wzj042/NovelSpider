"""
    调试类
"""
import logging
from common.const import const
__all__ = ['logger']

# 调试日志设置
logger = logging.getLogger(const.NAME)
logger.setLevel(logging.DEBUG)
formatter = None
if const.DEBUG:
    formater = logging.Formatter(
    fmt=
    '[line:%(lineno)d] %(funcName)s %(levelname)s - %(message)s')
else:
    formater = logging.Formatter(
    fmt=
    '%(asctime)s [line:%(lineno)d] [%(filename)s] %(funcName)s %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)