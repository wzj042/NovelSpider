import os
import hashlib
import json
from ujson import getJson, saveJson



folder = 'img\original'
ouput_tmp_json = r'output\text.json'

# 获取json 查重
tmpJson = getJson(ouput_tmp_json)

textImgList = []



if tmpJson is None:
    tmpJson = {
        'texts':[]
    }
else:
    for text in tmpJson['texts']:
        textImgList.append(text['imgName'])


files = os.listdir(folder)
# 添加相应的json
for fileName in files:
    if not fileName in textImgList:
        print('处理',fileName)
        file = open(f'{folder}\{fileName}','rb')
        md5 = hashlib.md5(file.read()).hexdigest()
        tmpJson['texts'].append({
            'imgName': fileName,
            'text':'丰',
            'md5': md5
        })

saveJson(ouput_tmp_json, tmpJson)
    



