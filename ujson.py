import os, json


# 封装json操作

def load_json(file_url):
    """
    加载JSON文件
    :param file_url:
    :return:
    """
    res_json = None
    if not os.path.exists(file_url):
        print('>>json文件不存在')
    else:
        with open(file_url, 'r', encoding='utf-8') as f:
            content = f.read()
            if len(content) != 0:
                res_json = json.loads(content)
                print('>>已读取json文件')
            else:
                print('>>json文件内容为空')
            f.close()
    return res_json


def save_json(file_url, json_content):
    """
    保存JSON到文件
    :param file_url:
    :param json_content:
    :return:
    """
    with open(file_url, 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_content, ensure_ascii=False, indent=4))
        print('>>已更新json文件')
        f.close()
