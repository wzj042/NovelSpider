"""
    调试日志模块
"""
import logging
from common.const import const
__all__ = ['logger']


logger = logging.getLogger(const.NAME)
logger.setLevel(logging.DEBUG)

if const.DEBUG:
    print('====================DEBUG MODE====================')
    formatter = logging.Formatter(
    fmt=
    '[line:%(lineno)d] [%(levelname)s] - %(message)s')
else:
    formatter = logging.Formatter(
    fmt=
    '%(asctime)s [line:%(lineno)d] [%(filename)s] %(funcName)s %(levelname)s - %(message)s' ,
    datefmt='%Y-%m-%d %H:%M:%S')

console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)