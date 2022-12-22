import os
import configparser
import re

BASE_DIR = os.path.dirname(os.path.abspath('config.ini'))
# 保存文件格式
NOVEL_NAME_FORMAT = "novel/{author}/{title}.txt"
# 是否打印错误
PRINT_ERROR = False
AUTO_SOLVE_TEXT = False
USE_MOBILE_UA = False
# 可以自己手动加上要屏蔽的广告
BAN_TEXT_LIST = []
NOVEL_LIST = []
DRIVER_URL = None
MOBILE_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) ' \
            'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
            'Mobile/16A366 ' \
            'MicroMessenger/6.7.3(0x16070321) ' \
            'NetType/WIFI ' \
            'Language/zh_CN '
PC_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/108.0.0.0 ' \
        'Safari/537.36 '


def sub_replace(reg, content, rep_dict) -> str:
    pattern = re.compile(reg)
    match_arr = pattern.findall(content)
    for line in match_arr:
        for r in rep_dict:
            content = content.replace(line, re.sub(r, rep_dict[r], line))
    return content


def solve_ad_text(content) -> str:
    """
    处理匹配一下小说中的广告文本
    :param content:
    :return:
    """
    # 将分页的换行替换掉
    symbol = '[…，、•！～。？]'
    not_end_symbol = '[…，、•～]'
    end_symbol = '[】！。？」》]'
    cn = '[\u4e00-\u9fa5]'
    regex_rule_0 = '\n+\\s*'
    regex_rule_1 = '?\n+\\s*'

    content = sub_replace(cn + regex_rule_0 + cn, content, {regex_rule_0: ''})
    content = sub_replace(end_symbol + regex_rule_1 + cn, content,
                          {regex_rule_0: '\n'})
    ad_count = 0
    for ban in BAN_TEXT_LIST:
        if ban in content:
            ad_count += 1
            print(f'处理文本*{ad_count}')
            content = content.replace(ban, '')

    content = sub_replace('[a-zA-Z]+\n+\\s*[a-zA-Z]+', content,
                          {regex_rule_0: ''})
    content = sub_replace(not_end_symbol + regex_rule_1 + cn, content,
                          {regex_rule_0: ''})
    content = sub_replace(not_end_symbol + regex_rule_1 + end_symbol, content,
                          {regex_rule_0: ''})
    content = sub_replace(cn + regex_rule_1 + symbol, content,
                          {regex_rule_0: ''})

    # 将替换后的空白行替换掉

    content = re.sub('\n{3,}\\s', '\n', content)
    content = re.sub('\n\\s{4}\n{2}', '', content)
    content = re.sub('\\s{4}\n\\s{4}', '', content)

    return content


def solve_ad():
    # 遍历小说列表替换广告, 这里不打算考虑加载上mb的文件，就不分块加载了
    for root, dirs, files in os.walk("novel", topdown=False):
        for name in files:
            if '_backup' not in name:
                print(name)
                content = ''
                with open(f'{root}\{name}', 'r', encoding='utf-8') as f:
                    for line in f.readlines():
                        content += line
                    f.close()
                content = solve_ad_text(content)
                with open(f'{root}\{name}', 'w', encoding='utf-8') as f:
                    # with open(f'{root}\{name}_backup', 'w', encoding='utf-8') as f:
                    f.write(content)
                    f.close()


def init_config() -> dict:
    config = configparser.ConfigParser()
    config.read(os.path.join(BASE_DIR, 'config.ini'), encoding='UTF-8')
    novel_list_path = config.get('parser_config', 'novel_list_path')
    global DRIVER_URL
    global AUTO_SOLVE_TEXT
    global USE_MOBILE_UA
    global NOVEL_NAME_FORMAT
    global PRINT_ERROR
    DRIVER_URL = config.get('parser_config', 'driver_path')
    AUTO_SOLVE_TEXT = config.getboolean('parser_config', 'auto_solve_text')
    USE_MOBILE_UA = config.getboolean('parser_config', 'use_mobile_ua')
    solver_list_path = config.get('solver_config', 'solve_text_path')
    NOVEL_NAME_FORMAT = config.get('other', 'novel_rename')
    PRINT_ERROR = config.getboolean('developer', 'print_error')

    with open(os.path.join(BASE_DIR, novel_list_path), 'r',
              encoding='UTF-8') as f:
        NOVEL_LIST.extend(f.read().split('\n'))
        f.close()
    with open(os.path.join(BASE_DIR, solver_list_path), 'r',
              encoding='UTF-8') as f:
        for ban in f.read().split('\n'):
            BAN_TEXT_LIST.append(ban)
        f.close()

    return {
        'AUTO_SOLVE_TEXT': AUTO_SOLVE_TEXT,
        'NOVEL_LIST': NOVEL_LIST,
        'BAN_TEXT_LIST': BAN_TEXT_LIST,
        'DRIVER_URL': DRIVER_URL,
        'USE_MOBILE_UA': USE_MOBILE_UA,
        'PRINT_ERROR': PRINT_ERROR,
        'NOVEL_NAME_FORMAT': NOVEL_NAME_FORMAT
    }


if __name__ == '__main__':
    init_config()
    solve_ad()
