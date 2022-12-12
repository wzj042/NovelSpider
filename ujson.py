import os,json
# 封装json操作

def getJson(file_url):
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

def saveJson(file_url, save_json):
    with open(file_url, 'w', encoding='utf-8') as f:
        f.write(json.dumps(save_json, ensure_ascii=False, indent=4))
        print('>>已更新json文件')
        f.close()