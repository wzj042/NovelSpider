import os
import configparser
import re

BASE_DIR = os.path.dirname(os.path.abspath('config.ini'))
AUTO_SOLVE_TEXT = False
# 可以自己手动加上要屏蔽的广告
BAN_TEXT_LIST = []
NOVEL_LIST = []
DRIVER_URL = None

def subReplace(reg, content, repDict) -> str:
    pattern = re.compile(reg)
    matchs = pattern.findall(content)
    for line in matchs:
        for r in repDict:
            content = content.replace(line, re.sub(r, repDict[r], line))
    return content
# 处理匹配一下小说中的广告文本
def solveAdText(content) -> str:

    # 将分页的换行替换掉
    symbol = '[…，、•！～。？]'
    notEndSymbol = '[…，、•～]'
    endSymbol = '[】！。？]'
    cn = '[\u4e00-\u9fa5]'




    content = subReplace(cn+'\n+\s*'+cn, content, {
        '\n+\s*':''
    })

    adCount = 0
    for ban in BAN_TEXT_LIST:
        if ban in content:
            adCount += 1
            print(f'处理文本*{adCount}')
            content = content.replace(ban, '')

    content = subReplace('[a-zA-Z]+\n+\s*[a-zA-Z]+', content, {
        '\n+\s*':''
    })
    content = subReplace(notEndSymbol+'?'+'\n+\s*'+cn, content, {
        '\n+\s*':''
    })
    content = subReplace(notEndSymbol+'?'+'\n+\s*'+endSymbol, content, {
        '\n+\s*':''
    })
    content = subReplace(cn+'?'+'\n+\s*'+symbol, content, {
        '\n+\s*':''
    })
    # 将替换后的空白行替换掉
    
    content = re.sub('\n{3,}\s','\n',content)
    content = re.sub('\n\s{4}\n{2}','',content)
    content = re.sub('\s{4}\n\s{4}','',content)

    return content


def solveAd():
    # 遍历小说列表替换广告, 这里不打算考虑加载上mb的文件，就不分块加载了
    for root, dirs, files in os.walk("novel", topdown=False):
        for name in files:
            if '_backup' not in name:
                print(files)
                content = ''
                with open(f'{root}\{name}', 'r', encoding='utf-8') as f:
                    for line in f.readlines():
                        content += line
                    f.close()
                content = solveAdText(content)
                with open(f'{root}\{name}', 'w', encoding='utf-8') as f:
                # with open(f'{root}\{name}_backup', 'w', encoding='utf-8') as f:
                    f.write(content)
                    f.close()

    pass


def initConfg() -> dict:
    config = configparser.ConfigParser()
    config.read(os.path.join(BASE_DIR, 'config.ini'), encoding='UTF-8')
    novel_list_path = config.get('parser_config', 'novel_list_path')
    DRIVER_URL = config.get('parser_config', 'driver_path')
    AUTO_SOLVE_TEXT = config.getboolean('parser_config', 'auto_solve_text')
    solver_list_path = config.get('solver_config', 'solve_text_path')
    NOVEL_LIST = []

    with open(os.path.join(BASE_DIR, novel_list_path), 'r',
              encoding='UTF-8') as f:
        NOVEL_LIST = f.read().split('\n')
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
        'DRIVER_URL' :DRIVER_URL
    }


if __name__ == '__main__':
    initConfg()
    solveAd()
